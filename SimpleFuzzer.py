from FuzzerBase import FuzzerBase
from utils import custom_types, type_combos
from inspect import signature
import random
import time
# from utils import builtin_types

class SimpleFuzzer(FuzzerBase):
    """A simple, not-very-intelligent fuzzer. It randomly tries different combinations of types, records the ones that work, and returns those."""

    def __init__(self, name = ''):
        """Can set a custom name for the fuzzer, or use class name by default."""
        super().__init__(name)

    def fuzz_single_param(self, func):
        """Returns all possible parameter types of a function that takes in a single parameter.

        func -- the function to be fuzzed, which takes one parameter.
        """

        allowed_types = set()

        for test_type in custom_types():
            try:
                test_wrapper = test_type()
                func(test_wrapper.getVal())
                allowed_types.add(test_wrapper.get_type())
            except (TypeError, AttributeError):
                continue
            except:
                allowed_types.add(test_wrapper.get_type())

        return allowed_types

    def fuzz_multi_param_deterministic(self, func):
        """Fuzzes a function by trying all possible default types deterministically.
        """
        success = False
        total_tries = 0
        tries_until_success = 0
        start_time = time.perf_counter()

        sig = signature(func)
        n = len(sig.parameters)
        allowed_types = set()
        for i in type_combos(n):
            try:
                func(*[i.getVal() for i in i[0]])
                allowed_types.add(i[1])

                if not success:
                    tries_until_success = total_tries
                success = True

            except (TypeError, AttributeError):
                continue

            except Exception:
                allowed_types.add(i[1])
                if not success:
                    tries_until_success = total_tries
                success = True

            finally:
                total_tries += 1
        self.record_fuzz(success, time.perf_counter() - start_time, tries_until_success, len(allowed_types))
        return allowed_types

    def fuzz_multi_param_random(self, func, num_trials):
        """Randomly tries type combinations for the required trials"""

        success = False
        total_tries = 0
        tries_until_success = 0
        start_time = time.perf_counter()


        sig = signature(func)
        n = len(sig.parameters)
        allowed_types = set()
        params = [None] * n
        for i in range(num_trials):
            for i in range(n):
                params[i] = random.choice(custom_types())()
            try:
                func(*tuple(i.getVal() for i in params))
                allowed_types.add(tuple(x.get_type() for x in params))

                if not success:
                    tries_until_success = total_tries
                success = True

            except (TypeError, AttributeError) as error:
                continue

            except:
                allowed_types.add(tuple(x.get_type() for x in params))
                if not success:
                    tries_until_success = total_tries
                success = True

            finally:
                total_tries += 1
        self.record_fuzz(success, time.perf_counter() - start_time, tries_until_success, len(allowed_types))
        return allowed_types


    
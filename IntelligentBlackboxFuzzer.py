import builtins as b
import pprint
from FuzzerBase import FuzzerBase
from utils import custom_types
from inspect import signature
import random
import re
import time


class IntelligentBlackboxFuzzer(FuzzerBase):
    """A much more intelligent version of the SimpleFuzzer - it tries to fuzz types based on the TypeError message content. (Blackbox)"""
    def __init__(self, name = ""):
        super().__init__(name)
        
    def fuzz(self, func, max_trials = 1000):
        success = False
        total_tries = 0
        tries_until_success = 0
        start_time = time.perf_counter()
        sig = signature(func)
        n = len(sig.parameters)

        allowed_types = set()
        failed_types = set()

        #Initially, seed the parameters with random values
        params = IntelligentBlackboxFuzzer.generate_random_params(n)
        
        for i in range(max_trials):
            try:
                # Try to pass in the parameters to the function
                func(*(j.getVal() for j in params))

                # If this line is reached without an error, the function ran successfully
                allowed_types.add(tuple(x.get_type() for x in params))
                
                #Instrumentation
                if not success:
                    tries_until_success = total_tries
                success = True

                #Reseed to continue searching for types
                params = IntelligentBlackboxFuzzer.generate_random_params(n)

            except (TypeError, AttributeError) as error:
                # Track failed types to avoid repeating previously-seen combos
                failed_types.add(tuple(x.get_type() for x in params))

                # Find and normalize types seen in error message
                match = re.findall("Str|Bool|Int|Float|Bytes|Complex|List|Dict|Tuple|Set|Frozenset|str|bool|int|float|bytes|complex|list|dict|tuple|set|frozenset", str(error))
                match = [m.capitalize() for m in match]

                # Try to swap out every type found in error message
                while match:
                    type = random.choice(match)
                    match.remove(type)
                    matching_params = list()                    
                    for j in range(len(params)):
                        if (params[j].get_type()) == type:
                            matching_params.append(j)

                    if len(matching_params) > 0:
                        break
                
                # If no params were found, re-randomize and continue
                if not matching_params:
                    for j in range(n):
                        params[j] = random.choice(custom_types())()
                    continue

                # Try replacing the parameter an arbitrary number of times. If this continually generates combinations seen before, re-randomize and continue 
                num_trials = 0
                while tuple(x.get_type() for x in params) in failed_types:
                    if num_trials > 20:
                        break
                    mutant_ind = random.choice(matching_params)
                    params[mutant_ind] = random.choice(custom_types())()
                    num_trials += 1
            except:
                # If another exception is generated, assume it is some sort of unrelated error (out of bounds, etc.), and add it to the allowed types list.
                allowed_types.add(tuple(x.get_type() for x in params))

                #Instrumentation
                if not success:
                    tries_until_success = total_tries
                success = True

                for i in range(n):
                    params[i] = random.choice(custom_types())()
            finally:
                total_tries += 1
        self.record_fuzz(success, time.perf_counter() - start_time, tries_until_success, len(allowed_types))
        return allowed_types


    @staticmethod
    def generate_random_params(n):
        return [random.choice(custom_types())() for i in range(n)]
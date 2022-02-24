import builtins as b
import pprint
from utils import custom_types, type_combos
from inspect import signature
import random
# from utils import builtin_types

class SimpleFuzzer:
    def __init__(self):
        pass

    def fuzz_single_param(self, func):
        allowed_types = set()
        for i in custom_types():
            try:
                test_wrapper = i()
                func(test_wrapper.getVal())
                allowed_types.add(test_wrapper.get_type())
            except TypeError:
                continue
        return allowed_types

    def fuzz_multi_param(self, func):
        sig = signature(func)
        n = len(sig.parameters)
        print(n)
        allowed_types = set()
        for i in type_combos(n):
            try:
                func(*[i.getVal() for i in i[0]])
                allowed_types.add(i[1])
            except TypeError:
                continue
            except:
                allowed_types.add(i[1])
        return allowed_types

    def fuzz_multi_param_2(self, func, num_trials):
        # At every point, depending on where the error is, change the variable
        sig = signature(func)
        n = len(sig.parameters)
        param_names = sig.parameters.keys()

        
        allowed_types = set()
        params = [None] * n
        for i in range(num_trials):
            for i in range(n):
                params[i] = random.choice(custom_types())()
            # print(list(map(lambda x: x.get_type(), params)))
            try:
                func(*tuple(i.getVal() for i in params))
                allowed_types.add(tuple(x.get_type() for x in params))
            except TypeError as error:
                continue
            except:
                allowed_types.add(tuple(x.get_type() for x in params))
        return allowed_types
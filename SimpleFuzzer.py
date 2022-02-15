import builtins as b
import pprint
from utils import simple_func, custom_types, type_combos
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
                allowed_types.add(test_wrapper.actualType())
            except TypeError:
                continue
        return allowed_types

    def fuzz_multi_param(self, func, n):
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

    def fuzz_multi_param_2(self, func, n):
        # At every point, depending on where the error is, change the variable
        
        allowed_types = set()
        for i in custom_types():
            try:
                func(i())
                allowed_types.add(i)
            except TypeError:
                continue
        return allowed_types
        
from .type_wrappers import *
from .test_cases import *
import builtins as b

def builtin_types():
    return [t
            for t in b.__dict__.values()
            if isinstance(t, type) and t not in [super, memoryview, classmethod, enumerate, filter, map, range, reversed, slice, staticmethod, type]]

def types():
    return set([int, float, bool, list, bytes, str, dict, set, frozenset, complex, tuple])

def custom_types() -> list[BaseType]:
    return [Int, Float, Bool, Bytes, Str, Complex, List, Dict, Tuple, Set, Frozenset]

def type_combos(n):
    if n == 1:
        for i in custom_types():
            curr_obj = i()
            yield [(curr_obj, ), (curr_obj.get_type(), )]
    else:
        for i in custom_types():
            for j in type_combos(n - 1):
                curr_obj = i()
                yield [(curr_obj, *(j[0])), (curr_obj.get_type(), *(j[1]))]

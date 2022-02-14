from .test_cases import *
import builtins as b

def builtin_types():
    return [t
            for t in b.__dict__.values()
            if isinstance(t, type) and t not in [super, memoryview, classmethod, enumerate, filter, map, range, reversed, slice, staticmethod, type]]

def types():
    return set([int, float, bool, list, bytes, str, dict, set, frozenset, complex, tuple])

def type_combos(n):
    out = []
    if n == 1:
        for i in types():
            print(i)
            out.append([(i(), ), (i, )])
    else:
        for i in types():
            for j in type_combos(n - 1):
                out.append([(i(), *(j[0])), (i, *(j[1]))])
    return out
from utils import simple_func, simple_multi_param
from utils.type_wrappers import *
from utils import custom_types

from SimpleFuzzer import SimpleFuzzer

print(SimpleFuzzer().fuzz_multi_param(simple_multi_param, 2))

# print(SimpleFuzzer().fuzz_single_param(simple_func))
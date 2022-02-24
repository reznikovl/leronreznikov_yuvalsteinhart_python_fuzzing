from utils import simple_func, simple_multi_param
from utils.type_wrappers import *

from SimpleFuzzer import SimpleFuzzer

print(SimpleFuzzer().fuzz_multi_param_2(simple_multi_param, 30))

# print(SimpleFuzzer().fuzz_single_param(simple_func))
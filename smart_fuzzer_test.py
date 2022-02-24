from utils import simple_func, simple_multi_param, complex_1
from utils.type_wrappers import *

from Fuzzer2 import Fuzzer2

print(Fuzzer2().fuzz(complex_1, 100))
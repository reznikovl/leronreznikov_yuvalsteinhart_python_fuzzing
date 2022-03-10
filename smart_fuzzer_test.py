from utils import simple_func, simple_multi_param, complex_1, complex_2
from utils.type_wrappers import *

from IntelligentBlackboxFuzzer import IntelligentBlackboxFuzzer
x = IntelligentBlackboxFuzzer()

for _ in range(10):
    x.fuzz(complex_2, 1000)
x.display_all_plots()
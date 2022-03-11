from utils import simple_func, simple_multi_param, complex_1, complex_2
from utils.type_wrappers import *

from IntelligentBlackboxFuzzer import IntelligentBlackboxFuzzer
from WhiteboxFuzzer import WhiteBoxFuzzer
from SimpleFuzzer import SimpleFuzzer

smart_blackbox = IntelligentBlackboxFuzzer()
white_box = WhiteBoxFuzzer()
simple = SimpleFuzzer()

for _ in range(10):
    simple.fuzz_multi_param_random(complex_2, 1000)
    smart_blackbox.fuzz(complex_2, 1000)
    white_box.fuzz(complex_2, 1000)
    
simple.display_all_plots()
smart_blackbox.display_all_plots()
white_box.display_all_plots()
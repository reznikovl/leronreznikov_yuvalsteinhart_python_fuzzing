from utils import simple_func, simple_multi_param, complex_1, four_params
from utils.type_wrappers import *
from utils import type_combos

from SimpleFuzzer import SimpleFuzzer

# print(SimpleFuzzer().fuzz_multi_param_2(simple_multi_param, 30))
det = SimpleFuzzer("Deterministic Simple Fuzzer")
ran = SimpleFuzzer('Random Simple Fuzzer')
for i in range(2):
    det.fuzz_multi_param_deterministic(four_params)
    ran.fuzz_multi_param_random(four_params, 10000)

det.display_all_plots()
ran.display_all_plots()

# SimpleFuzzer().plot_time_to_fuzz()

# print(SimpleFuzzer().fuzz_single_param(simple_func))
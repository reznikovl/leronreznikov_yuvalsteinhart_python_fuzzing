from utils import simple_func, simple_multi_param, complex_1, complex_2
from utils.type_wrappers import *
import matplotlib.pyplot as plt

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

simple_title, simple_fuzztime, simple_successful_combos, simple_tries_until_success = simple.dump_all_data()
smart_title, smart_fuzztime, smart_successful_combos, smart_tries_until_success = smart_blackbox.dump_all_data()
white_box_title, white_box_fuzztime, white_box_successful_combos, white_box_tries_until_success = white_box.dump_all_data()

labels = [simple_title, smart_title, white_box_title]

# Fuzz time plot
plt.boxplot([simple_fuzztime, smart_fuzztime, white_box_fuzztime], labels = labels)
plt.ylabel('Time Taken (s)')
plt.title('Time Taken Per Run')
plt.show()

# Fuzz Succesful Combos
plt.boxplot([simple_successful_combos, smart_successful_combos, white_box_successful_combos], labels = labels)
plt.ylabel("Combinations Generated Per Run")
plt.title("Successful Combinations Generated")
plt.show()

# Fuzz Tries until Success
plt.boxplot([simple_tries_until_success, smart_tries_until_success, white_box_tries_until_success], labels = labels)
plt.ylabel("Tries Until Success")
plt.title("Tries Until Success Per Successful Run")
plt.show()
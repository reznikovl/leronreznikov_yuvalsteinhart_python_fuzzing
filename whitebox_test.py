from utils import simple_func, simple_multi_param, complex_1, complex_2, complex_3
from utils.type_wrappers import *

from WhiteboxFuzzer import WhiteBoxFuzzer


# WhiteBoxFuzzer(complex_3).call_graph()
print(WhiteBoxFuzzer(simple_multi_param).fuzz())

# from pycallgraph3 import PyCallGraph
# from pycallgraph3 import Config
# from pycallgraph3 import GlobbingFilter
# from pycallgraph3.output import GraphvizOutput
from utils import gen_cfg, to_graph
from graphviz import Source, Digraph
import inspect


class WhiteBoxFuzzer:

    def __init__(self, func):
        self.function_ = func

    def call_graph(
        self,
        # output_png="call_graph_png",
        # custom_include=None

    ):
        cfg = gen_cfg(inspect.getsource(self.function_))
        to_graph(cfg)

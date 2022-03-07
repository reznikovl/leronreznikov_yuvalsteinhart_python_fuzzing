# from pycallgraph3 import PyCallGraph
# from pycallgraph3 import Config
# from pycallgraph3 import GlobbingFilter
# from pycallgraph3.output import GraphvizOutput
from FuzzerBase import FuzzerBase
from utils import gen_cfg, to_graph, complex_1, rich_output, showast
from graphviz import Source, Digraph
import inspect
import ast



class WhiteBoxFuzzer(FuzzerBase):

    def __init__(self, func, name = ""):
        self.function_ = func

    def call_graph(
        self,
        # output_png="call_graph_png",
        # custom_include=None

    ):
        cfg = gen_cfg(inspect.getsource(self.function_))
        to_graph(cfg)
    
    def fuzz(self):
        sig = inspect.signature(self.func)
        n = len(sig.parameters)
        param_names = sig.parameters.keys()
        param_constraints = dict()
        for i in param_names:
            param_constraints[i] = []
        src = inspect.getsource(self.func)
        func_ast = ast.parse(src)
        showast.show_ast(func_ast)
        


# def token_to_magic(tok):
#     tokenizer = {
#         '+': '__add__',
#         'abs': '__abs__',
#         'and': '__and__',
#         'bool': '__bool__',
#         'ceil': '__ceil__',
#         'class': '__class__',
#         'delattr': '__delattr__',
#         'dir': '__dir__',
#         'divmod': '__divmod__',
#         'doc': '__doc__',
#         '==': '__eq__',
#         'float': '__float__',
#         'floor': '__floor__',
#         '//': '__floordiv__',
#         'format': '__format__',
#         '>=': '__ge__',
#         'getattribute': '__getattribute__',
#         '>': '__gt__',
#         'hash': '__hash__',
#         'index': '__index__',
#         'int': '__int__',
#         '~': '__invert__',
#         '<=': '__le__',
#         '<<': '__lshift__'.
        
#         'setattr': '__setattr__',
#         'size_of': '__sizeof__',
#         'str': '__str__'
#         '-': '__sub__',
#         'trunc': '__trunc__'
#         '^': '__xor__'
#     }

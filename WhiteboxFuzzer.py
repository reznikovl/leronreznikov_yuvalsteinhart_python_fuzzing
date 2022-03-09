# from pycallgraph3 import PyCallGraph
# from pycallgraph3 import Config
# from pycallgraph3 import GlobbingFilter
# from pycallgraph3.output import GraphvizOutput
from FuzzerBase import FuzzerBase
from utils import gen_cfg, to_graph, complex_1, rich_output
from graphviz import Source, Digraph
import inspect
import ast

param_constraints = dict()

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
        sig = inspect.signature(self.function_)
        n = len(sig.parameters)
        param_names = sig.parameters.keys()
        global param_constraints
        param_constraints = dict()
        for i in param_names:
            param_constraints[i] = []
        src = inspect.getsource(self.function_)
        func_ast = ast.parse(src)
        print(ast.dump(ast.parse(src)))
        
        
        

class visitor(ast.NodeVisitor):
    def visit_Attribute(self, node: Attribute) -> Any:
        param = node.Name
        if param in param_constraints:
            param_constraints[param].append(node.attr)
        return super().visit_Attribute(node)

    def visit_BinOp(self, node: BinOp) -> Any:
        try:
            param = node.left.Name
            if param in param_constraints:
                param_constraints[param].append(node.op)
        except:
            pass
        return super().visit_BinOp(node)

    def visit_BoolOp(self, node: BoolOp) -> Any:
        try:
            param = node.left.Name
            if param in param_constraints:
                param_constraints[param].append(node.op)
        except:
            pass
        return super().visit_BoolOp(node)
    
    def visit_Call(self, node: Call) -> Any:
        try:
            param = node.args[0].Name
            if param in param_constraints:
                param_constraints[param].append(node.func.Name)
        except:
            pass
        return super().visit_Call(node)
    
    def visit_Compare(self, node: Compare) -> Any:
        return super().visit_Compare(node)

    def visit_Constant(self, node: Constant) -> Any:
        return super().visit_Constant(node)
    
    def visit_ListComp(self, node: ListComp) -> Any:
        return super().visit_ListComp(node)
                    
    def visit_Set(self, node: Set) -> Any:
        return super().visit_Set(node)
    
    def visit_SetComp(self, node: SetComp) -> Any:
        return super().visit_SetComp(node)
    
    def visit_Slice(self, node: Slice) -> Any:
        return super().visit_Slice(node)
        
    def visit_Subscript(self, node: Subscript) -> Any:
        return super().visit_Subscript(node)
    
    def visit_Tuple(self, node: Tuple) -> Any:
        return super().visit_Tuple(node)
    
    def visit_UnaryOp(self, node: UnaryOp) -> Any:
        return super().visit_UnaryOp(node)
    
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

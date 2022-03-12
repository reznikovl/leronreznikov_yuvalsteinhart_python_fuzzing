from FuzzerBase import FuzzerBase
from utils import custom_types, type_wrappers, types
from graphviz import Source, Digraph
import inspect
import ast
from typing import *
import random
import datetime
import time

param_constraints = dict()
out_of_consideration = set()
random.seed(datetime.datetime.now())


class WhiteBoxFuzzer(FuzzerBase):
    """A whitebox fuzzer that uses a function's AST to generate type constraints."""

    def __init__(self, name = ""):
        super().__init__(name)
    
    def fuzz(self, func, max_trials=1000):
        global param_constraints
        global out_of_consideration
        success = False
        total_tries = 0
        tries_until_success = 0
        start_time = time.perf_counter()

        sig = inspect.signature(func)
        param_names = sig.parameters.keys()
        
        param_constraints = dict()
        out_of_consideration = set()
        
        # Initially, start with empty constraints
        for i in param_names:
            param_constraints[i] = []
        src = inspect.getsource(func)
        func_ast = ast.parse(src)

        # Generate the ast, and build the constraints
        visitor().visit(func_ast)

        # Need to ensure particular type combo actually works
        result = {}
        for param, constraints in param_constraints.items():
            result[param] = []
            for curr_type in custom_types():
                if all([constraint in dir(curr_type) for constraint in constraints]):
                    # Some default type matches the constraints!
                    result[param].append(curr_type)
            if not result[param]:
                #No default type has requirements
                raise TypeError

        attempted_combos = set()
        allowed_combos = set()

        #Similarly to our other fuzzers, we try all combinations until we find some that work.
        for i in range(max_trials):
            try:
                inp = tuple([random.choice(result[i]) for i in sig.parameters])
                if inp in attempted_combos:
                    inp = tuple([random.choice(result[i]) for i in sig.parameters])
                    continue
                func(*(j() for j in inp))
                allowed_combos.add(inp)
                if not success:
                    tries_until_success = total_tries
                success = True
            except (TypeError, AttributeError):
                attempted_combos.add(tuple(inp))
            except:
                allowed_combos.add(inp)
                if not success:
                    tries_until_success = total_tries
                success = True
        self.record_fuzz(success, time.perf_counter() - start_time, tries_until_success, len(allowed_combos))
        return allowed_combos

        
        
        

class visitor(ast.NodeVisitor):
    """AST visitor. 
    
    For all "interesting" / constraint-generating nodes, we determine if it is a parameter, and if so add the constraints to the global dict"""
    def visit_Attribute(self, node: ast.Attribute) -> Any:
        param = node.value.id
        if param in param_constraints and param not in out_of_consideration:
            param_constraints[param].append(node.attr)
        return super().generic_visit(node)

    def visit_BinOp(self, node: ast.BinOp) -> Any:
        try:
            param = node.left.id
            if param in param_constraints and param not in out_of_consideration:
                param_constraints[param].append(binop_tostr(node.op))
        except:
            pass
        return super().generic_visit(node)

    def visit_BoolOp(self, node: ast.BoolOp) -> Any:
        try:
            param = node.left.id
            if param in param_constraints and param not in out_of_consideration:
                param_constraints[param].append(boolop_tostr(node.op))
        except:
            pass
        return super().generic_visit(node)
    
    def visit_Compare(self, node: ast.Compare) -> Any:
        try:
            param = node.left.id
            if param in param_constraints and param not in out_of_consideration:
                param_constraints[param].append(compare_tostr(node.ops[0]))
        except:
            pass
        try:
            param = node.comparators[0].id
            if param in param_constraints and param not in out_of_consideration:
                param_constraints[param].append(compare_tostr(node.ops[0]))
        except:
            pass
        return super().generic_visit(node)

    def visit_ListComp(self, node: ast.ListComp) -> Any:
        try:
            param = node.iter.id
            if param in param_constraints and param not in out_of_consideration:
                param_constraints[param].append('__iter__')
        except:
            pass
        return super().generic_visit(node)
    
    def visit_comprehension(self, node: ast.comprehension) -> Any:
        try:
            param = node.iter.id
            if param in param_constraints and param not in out_of_consideration:
                param_constraints[param].append('__iter__')
        except:
            pass
        return super().generic_visit(node)
                    
    
    def visit_Slice(self, node: ast.Slice) -> Any:
        try:
            param1 = node.lower.id
            if param1 in param_constraints and param1 not in out_of_consideration:
                param_constraints[param1].append("__int__")
        except:
            pass
        try:
            param2 = node.upper.id
            if param2 in param_constraints and param2 not in out_of_consideration:
                param_constraints[param2].append("__int__")
        except:
            pass
        return super().generic_visit(node)
        
    def visit_Subscript(self, node: ast.Subscript) -> Any:
        try:
            param = node.value.id
            if param in param_constraints and param not in out_of_consideration:
                param_constraints[param].append("index")
        except:
            pass
        return super().generic_visit(node)
    
    def visit_UnaryOp(self, node: ast.UnaryOp) -> Any:
        try:
            param = node.operand.id
            if param in param_constraints and param not in out_of_consideration:
                param_constraints[param].append(unop_tostr(node.op))
        except:
            pass
        return super().generic_visit(node)
    
    def visit_AugAssign(self, node: ast.AugAssign) -> Any:
        try:
            param = node.target.id
            if param in param_constraints and param not in out_of_consideration:
                param_constraints[param].append(binop_tostr(node.op))
        except:
            pass
        try:
            param = node.value.id
            if param in param_constraints and param not in out_of_consideration:
                param_constraints[param].append(binop_tostr(node.op))
        except:
            pass
        return super().generic_visit(node)

    def visit_Assign(self, node: ast.Assign) -> Any:
        try:
            param = node.targets[0].id
            if param in param_constraints and param not in out_of_consideration:
                out_of_consideration.add(param)
        except:
            pass
        return super().generic_visit(node)
    
    def visit_For(self, node: ast.For) -> Any:
        try:
            param = node.iter.id
            if param in param_constraints and param not in out_of_consideration:
                param_constraints[param].append("__iter__")
        except:
            pass
        return super().generic_visit(node)


def binop_tostr(node):
    ops = {
        ast.Add: "__add__",
        ast.Sub: "__sub__",
        ast.Mult: "__mul__",
        ast.Div: "__div__",
        ast.FloorDiv: "__floordiv__",
        ast.Mod: "__mod__",
        ast.Pow: "__pow__",
        ast.LShift: "__lshift__",
        ast.RShift: "__rshift__",
        ast.BitOr: "__or__",
        ast.BitXor: "__xor__",
        ast.BitAnd: "__and__"
    }
    return ops[type(node)]

def boolop_tostr(node):
    if type(node) == ast.And:
        return "__and__"
    else:
        return "__or__"

def compare_tostr(node):
    ops = {
        ast.Eq: "__eq__",
        ast.NotEq: "__neq__",
        ast.Lt: "__lt__",
        ast.LtE: "__lte__",
        ast.Gt: "__gt__",
        ast.GtE: "__gte__",
        ast.Is: "__init__",
        ast.IsNot: "__init__",
        ast.In: "__iter__",
        ast.NotIn: "__iter__"
    }
    return ops[type(node)]

def unop_tostr(node):
    ops = {
        ast.UAdd: "__uadd__",
        ast.USub: "__usub__",
        ast.Not: "__not__",
        ast.Invert: "__invert__"
    }
    return ops[type(node)]

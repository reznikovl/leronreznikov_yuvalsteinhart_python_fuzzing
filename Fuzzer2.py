import builtins as b
import pprint
from utils import custom_types, type_combos
from inspect import signature
import random
import re


class Fuzzer2:
    def __init__(self):
        pass


    def fuzz(self, func, num_trials = 1000):
        sig = signature(func)
        n = len(sig.parameters)
        param_names = sig.parameters.keys()

        allowed_types = set()
        params = [None] * n

        failed_types = set()

        #pick random attempts for params
        for i in range(n):
            params[i] = random.choice(custom_types())()
        for i in range(num_trials):
            print(list(map(lambda x: x.get_type(), params)))
            try:
                # Try to pass in 
                func(*(j.getVal() for j in params))
                allowed_types.add(tuple(x.get_type() for x in params))
                for i in range(n):
                    params[i] = random.choice(custom_types())()
            except (TypeError, AttributeError) as error:
                print(error)
                failed_types.add(tuple(x.get_type() for x in params))
                match = re.findall("Str|Bool|Int|Float|Bytes|Complex|List|Dict|Tuple|Set|Frozenset|str|bool|int|float|bytes|complex|list|dict|tuple|set|frozenset", str(error))
                match = [m.capitalize() for m in match]
                while match:
                    type = random.choice(match)
                    match.remove(type)
                    matching_params = list()                    
                    for j in range(len(params)):
                        if (params[j].get_type()) == type:
                            matching_params.append(j)
                    if len(matching_params) > 0:
                        break
                if not matching_params:
                    for j in range(n):
                        params[j] = random.choice(custom_types())()
                    continue
                num_trials = 0
                while tuple(x.get_type() for x in params) in failed_types:
                    if num_trials > 20:
                        break
                    mutant_ind = random.choice(matching_params)
                    params[mutant_ind] = random.choice(custom_types())()
                    # print(tuple(x.get_type() for x in params))
                    num_trials += 1
                continue
            except:
                allowed_types.add(tuple(x.get_type() for x in params))
                for i in range(n):
                    params[i] = random.choice(custom_types())()
        return allowed_types
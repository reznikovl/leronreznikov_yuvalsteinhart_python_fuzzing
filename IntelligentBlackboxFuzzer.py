import builtins as b
import pprint
from FuzzerBase import FuzzerBase
from utils import custom_types
from inspect import signature
import random
import re


class IntelligentBlackboxFuzzer(FuzzerBase):
    """A much more intelligent version of the SimpleFuzzer - it tries to fuzz types based on the TypeError message content. (Blackbox)"""
    def fuzz(self, func, num_trials = 1000):
        sig = signature(func)
        n = len(sig.parameters)

        allowed_types = set()
        failed_types = set()

        #Initially, seed the parameters with random values
        params = IntelligentBlackboxFuzzer.generate_random_params(n)
        
        for i in range(num_trials):
            print(list(map(lambda x: x.get_type(), params)))
            try:
                # Try to pass in the parameters to the function
                func(*(j.getVal() for j in params))

                # If this line is reached without an error, the function ran successfully
                allowed_types.add(tuple(x.get_type() for x in params))

                #Reseed to continue searching for types
                params = IntelligentBlackboxFuzzer.generate_random_params(n)

            except (TypeError, AttributeError) as error:
                print(error)
                
                # Track failed types to avoid repeating previously-seen combos
                failed_types.add(tuple(x.get_type() for x in params))

                # Find and normalize types seen in error message
                match = re.findall("Str|Bool|Int|Float|Bytes|Complex|List|Dict|Tuple|Set|Frozenset|str|bool|int|float|bytes|complex|list|dict|tuple|set|frozenset", str(error))
                match = [m.capitalize() for m in match]

                # Try to swap out every type found in error message
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


    @staticmethod
    def generate_random_params(n):
        return [random.choice(custom_types()) for i in range(n)]
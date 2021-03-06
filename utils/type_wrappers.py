import random
import string

from pandas import value_counts

def generateRandomType():
    possibilities = [Int, Float, Bool, Bytes, Str, Complex]
    return random.choice(possibilities)

class BaseType:
    def __init__(self):
        self.generate()
    def generate(self):
        pass
    def getVal(self):
        return self.val
    def __repr__(self):
        return str(self.val)
    def get_type(self):
        return type(self.val).__name__.capitalize()

class Int(BaseType, int):
    def generate(self):
        self.val = random.randint(-2 ** 31, 2 ** 31)

class Float(BaseType, float):
    def generate(self):
        self.val = random.random() * random.randint(-1000, 1000)

class Bool(BaseType, int):
    def generate(self):
        if (random.random()) > .5:
            self.val = True
        else:
            self.val = False

class Bytes(BaseType, bytes):
    def generate(self):
        self.val = random.randbytes(random.randint(1, 100))

class Str(BaseType, str):
    def generate(self):
        possibilities = string.ascii_letters + string.digits + string.punctuation
        self.val = ''.join(random.choice(possibilities) for _ in range(random.randint(1, 100)))

class Complex(BaseType, complex):
    def generate(self):
        self.val = complex(Float().getVal(), Float().getVal())

class List(BaseType, list):
    def generate(self):
        self.val = []
        data_type = generateRandomType()
        for _ in range(random.randint(1, 10)):
            self.val.append(data_type())

class Dict(BaseType, dict):
    def generate(self):
        self.val = {}
        key_type = generateRandomType()
        val_type = generateRandomType()
        for _ in range(random.randint(1, 10)):
            self.val[key_type()] = val_type()

class Tuple(BaseType, tuple):
    def generate(self):
        self.val = tuple(List().getVal())

class Set(BaseType, set):
    def generate(self):
        self.val = set(List().getVal())

class Frozenset(BaseType, frozenset):
    def generate(self):
        self.val = frozenset(List().getVal())
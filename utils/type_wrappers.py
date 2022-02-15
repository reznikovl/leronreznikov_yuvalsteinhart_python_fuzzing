import random
import string

def generateRandomObject():
    possibilites = [Int, Float, Bool, Bytes, Str, Complex]
    return random.choice(possibilites)()

class BaseType:
    def __init__(self):
        self.generate()
    def generate(self):
        pass
    def getVal(self):
        return self.val
    def __repr__(self):
        return str(self.val)
    def actualType(self):
        return type(self.val)

class Int(BaseType):
    def generate(self):
        self.val = random.randint(-2 ** 31, 2 ** 31)

class Float(BaseType):
    def generate(self):
        self.val = random.random() * random.randint(-1000, 1000)

class Bool(BaseType):
    def generate(self):
        if (random.random()) > .5:
            self.val = True
        else:
            self.val = False

class Bytes(BaseType):
    def generate(self):
        self.val = random.randbytes(random.randint(1, 100))

class Str(BaseType):
    def generate(self):
        possibilities = string.ascii_letters + string.digits + string.punctuation
        self.val = ''.join(random.choice(possibilities) for _ in range(random.randint(0, 100)))

class Complex(BaseType):
    def generate(self):
        self.val = complex(Float().getVal(), Float().getVal())

class List(BaseType):
    def generate(self):
        self.val = []
        for _ in range(random.randint(0, 10)):
            self.val.append(generateRandomObject())

class Dict(BaseType):
    def generate(self):
        self.val = {}
        for _ in range(random.randint(0, 10)):
            self.val[generateRandomObject()] = generateRandomObject()

class Tuple(BaseType):
    def generate(self):
        self.val = tuple(List().getVal())

class Set(BaseType):
    def generate(self):
        self.val = set(List().getVal())

class FrozenSet(BaseType):
    def generate(self):
        self.val = frozenset(List().getVal())
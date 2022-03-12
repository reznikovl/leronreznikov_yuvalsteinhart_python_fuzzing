def simple_func(x):
    return x - 1

def simple_multi_param(a, x):
    x *= 2
    return a[x]

def four_params(a, b, c, d):
    x = a - b
    c.append(x)
    d.add(x)

def complex_1(a, b, c, d, e):
    e += a + b
    c.add(10)
    c = 1
    
    c *= 2
    d -= e
    return d

def complex_2(a, b, c, d, e, f, g):
    for i in a:
        b.add(i)
    if b == a:
        pass
    q = d - e
    a.append(f)
    x = complex(d, e)
    y = complex(c, g)

def complex_3(a, b, c):
    t = a * b
    complex_2(a, b, c, -10, 7, 'hi', t)

def summing(a):
    total = 0
    for i in a:
        total += i
    return total
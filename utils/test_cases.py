def simple_func(x):
    return x - 1

def simple_multi_param(a, x):
    return a[x]

def four_params(a, b, c, d):
    x = a - b
    c.append(x)
    d.add(x)

def complex_1(a, b, c, d, e):
    e += a + b
    c.add(10)
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
    complex_2(a, b, c, d, e, f, t)

# complex_2(['krYAu7UC7dN', 1940900255, 'LIqG^{dJ?U@l*eE1:qUcOk6b>4R:NXJZa\'d>;\nhOD|;W!8jLE`{%;c@=O.l7|n>^n50Ssi;J&^B1g', b'\x13\xff\xf0]2\x8d\x1cg\x9a\xb1\x18\xe0\xca%hE\xf6!\xe7N\xde+h\xc2i\xa4\xaa\xaa\xf6\xe1\xa3\xc1ii_3\x01\xaf\x8f\\\x1ei\xc0|\xef\x05\x80\xeb\xb9d\xf3\x96Bi\xd8\x97\x8e0\xe1{t\x82w\xb9\xedA'], [-831.1511943107936, True, '7BPpa=z4E3p2lFkVY."_89AF-hTB?]GEp(:%7v!MiL\#\'NktUC!Nkjg|sVoE, jWgP}U_c,xrtLC|\'PU<Kls[J9]$a[>R&+]^kh\'+%[Q;.2TqK*#df>i==hs{_hmrD*{g1tJ]'], False, 856794861, -538698766, -342.416357758386, 597.1847185488544)
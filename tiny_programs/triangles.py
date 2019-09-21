# -*- coding: utf-8 -*-

def triangles(max):
    yield [1]
    n = 1
    t = [1, 1]
    while n < max:
        yield t
        t = [1] + [t[i] + t[i + 1] for i in range(len(t) - 1)] + [1]
        n = n + 1
    return

row = int(input('Number: '))
for n in triangles(row):
    print(n)

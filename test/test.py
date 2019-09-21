def rp(a, b):
    r = True
    n = min(a, b)
    for i in range(2, n+1):
        if a % i == 0 and b % i == 0:
            r = False
            break
    return r

n = tuple(map(int, input('Numbers: ').split()))
mrp = False
for i in range(len(n)):
    for j in range(i+1, len(n)):
        if rp(n[i], n[j]):
            mrp = True
            break
    if mrp == True:
        break
prp = True
for i in range(len(n)):
    for j in range(i+1, len(n)):
        if not rp(n[i], n[j]):
            prp = False
            break
    if prp == False:
        break
if prp:
    print('prp')
elif mrp:
    print('mrp')
else:
    print('~')

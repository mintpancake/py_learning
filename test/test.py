list = [1, 2, 3]
s = set([])
for i in range(len(list)):
    for j in range(len(list)):
        if i != j:
            s.add(list[i]+list[j])
print(s)
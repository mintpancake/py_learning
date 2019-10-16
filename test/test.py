def show(l,size):
    for i in range(size):
        for j in range(size):
            print(f'{l[size*i+j]:>2}',end='')
            if j==size-1:
                print()
            else:
                print(' ',end='')

def judge(l,size):
    for i in range(size):
        if len(set(l[i*size:(i+1)*size]))==1:
            print('Winner:',l[i*size])
            return True
        elif len(set(l[i::size]))==1:
            print('Winner:',l[i])
            return True
    if len(set(l[0::size+1]))==1:
        print('Winner:',l[0])
        return True
    elif len(set(l[size-1:size**2-2:size-1]))==1:
        print('Winner:',l[size-1])
        return True
    return False

size=int(input('Size--> '))
l=[]
for i in range(size):
    for j in range(size):
        l.append(size*i+j)
show(l,size)
for n in range(size**2):
    if n%2==0:
        x=int(input('X--> '))
        l[x]='X'
    else:
        o=int(input('O--> '))
        l[o]='O'
    show(l,size)
    if judge(l,size):
        exit()
print('Winner: None')
danger_map=[]
safety_map=[]

def init_map():
    init_line=list(input())
    danger_map.append(init_line)
    n=len(init_line)
    for _ in range(n-1):
        danger_map.append(list(input()))
    for i in range(n):
        safety_map.append([])
        for _ in range(n):
            safety_map[i].append('0')
    for i,v in enumerate(danger_map):
        for j,w in enumerate(v):
            if w=='1':
                safety_map[i][j]='#'
    return

def judge(pos,level):
    i,j=pos
    n=len(safety_map)
    if level==1:
        for p in range(i-1,i+2):
            for q in range(j-1,j+2):
                if not (p>=0 and p<=n-1 and q>=0 and q<=n-1):
                    continue
                else:
                    if danger_map[p][q]=='1':
                        return False
        return True

    elif level==2:
        for p in range(i-2,i+3):
            for q in range(j-2,j+3):
                if not (p>=0 and p<=n-1 and q>=0 and q<=n-1):
                    continue
                else:
                    if danger_map[p][q]=='1':
                        return False
        return True
    return False

def modify():
    safety_map_copy=safety_map
    for i,v in enumerate(safety_map_copy):
        for j,w in enumerate(v):
            if w=='#':
                continue
            else:
                if judge((i,j),1):
                    safety_map[i][j]='1'
                if judge((i,j),2):
                    safety_map[i][j]='2'
    return

def show():
    for i in safety_map:
        print(''.join(i))
    return

def main():
    init_map()
    modify()
    show()
    return

main()
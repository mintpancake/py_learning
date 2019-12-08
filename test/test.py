N,D=0,0
charging_stations=[]
my_location=(0,0)
target_location=(0,0)
paths={'M':[],'T':[]}

def init():
    global N,D,charging_stations,my_location,target_location,paths
    N,D=tuple(map(int,input().split()))
    for _ in range(N):
        charging_stations.append(tuple(map(int,input().split())))
    my_location=tuple(map(int,input().split()))
    target_location=tuple(map(int,input().split()))
    for i,v in enumerate(charging_stations):
        paths[i]=[]
    xM,yM=my_location
    xT,yT=target_location
    if (xT-xM)**2+(yT-yM)**2<=D**2:
        paths['M'].append('T')
        paths['T'].append('M')
    for i,v in enumerate(charging_stations):
        x,y=v
        if (x-xM)**2+(y-yM)**2<=D**2:
            paths['M'].append(i)
            paths[i].append('M')
        if (x-xT)**2+(y-yT)**2<=D**2:
            paths['T'].append(i)
            paths[i].append('T')
        for j,w in enumerate(charging_stations):
            if i==j:
                continue
            x2,y2=w
            if (x-x2)**2+(y-y2)**2<=D**2:
                paths[i].append(j)
    return

def find():
    q=[]
    visited={}
    visited['M']=False
    visited['T']=False
    for i,_ in enumerate(charging_stations):
        visited[i]=False
    current='M'
    visited[current]=True
    for i in paths[current]:
        if visited[i]==False and i not in q:
            q.append(i)
    while len(q)>0 and not visited['T']:
        current=q.pop(0)
        visited[current]=True
        for i in paths[current]:
            if visited[i]==False and i not in q:
                q.append(i)
    if visited['T']:
        return True
    else:
        return False
    return False

def main():
    init()
    if find():
        print('y')
    else:
        print('n')
    return

main()
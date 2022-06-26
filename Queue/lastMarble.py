x=int(input())
l = list(map(int,input().strip().split()))
 
while(True):
    l.sort()
    x=l.pop()
    y=l.pop()
    l.append(abs(x-y))
    if(len(l)==1 and l[0]==0):
        print(-1)
        break   
    if(len(l)==1):
        print(l[0])
        break
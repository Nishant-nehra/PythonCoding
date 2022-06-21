n=int(input())
arr=[]
for _ in range(n):
  row=list(map(int,input().split()))
  arr.append(row)
q=int(input())
for _ in range(q):
  bit,x,y,val=map(int,input().split())
  x-=1
  y-=1
  if bit==1:
    for row in range(x,y+1):
      for col in range(n):
        arr[row][col]^=val
  else:
    for row in range(n):
      for col in range(x,y+1):
        arr[row][col]^=val
for row in arr:
  print(*row,sep=' ')
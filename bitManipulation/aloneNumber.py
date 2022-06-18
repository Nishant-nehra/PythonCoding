for _ in range(int(input())):
  n=int(input())
  arr=list(map(int,input().split()))
  res=arr[0]
  for i in range(1,n):
    res=res^arr[i]
  print(res)

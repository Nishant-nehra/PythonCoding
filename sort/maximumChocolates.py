for _ in range(int(input())):
  n=int(input())
  arr=list(map(int,input().split()))
  ans=0
  arr.sort()
  for item in arr[-1::-2]:
    ans+=item
  print(ans)
l,r=map(int,input().split())
flag=True
for i in range(31):
  power2=(2**i)
  if power2 >l and power2<=r:
    print(0)
    flag=False
    break
if flag:
  ans=l
  for i in range(l+1,r+1):
        ans=ans&i
  print(ans)

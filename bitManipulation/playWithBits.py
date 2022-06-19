import math
l,r = map(int,input().split())
count = 0
n = int(math.log(10**18,2))+1
for i in range(n+1):
  x = 2**i -1
  for j in range(i+1,n+1):
    x = x | (1<<j)
    if(l <= x <= r):
      count += 1
print(count)
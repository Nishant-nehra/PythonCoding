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


#to understand this n=5 and print at line 6 and 8
#1 for line 6(print x and i) and 2 for print on line 8
#we have taken x=2**i-1 ie 0,1,3,7 which are 0,1,11,111
#now we will add a zero at LHS of them till n=60(which is 10^18)
#this is done using or operation with right shift 1
#now if no in range then count++
# 1: 0b0 0
# 2: 0b10
# 2: 0b110
# 2: 0b1110
# 2: 0b11110
# 1: 0b1 1
# 2: 0b101
# 2: 0b1101
# 2: 0b11101
# 1: 0b11 3
# 2: 0b1011
# 2: 0b11011
# 1: 0b111 7
# 2: 0b10111
# 1: 0b1111 15
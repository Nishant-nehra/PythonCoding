n=int(input())
#count No of 1s in binary representation of n
#n&(n-1) unsets last set bit ie it unsets a 1
count=0
while(n):
  n=n&(n-1)
  count+=1
print(count)
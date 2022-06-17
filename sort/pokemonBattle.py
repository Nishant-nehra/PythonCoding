for _ in range(int(input())):
  n=int(input())
  arr1=list(map(int,input().split()))
  arr2=list(map(int,input().split()))
  arr1.sort()
  arr2.sort()
  count=0
  i=0
  j=0
  while i<n and j<n:
    if arr1[i]>arr2[j]:
      i+=1
      j+=1
      count+=1
    else:
      i+=1
  print(count)
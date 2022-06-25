def waterStored(arr,n):
  water=0
  left=[-1]*n
  left[0]=arr[0]
  for i in range(1,n):
    left[i]=max(arr[i],left[i-1])
  right=[-1]*n
  right[-1]=arr[-1]
  for i in range(n-2,-1,-1):
    right[i]=max(arr[i],right[i+1])

  for i in range(n):
    water+=min(left[i],right[i])-arr[i]
  return water


n=int(input())
arr1=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))
rahul=waterStored(arr1,n)
amit=waterStored(arr2,m)
if rahul>amit:
  print("Rahul {}".format(rahul-amit))
elif rahul<amit:
  print("Amit {}".format(amit-rahul))
else:
  print(-1)
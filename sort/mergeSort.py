from sys import setrecursionlimit
setrecursionlimit(110000)

def merge(arr,left,right,mid):
  leftList=arr[left:mid+1]
  rightList=arr[mid+1:right+1]
  i=0
  j=0
  k=left
  while i<len(leftList) and j<len(rightList):
    if leftList[i]<=rightList[j]:
      arr[k]=leftList[i]
      k+=1
      i+=1
    else:
      arr[k]=rightList[j]
      k+=1
      j+=1
  
  while i<len(leftList):
    arr[k]=leftList[i]
    k+=1
    i+=1
  while j<len(rightList):
    arr[k]=rightList[j]
    k+=1
    j+=1
  
def mergeSort(arr,left,right):
  if left<right:
    mid=left+(right-left)//2
    mergeSort(arr,left,mid)
    mergeSort(arr,mid+1,right)
    merge(arr,left,right,mid)

for _ in range(int(input())):
  n=int(input())
  arr=list(map(int,input().split()))
  mergeSort(arr,0,n-1)
  print(*arr,sep=' ')

def sortCheck(arr, start, end):
    
    if(start + 1 == end):
        return 1
    
    mid = (start + end) // 2
    h1 = sortCheck(arr, start, mid)
    h2 = sortCheck(arr, mid, end)
    
    if(h1 == h2 and h1 == (end - start) // 2 and arr[mid - 1] <= arr[mid]):
        return end-start
    
    return max(h1, h2)

for _ in range(int(input())):
  n=int(input())
  arr=list(map(int,input().split()))
  print(sortCheck(arr,0,n))
  
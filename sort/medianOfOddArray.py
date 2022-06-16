n=int(input())
arr=list(map(int,input().split()))
mid=(n+1)//2
arr.sort()
print(arr[mid-1])
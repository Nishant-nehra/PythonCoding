for _ in range(int(input())):
  n=int(input())
  arr=[]
  for _ in range(n):
    c,p,d=input().split()
    arr.append((c,p,d))
    arr.sort(key=lambda x:(x[2],x[1]),reverse=True)
  for i in range(n):
    print(arr[i][0])
import collections
n=int(input())
arr=list(map(int,input().split()))
que=collections.deque()
for i in arr:
  que.append(i)
  print(*que)
for i in range(n-1):
  que.popleft()
  print(*que)
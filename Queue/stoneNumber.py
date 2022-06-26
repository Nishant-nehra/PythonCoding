import collections
for _ in range(int(input())):
  n=int(input())
  deque=collections.deque()
  for i in range(1,n+1):
    deque.append(i)
  flagMoveToEnd=1
  while len(deque)!=1:
    if flagMoveToEnd==1:
      item=deque[0]
      deque.popleft()
      deque.append(item)
      flagMoveToEnd=0
    else:
      flagMoveToEnd=1
      deque.popleft()
  print(deque[0])
      
import collections
for _ in range(int(input())):
  deque=collections.deque()
  n=int(input())
  deque.append('1')
  while n!=0:
    n-=1
    deque.append(deque[0]+'0')
    deque.append(deque[0]+'1')
    print(deque[0],end=' ')
    deque.popleft()
  print()
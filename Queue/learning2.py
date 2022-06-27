from collections import deque
deq=deque()
while True:
  n=int(input())
  if n==-3:
    break
  elif n==-2:
    print(deq[-1][1])
  elif n==-1:
    deq.pop()
  else:
    if len(deq)==0:
      deq.append((n,n))
    else:
      deq.append((n,max(deq[-1][1],n)))
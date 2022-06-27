import collections
deque=collections.deque()

string=input()
n=len(string)
i=0
while i<n:
  if string[i]=='p':
    if i+1!=n and string[i+1]=='p':
      i+=2
      if len(deque)==0:
        print('OOPS')
      else:
        deque.pop()
    else:
      i+=1
      if len(deque)==0:
        print('OOPS')
      else:
        print(deque[-1])
  else:
    deque.append(string[i])
    i+=1
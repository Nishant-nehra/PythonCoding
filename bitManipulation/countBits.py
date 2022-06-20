for _ in range(int(input())):
  n=int(input())
  count=0
  for i in range(n+1):
    count+=bin(i).count('1')
  print(count)
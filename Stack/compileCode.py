def longestPrefixErrorFree(string):
  arr=[]
  longest=0
  curr=0
  for i in string:
    if i=='<':
      arr.append(i)
    if i=='>':
      if len(arr)==0:
        return longest
      elif arr[-1]=='<':
        arr.pop()
        curr+=2
        if len(arr)==0:
          longest=curr
  return longest

for _ in range(int(input())):
  n=int(input())
  string=input()
  print(longestPrefixErrorFree(string))
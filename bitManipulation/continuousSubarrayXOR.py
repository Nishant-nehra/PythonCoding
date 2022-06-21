for _ in range(int(input())):
  n=int(input())
  arr=list(map(int,input().split()))
  # subArr=[]
  # xorOfSubArr=[]
  # for i in range(n):
  #   for j in range(i+1,n+1):
  #     subArr.append(arr[i:j])
  # for i in range(len(subArr)):
  #   xor=subArr[i][0]
  #   for j in range(1,len(subArr[i])):
  #     xor=xor^subArr[i][j]
  #   xorOfSubArr.append(xor)
  # ans=xorOfSubArr[0]
  # for i in range(1,len(xorOfSubArr)):
  #   ans=ans^xorOfSubArr[i]
  # print(ans)
  ans=0
  for i in range(n):
    #we are checking which elements will occur odd times in subarr
    #xor of even occurence of element is 0
    #freq=(i+1)*(n-i) returns no. of times el will come in all subarrays
    freq=(i+1)*(n-i)
    if freq%2!=0:
      ans=ans^arr[i]
    
  print(ans)
for _ in range(int(input())):
  n=int(input())
  consecutive1=0
  flipped=False
  binary=bin(n)[2:]
  length=len(binary)
  for i in range(len(binary)):
      for j in range(i+1,(len(binary))):
          arr=binary[i:j+1]
          zeros=arr.count('0')
          currFlipped=False
          if zeros>1:
              break
          if zeros==1:
            currFlipped=True
          if len(arr)>consecutive1:
              consecutive1=len(arr)
              flipped=currFlipped
  if flipped==False:
    print(consecutive1+1)
  else:
    print(consecutive1)
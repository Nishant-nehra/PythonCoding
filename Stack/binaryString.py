for _ in range(int(input())):
  arr=list(input())
  count=0
  length=len(arr)
  if length%2==0:
    ones=0
    zero=0
    for item in arr:
      if item=='1':
        ones+=1
      else:
        if ones>zero:
          zero+=1
        else:
          count+=1
          ones+=1
    
    if ones==zero:
      print(count)
    else:
      print(count+(ones-zero)//2)
  else:
    print(-1)
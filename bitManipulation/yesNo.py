def power(arr,n,powerArr,tempArr,currIndex):
  if len(tempArr)==n:
    powerArr.append(sum(tempArr))
    return
  else:
    tempArrCopy=tempArr.copy()
    tempArrCopy.append(arr[currIndex])
    power(arr,n,powerArr,tempArrCopy,currIndex+1)
    tempArrCopy2=tempArr.copy()
    tempArrCopy2.append(-arr[currIndex])
    power(arr,n,powerArr,tempArrCopy2,currIndex+1)


n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
flag = 0
powerArr=[]
tempArr=[]
power(arr,n,powerArr,tempArr,0)
for i in powerArr:
  if i>=0 and i%360==0:
    print('YES')
    flag=1
    break
if flag != 1:
    print("NO")
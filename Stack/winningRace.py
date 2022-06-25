n=int(input())
arr=list(map(int,input().split()))
ansArr=[-1]*len(arr)
st=[]
st.append(arr[0])
for i in range(1,n):
  while len(st)!=0:
    if arr[i]>st[-1]:
      ansArr[i]=st[-1]
      break
    st.pop()
  st.append(arr[i])
print(*ansArr,end=' ')
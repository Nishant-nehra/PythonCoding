inputsArr=[]
while True:
  arr = list(input())
  if '-' in arr:
    break
  inputsArr.append(arr)

for i in range(len(inputsArr)):
    arr = inputsArr[i]
    st = []
    ans = 0
    for item in arr:
      if item=='{':
        st.append(item)
      else:
        if len(st)==0:
          st.append(item)
        elif st[-1]=='{':
          st.pop()
        else:
          st.append(item)
    left=st.count('{')
    right=st.count('}')
    if left%2==0:
      ans+=left//2
      left=0
    else:
      ans+=left//2
      left=1
    if right%2==0:
      ans+=right//2
      right=0
    else:
      ans+=right//2
      right=1
    if left==right:
      ans+=left+right
    print('{}. {}'.format(i+1,ans))

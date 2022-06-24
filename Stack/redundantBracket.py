st=[]
string=input()
operators=['+','-','*','/']
flag=0
for item in string:
  if item in operators:
    st.append(item)
  elif item=='(':
    st.append(item)
  elif item==')':
    if st[-1] in operators:
      st.pop()
      st.pop()
    elif st[-1]=='(':
      flag=1
      break

print(flag)
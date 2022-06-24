class Stack:
  def __init__(self):
    self.arr=[]

  def push(self,data):
    if self.isEmpty():
      self.arr.append((data,data))
    else:
      if data<self.arr[-1][1]:
        self.arr.append((data,data))
      else:
        self.arr.append((data,self.arr[-1][1]))
      
  def isEmpty(self):
    if len(self.arr)==0:
      return 1
    return 0
  
  def pop(self):
    if self.isEmpty()==1:
      print(-1)
    else:
      self.arr.pop()
  
  def top(self):
    if self.isEmpty()==1:
      return -1
    else:
      return self.arr[-1][0]
  
  def getMin(self):
    if self.isEmpty()==1:
      return -1
    else:
      return self.arr[-1][1]
    
st=Stack()
for _ in range(int(input())):
  lst=list(map(int,input().split()))
  if len(lst)==1:
    if lst[0]==2:
      st.pop()
    elif lst[0]==3:
      print(st.top())
    elif lst[0]==4:
      print(st.getMin())
  else:
    st.push(lst[1])
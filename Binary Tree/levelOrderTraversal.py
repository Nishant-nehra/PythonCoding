"""
Complete the levelOrderTraversal function below
For your reference

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

Methods implemented are:
buildTreeLevelWise(ip) # ip denotes input given by the users
"""
import collections
def levelOrderTraversal(root):
  deque=collections.deque()
  deque.append(root)
  while len(deque)!=0:
    temp=deque[0]
    if temp.left is not None:
      deque.append(temp.left)
    if temp.right is not None:
      deque.append(temp.right)
    print(temp.data,end=' ')
    deque.popleft()
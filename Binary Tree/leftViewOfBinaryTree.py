"""
Complete the leftView function below
For your reference
from queue import Queue
class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

Methods implemented are:
buildTreeLevelWise(ip) # ip denotes input given by the users
"""
import collections
def leftView(root):
  if root is None:
    return
  deque=collections.deque()
  currLevelPrinted=0
  deque.append((root,currLevelPrinted))
  while(len(deque)):
    currNode=deque[0][0]
    currNodeLevel=deque[0][1]
    if currLevelPrinted==currNodeLevel:
      currLevelPrinted+=1
      print(currNode.data,end=" ")
    
    deque.popleft()
    if currNode.left!=None:
      deque.append((currNode.left,currNodeLevel+1))
    if currNode.right!=None:
      deque.append((currNode.right,currNodeLevel+1))
      
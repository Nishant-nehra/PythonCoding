"""
Complete the checkSumTree function below
For your reference

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

Methods implemented are:
buildTreeLevelWise(ip) # ip denotes input given by the users
"""

def checkSumTree(root):
	if root is None:
	  return True
	if root.left is None and root.right is None:
	  return True
	left=checkSumTree(root.left)
	right=checkSumTree(root.right)
	if left and right:
	  if root.left and root.right:
	    if root.data==root.left.data+root.right.data:
	      root.data=root.data+root.left.data+root.right.data
	      return True
	  elif root.left:
	   if root.data==root.left.data:
	      root.data=root.data+root.left.data
	      return True
	   else:
	      return False
	  elif root.right:
	    if root.data==root.right.data:
	      root.data=root.data+root.right.data
	      return True
	  else:
	    return False
	
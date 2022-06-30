"""
Complete the convertSumTree function below
For your reference

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

Methods implemented are:
buildTreeLevelWise(ip) # ip denotes input given by the users
"""

def convertSumTree(root):
  if root is None:
    return 0
  lside=convertSumTree(root.left)
  rside=convertSumTree(root.right)
  data=root.data
  root.data=lside+rside
  return data+root.data

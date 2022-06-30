"""
Complete the checkMirrorTree function below
For your reference

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

Methods implemented are:
buildTreeLevelWise(ip) # ip denotes input given by the users
"""

def checkMirrorTree(root1,root2):
  if root1 is None and root2 is None:
    return True
  if root1.data!=root2.data:
    return False
  lside= checkMirrorTree(root1.left,root2.right)
  rside= checkMirrorTree(root1.right,root2.left)
  return root1.data==root2.data and lside and rside
  
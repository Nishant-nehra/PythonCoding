"""
Complete the findLowestAncestor function below
For your reference

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

Methods implemented are:
buildTreeLevelWise(ip) # ip denotes input given by the users
"""

def findLowestAncestor(root,v1,v2):
	if root is None:
	  return None
	#if we get a value in root then we stop going further
	if root.data==v1 or root.data==v2:
	  return root
	leftSide=findLowestAncestor(root.left,v1,v2)
	rightSide=findLowestAncestor(root.right,v1,v2)
	#if a root has received data on both left and right then it is LCA
	if leftSide and rightSide:
	  return root
	if leftSide is None and rightSide is None:
	  return None
	#if root has received data on only 1side then 2nd data is child of 1st data node
	#so LCA is first node
	return rightSide or leftSide

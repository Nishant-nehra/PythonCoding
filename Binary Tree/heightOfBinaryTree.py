"""
Complete the calculateHeight function below
For your reference

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

Methods implemented are:
buildTreeLevelWise(ip) # ip denotes input given by the users
"""

def calculateHeight(root):
    if root is None:
      return 0
    leftHeight=calculateHeight(root.left)
    rightHeight=calculateHeight(root.right)
    return max(leftHeight,rightHeight)+1
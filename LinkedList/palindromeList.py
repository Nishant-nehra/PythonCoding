"""
Complete the palindromeLlist() function below
For your reference
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head=None
		self.tail = None


 	def insertAtEnd(self,data): # returns head of the linked list
 	def printSinglyLinkedList(self):
"""


# Function Arguments: head (refers to the head of the linked list)
  
def palindromeLlist(head):
  arr=[]
  temp=head
  while temp is not None:
    arr.append(temp.data)
    temp=temp.next
  return arr[:]==arr[-1::-1]
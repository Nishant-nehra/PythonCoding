"""
Complete the insertSortedNode() function below
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


# Function Arguments: head (refers to the head of the linked list) and k (denoting the value to be inserted)
def insertSortedNode(head,k):
  newNode=Node(k)
  temp=head
  if(k<temp.data):
    newNode.next=head
    head=newNode
    return head
  while(temp.next is not None):
    if k>=temp.data and k<=temp.next.data:
      newNode.next=temp.next
      temp.next=newNode
      return head
    else:
      temp=temp.next
  if temp.next is None:
    temp.next=newNode
  return head
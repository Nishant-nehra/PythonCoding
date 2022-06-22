"""
Complete the lastElementFirst() function below
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
def lastElementFirst(head):
  last=head
  secondLast=None
  length=1
  while(last.next is not None):
    secondLast=last
    last=last.next
    length+=1
  if length==1:
    return head
  secondLast.next=None
  last.next=head
  head=last
  return head
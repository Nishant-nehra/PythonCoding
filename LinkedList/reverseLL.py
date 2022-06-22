"""
Complete the reverseLinkedList() function below
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
def reverseLinkedList(head):
  curr=head
  prev=None
  if curr.next is None:
    return head
  while curr.next is not None:
    next=curr.next
    curr.next=prev
    prev=curr
    curr=next
  curr.next=prev
  head=curr
  return head
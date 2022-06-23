"""
Complete the addOneToList() function below
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
def addOneToList(head):
  temp=head
  string=''
  string+=str(temp.data)
  while temp.next is not None:
    temp=temp.next
    string+=str(temp.data)
  if temp.data!=9:
    temp.data+=1
    return head
  else:
    len1=len(string)
    string2=str((eval(string+'+1')))
    len2=len(string2)
    temp2=head
    i=0
    temp2.data=string2[i]
    i+=1
    while temp2.next is not None:
      temp2=temp2.next
      temp2.data=string2[i]
      i+=1
    if i<len2:
      newNode=Node(0)
      temp.next=newNode
  return head
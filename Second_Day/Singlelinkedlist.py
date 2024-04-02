class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
head = Node(3)
second = Node(45)
third = Node(34)
fourth = Node(67)
head.next = second
second.next= third
third.next = fourth
def display(head):
        
        while head!=None:
            print(head.data)
            head=head.next
def insert_atb(data,head):
     newNode = Node(data)
     newNode.next = head
     head = newNode
     return head

def insert_at_e(data,head):
    newNode =Node(data)
    temp = head
    while temp.next!=None:
        temp = temp.next
    temp.next = newNode
    return head
    
display(head)
head = insert_atb(65,head)
head = insert_atb(21,head)
print(head)
display(head)
head = insert_at_e(65,head)
head = insert_at_e(21,head)
print(head)
display(head)







# write a function which takes two arguments data and next nodes and display the apended nodes in the front

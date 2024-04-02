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
        count = 0
        while head!=None:
            print(head.data)
            head=head.next
            count +=1
        print(f"Linked list consist of {count} elements")
def insert_atb(data,head): # a function which takes two arguments data and next nodes and display the apended nodes in the front
     newNode = Node(data)
     newNode.next = head
     head = newNode
     return head

def insert_at_e(data,head): # a function which takes two arguments data and next nodes and display the apended nodes in the back
    newNode =Node(data)
    temp = head
    while temp.next!=None:
        temp = temp.next
    temp.next = newNode
    return head
def mid(head):  #to find a middle value
    l =  8
    middle = l//2
    c1 = 0
    temp =head
    while temp!=None and c1<middle:
        c1 = c1+1
        temp = temp.next
    ans =temp.data
    print("The middle element is",ans)
def delete(target,head):
     temp = head
     while temp!=None:
        if temp.next.data == target:
            temp.next = temp.next.next.data

        
               
    
head = insert_atb(65,head)
head = insert_atb(21,head)
head = insert_at_e(56,head)
head = insert_at_e(77,head)
display(head)
mid(head)

class Node:
    def __init__(self,data) :
        self.data=data
        self.next=None
def insert_at_begg(head,data):
    New_node=Node(data)
    New_node.next=head
    head=New_node
    return head
    
def display(head):
    temp=head
    while temp!=None:
        print(temp.data)
        temp=temp.next
        
def cou(head):
    temp=head
    count=0
    while temp!=None:
        count=count+1
        temp=temp.next
    print("count")
    print(count)
    mid=count//2
    return mid
    
def midval(head,mid):
    
    temp=head
    cou2=0
    while temp!=None:
        cou2+=1
        if cou2==mid+1:
            data1=temp.data
            print(temp.data)
            break
        temp=temp.next
    
    return data1

        
def insert_at_last(head,data):
    temp=head
    newnode=Node(data)
    while temp.next!=None:
        temp=temp.next
    temp.next=newnode
 
'''def remove(head,data):
    temp=head
    while temp!=None:
        if temp.data==data:
            temp.data=None
            temp_prev.next=temp.next
            temp.next=None
            break
        temp_prev=temp
        temp=temp.next'''

    
def remove(head,data):
    temp=head
    while temp.next!=None:
        if temp.next.data==data:
            
            temp.next=temp.next.next
        temp=temp.next
        
def removemid(head,data1):
        
        
    temp=head
    while temp.next!=None:
        if temp.next.data==data1:
            
            temp.next=temp.next.next
        temp=temp.next

        
"""def removemid(head):
    
    temp=head
    count=0
    while temp!=None:
        count=count+1
        temp=temp.next
    print("count")
    print(count)
    mid=count//2
    
        
    temp=head
    cou2=0
    while temp!=None:
        cou2+=1
        if cou2==mid+1:
            data1=temp.data
            print(temp.data)
            break
        temp=temp.next
        
        
    temp=head
    while temp.next!=None:
        if temp.next.data==data1:
            
            temp.next=temp.next.next
        temp=temp.next
        
 function call is removemid(head)"""
    
    
def reverse(head):
    curr=head
    prev=None
    while curr!=None:
        
        nex=curr.next
        
        curr.next=prev
        prev=curr
        curr=nex
        
    return prev

'''def reversespot(head,f,e):
    curr=head
    pre=None
    
    while curr!=None:
        
        nex=curr.next
        
        curr.next=prev
        prev=curr
        curr=nex
        
    return prev'''

              
            
        
    
        
    
        


head=Node(3)
second=Node(23)
third=Node(43)
forth=Node(58)
head.next=second #linkning one and two
second.next=third #linking two and three
third.next=forth
display(head)
print("----")

head=insert_at_begg(head,63)
print("After adding at begining")
display(head)
print("----")

mid=cou(head)
print("----")

print("mid val")

midval(head,mid)
print("----")
insert_at_last(head,55)
display(head)
print("----")

remove(head,43)
print("After removing")
display(head)
print("----")
print("mid")
data1=midval(head,mid)
print("----")

removemid(head,data1)
print("After removing mid")
display(head)

print("After reversing")
head=reverse(head)
display(head)


def merge(l1,l2):
    head1 = Node(-1)
    curr = head1
    while l1!= None and 12!=None:
        if l1.data<=l2.data:
            curr.next = l1.data
            l1 = l1.next
        else:
            curr.next = l2.data
            l2 = l2.next
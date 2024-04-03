class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
head = Node(1)
second = Node(2)
third = Node(3)    # [2,1,2,2,0,1,2,0,0,1,1]
fourth = Node(4)



head.prev = None
head.next = second
second.prev= head
second.next= third
third.prev = second
third.next = fourth
fourth.prev = third
fourth.next= None

temp = head
while(temp!=None):
    print(temp.data,end=" ->")
    temp = temp.next
print('null')


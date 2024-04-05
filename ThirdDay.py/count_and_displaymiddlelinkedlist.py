

# [2,1,2,2,0,1,2,0,0,1,1]

# output = [00011112222]
lst = [2,1,2,2,0,1,2,0,0,1,1]
lst1 = []
for i in range(len(lst)):
    if lst[i]==0:
         lst1.append(lst[i])
for i in range(len(lst)):
        
        if lst[i]==1:
            lst1.append(lst[i])
for i in range(len(lst)):
        
        if lst[i]==2:
            lst1.append(lst[i])
print(lst1)

lst2 = [2,1,2,2,0,1,2,0,0,1,1]
count_0 = 0
count_1 = 0
count_2 = 0
for i in lst:
    if i==0:
        count_0 += 1
    elif i==1:
        count_1 += 1
    else:
        count_2 += 1
indexval =0
while count_0!=0:
    lst2[indexval] = 0
    indexval +=1
    count_0 -=1
while count_1!=0:
    lst2[indexval] = 1
    indexval +=1
    count_1 -=1
while count_2!=0:
    lst2[indexval] = 2
    indexval +=1
    count_2 -=1
print(lst2)


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
head = Node(2)
second = Node(1)
third = Node(2)    # [2,1,2,2,0,1,2,0,0,1,1]
fourth = Node(2)
fifth = Node(0)
sixth = Node(1)
seventh = Node(2)
eigth = Node(0)
ninth= Node(0)
tenth = Node(1)
Eleventh = Node(1)

head.prev = None
head.next = second

second.prev= head
second.next= third
third.next = fourth

fourth.next= fifth
fifth.next = sixth
sixth.next = seventh
seventh.next = eigth
eigth.next = ninth
ninth.next= tenth
tenth.next = Eleventh

for i in range(len(lst)):
    if lst[i]==0:
         lst1.append(lst[i])
for i in range(len(lst)):
        
        if lst[i]==1:
            lst1.append(lst[i])
for i in range(len(lst)):
        
        if lst[i]==2:
            lst1.append(lst[i])
print(lst1)


def display(head):
        count = 0
        while head!=None:
            print(head.data)
            head=head.next
            count +=1

display(head)
while temp!=0:
     
     
     
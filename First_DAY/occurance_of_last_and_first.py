# using binary search find the first and last occurance of 4 and 15
l=[1,4,4,4,9,13,15,15] 
t=4
def first_occurrence(l,t):
    s=0
    e=len(l)-1
    result=-1
    while s<=e:
        mid=(s+e)//2
        if l[mid]==t:
            result=mid
            e=mid-1
        elif t<l[mid]:
            s=mid+1
        elif t>l[mid]:
            e=mid-1
    return result

def last_occurrence(l,t):
    s=0
    e=len(l)-1
    result=-1
    while s<=e:
        mid=(s+e)//2
        if l[mid]==t:
            result=mid
            s=mid+1
        elif t>l[mid]:
            s=mid+1
        elif t<l[mid]:
            e=mid-1
    return result
first = first_occurrence(l, 4)
last = last_occurrence(l, 4)
first15 = first_occurrence(l, 15)
last15 = last_occurrence(l, 15)
print("First occurrence of 4 is ", first)
print("Last occurrence of 4 is ", last)
print("First occurrence of 15 is ", first15)
print("Last occurrence of 15 is ", last15)
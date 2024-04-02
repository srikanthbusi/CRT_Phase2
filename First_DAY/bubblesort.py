# def bublesort(list1):
#     for i in range(len(list1)-1):
#         for j in range(len(list1)-i-1):
#             if list1[j]>list1[j+1]:
#                 list1[j],list1[j+1] = list1[j+1],list1[j]    
#     return(list1)
# clist = [4,34,23,1,4,34,23,133,44]
# print(bublesort(clist))
"""Time complexity = o(n^2)
Space Complexity = o(1)
Three typs of codes have been done"""

l = [12, 34, 56, 11, 64, 123, 233, 13]

for i in range(len(l)):
    for j in range(0, len(l)-i-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]

print("Sorted list is:", l)


# def sort(lst):
    
#     for i in range(len(lst)-1,0,-1):
#         for j in range(i):
#             if lst[j] > lst[j+1]:
#                 temp = lst[j]
#                 lst[j] = lst[j+1]
#                 lst[j+1] = temp
#     return lst

# lst =[2,34,45,233,45,22,12,34]
# print(sort(lst))

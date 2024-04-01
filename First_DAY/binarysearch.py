# l = [44,45,47,452,785,5566,55565]
# s =0
# e =len(l)-1
# mid = s + (e-s)//2
# t = int(input("dgj"))
# var=0
# while s<=e:
    
#     if l[mid]==t:
#         # print(mid)
#         var = mid
#         break
#     elif t<l[mid]:
#         e = mid-1
#     elif t>l[mid]+1:
#         s =mid+1
#     mid = s+(e-s)//2
# print(var)

# using binary search find the first and last occurance of 4 and 15
# l=[1,4,4,4,9,13,15,15] 
# t=4
# def first_occurrence(l,t):
#     s=0
#     e=len(l)-1
#     result=-1
#     while s<=e:
#         mid=(s+e)//2
#         if l[mid]==t:
#             result=mid
#             e=mid-1
#         elif t<l[mid]:
#             s=mid+1
#         elif t>l[mid]:
#             e=mid-1
#     return result

# def last_occurrence(l,t):
#     s=0
#     e=len(l)-1
#     result=-1
#     while s<=e:
#         mid=(s+e)//2
#         if l[mid]==t:
#             result=mid
#             s=mid+1
#         elif t>l[mid]:
#             s=mid+1
#         elif t<l[mid]:
#             e=mid-1
#     return result
# first = first_occurrence(l, 4)
# last = last_occurrence(l, 4)
# first15 = first_occurrence(l, 15)
# last15 = last_occurrence(l, 15)
# print("First occurrence of 4 is ", first)
# print("Last occurrence of 4 is ", last)
# print("First occurrence of 15 is ", first15)
# print("Last occurrence of 15 is ", last15)
# # [1,3,6,7,9,5,2]
# apply binary search on this list and find the peak element

# arr.sort()
# print(arr)
# target = max(arr)
def peakindex():
    s =0
    e =len(arr)-1
    mid = s+(e-s)//2
    while(s<=e):
        if arr[mid] >arr[mid-1] and arr[mid] >arr[mid+1]:
            return mid
        elif arr[mid-1] >arr[mid]:
            e = mid
        elif arr[mid] < arr[mid +1]:
            s = mid
        mid = s+ (e-s)//2

arr = [1,3,6,7,9,5,2]
print(peakindex())

# agressive cows
# there are multiple cows and multiple stalls for them you have
# to place them where the minimum distance should  be maximum
# birds the minimum distance shold  be minimum


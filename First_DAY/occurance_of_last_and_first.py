# # using binary search find the first and last occurance of 4 and 15
# def first_occurrence(lst, t):
#     s = 0
#     e = len(lst) - 1
#     result = -1
#     while s <= e:
#         mid = (s + e) // 2
#         if lst[mid] == t:
#             result = mid
#             e = mid - 1
#         elif t < lst[mid]:
#             e = mid - 1 
#         elif t > lst[mid]:
#             s = mid + 1
#     return result

# def last_occurrence(l,t):
#     s=0
#     e=len(l)-1
#     result=-1
#     while s<=e:
#         mid=(s+e)//2
#         if lst[mid]==t:
#             result=mid
#             s=mid+1
#         elif t>lst[mid]:
#             s=mid+1
#         elif t<lst[mid]:
#             e=mid-1
#     return result
# lst=[1,4,4,4,9,13,15,15] 
# first = first_occurrence(lst, 4)
# last = last_occurrence(lst, 4)
# first15 = first_occurrence(lst, 15)
# last15 = last_occurrence(lst, 15)
# print(f"First occurrence of 4 is:{first} and Last occurrence of 4 is:", last)
# print()
# print(f"First occurrence of 15 is:{first15} and Last occurrence of 15 is:", last15)

def fstocurance(l, tar):
    start = 0
    end = len(l) - 1
    result = -1
    while start <= end:
        midvalue = start + (end - start) // 2
        if tar == l[midvalue]:
            result = midvalue
            end = midvalue - 1
        elif tar < l[midvalue]:
            end = midvalue - 1
        elif tar > l[midvalue]:
            start = midvalue + 1
    return result

def lstocurance(l, tar):
    start = 0
    end = len(l) - 1
    result = -1
    while start <= end:
        midvalue = start + (end - start) // 2
        if tar == l[midvalue]:
            result = midvalue
            start = midvalue + 1
        elif tar < l[midvalue]:
            end = midvalue - 1
        elif tar > l[midvalue]:
            start = midvalue + 1
    return result

l = [20, 30, 40, 40, 40, 50, 60, 70]
print(fstocurance(l, 40))  # Should print the index of the first occurrence of 40
print(lstocurance(l, 40))  # Should print the index of the last occurrence of 40

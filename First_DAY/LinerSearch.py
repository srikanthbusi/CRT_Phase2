lst =[]
n = int(input("Enter the number of elements(Ascending order) to be considered for a list:"))
for i in range(0,n):
   ele = int(input())
   lst.append(ele)
print("Your list is:",lst)
t = int(input("Enter your taget number to show it's index:"))
for i in range(len(lst)):
    if t == lst[i]:
      print("The element found at",i)
      break


# l=[10,45,85,69,535,455]
# # creating an empty list
# lst = []
# # number of elements as input
# n = int(input("Enter number of elements : "))
# # iterating till the range
# for i in range(0, n):
# 	elements = int(input())
# 	# adding the element
# 	lst.append(elements) 
# print(lst)
    
# n = int(input("Enter number of elements : "))
# # Below line read inputs from user using map() function
# a = list(map(int, 
# 	input("\nEnter the numbers : ").strip().split()))[:n]

# print("\nList is - ", a)

# print(s)
# for i in range(len(s)-1):
#     if s[i] < s[i+1]:
#         s[i] = s[i+1]
#     else:
#         s[i] = -1
# s[-1] =-1
# print(s)
arr = [2,14,15,1,4,12]
s =[]
def nsg(arr):
    n = len(arr)
    ans =[-1]*n
    stack =[-1]
    for i in range(n-1,-1,-1):
        curr = arr[i]
        while top()!=-1 and stack.top()<=curr:
            stack.pop()
        ans[i] =stack.top()
        stack.append(curr)
    return ans


def top():
    return s[-1]


print(nsg(arr))
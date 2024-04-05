s=[]
s.append(2)
s.append(1)
s.append(3)
s.append(4)
s.append(8)
s1=[]

def push(data):
    s.append(data)

def display():
    while s>0:

        print(peek(s))
        s1.append(peek(s))
        print(s.pop())
# def reverse():
#     while s1>0:
#         print(peek(s1))
#         print(s1.pop())

# print("reverse")
# reverse()

def peek(s):
    print("The last element is:",s[-1])

def pop():
    print("The elements after poping last element",s.pop())

def isempty(s):
    if len(s) ==0:
        return True
    else:
        return False
    return len(s) == 0

def check(ch):
    s = []
    for i in range(len(ch)):
        if ch[i] in "{([":
            push(s,ch[i])
        elif (ch[i]  ==  ")" and peek(s) == "(") or (ch[i] == "]" and peek(s) == "[") or (ch[i]=="}" and ch[i]=="{"):
            s.pop()
        else:
            break
    if isempty(s) == True:
        print("valid")
    else:
        print("Invalid")


a = check(s)
print(a)

s=[]
s.append(2)
s.append(1)
s.append(3)
s.append(4)
s.append(8)

def push(data):
    s.append(data)

def display():
    while not isempty(s):
        print(s.pop())
display()

def peek(s):
    print("The last element is:",s[-1])

def pop():
    print("The elements after poping last element",s.pop())

def isempty(s):
    if len(s) ==0:
        return True
    else:
        return False
    return len(s) == 0

def reverse(s):
    temp = []
    while len(s) > 0:
        temp.append(s.pop())
    return temp

arr = [2,14,15,1,4,12]
s =[]
def nsg(arr):
    n = len(arr)
    ans =[-1]*n
    stack =[-1]
    for i in range(n-1,-1,-1):
        curr = arr[i]
        while peek()!=-1 and stack.peek()<=curr:
            stack.pop()
        ans[i] =stack.peek()
        stack.append(curr)
    return ans



print(nsg(arr))



push(10)
push(11)
push(15)
peek(s)
pop()
print(s)
print(isempty(s))
s = reverse(s)
print(s)


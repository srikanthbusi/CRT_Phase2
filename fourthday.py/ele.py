def push(s,data):
    s.append(data)

stack2=[]
push(stack2,21)
push(stack2,66)
push(stack2,0)
push(stack2,-1)
push(stack2,44)
push(stack2,2)
print(stack2)
def top(s):
    return s[-1]

def next_greater(s):
    s1=[]
    push(s1,-1)
    while len(s)!=1:
        push(s1,top(s))
        s.pop()
        if top(s)<top(s1):
            pass
        if top(s)>top(s1):
            s1.pop()
            push(s1,-1)
    s2=[]
    while len(s1)!=0:
        push(s2,top(s1))
        s1.pop()
    print(s2)
next_greater(stack2)

from collections import deque
dq = deque()
dq.append(1)
dq.append(2)
dq.append(3)
dq.append(4)
dq.append(5)
dq.append(6)
s = []
print(dq)
dq1 = deque()
for i in range(s):
    ele = dq.popleft()
    s.append
print(s)
while(len(s)!=0):
    dq.append(s.pop())

for i in range(len(dq)-s):
    dq.append(dq.popleft())
print(dq)


# [1,2,3,4,5,6]

# [3,2,1,4,5,6]
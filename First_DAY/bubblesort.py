l = [12, 34, 56, 11, 64, 123, 233, 13]

for i in range(len(l)):
    for j in range(0, len(l)-i-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]

print("Sorted list is:", l)

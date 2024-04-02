a = [12,45,799,34,66,454,3444,2344,454,23]
for i in range(1,len(a)):
        key =a[i]
        j =i - 1
        while j>=0 and a[j]>key:
             a[j+1] = a[j]
             j-=1
             a[j+1] = key
print(a)

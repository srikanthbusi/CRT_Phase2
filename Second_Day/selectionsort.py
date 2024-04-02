a = [12, 45, 799, 34, 66, 454, 3444, 2344, 454, 23]

# Selection Sort Algorithm
for i in range(len(a)):
    min_idx = i
    for j in range(i+1, len(a)):
        # Find the minimum element in the remaining unsorted array
        if a[min_idx] > a[j]:
            min_idx = j
    # Swap the found minimum element with the first element of the unsorted part
    a[i],a[min_idx] = a[min_idx], a[i]

print(a)  # This will now print the sorted list


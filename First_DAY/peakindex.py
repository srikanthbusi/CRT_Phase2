# # [1,3,6,7,9,5,2]
# apply binary search on this list and find the peak element
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
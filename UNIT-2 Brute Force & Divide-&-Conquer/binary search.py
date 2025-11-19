def binary_search(arr,x):
    l=0
    h=len(arr)-1
    while l<=h:
        mid=(l+h)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            l=mid+1
        else:
            h=mid-1
    return -1
arr=[2,4,6,8,13,15]
print(binary_search(arr,15))

def binarySearchRecursive(arr, value, start, end):
    
    if start > end:
        return -1
    
    mid = (start + end) // 2
    
    if value < arr[mid]:
        return binarySearchRecursive(arr, value, start, mid-1)
    elif value > arr[mid]:
        return binarySearchRecursive(arr, value, mid+1, end)
    else:
        return mid

array = [2,4,6,7,8,31,34,54,70,88,90,100]

print("BinarySearch: ", binarySearchRecursive(array, 70, 0, len(array)-1))
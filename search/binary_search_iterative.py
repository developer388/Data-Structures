def binarySearchIterative(arr, value):
    start = 0
    end = len(arr) -1
    
    while start <= end:
        
        mid = (start + end) // 2
        
        if value < arr[mid]:
            end = mid - 1
        elif value > arr[mid]:
            start = mid + 1 
        else:
            return mid
    
    return -1


array = [2,4,6,7,8,31,34,54,70,88,90,100]

print("BinarySearch: ", binarySearchIterative(array, 70))
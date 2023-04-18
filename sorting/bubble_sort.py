arr = [10,9,5,6,7,4,1,3,50,21,1]

"""
Algo
compare adjacent elements and swap them

    Loop 1
       set min_index as ith value
      Loop 2 from i+1 to end
        if jth value < min_index value
           set min_index as j
      swap(arr[j] & arr[min_index])

"""


for i in range(len(arr)):
   for j in range(len(arr)-i-1):
      if arr[j] > arr[j+1]:
         arr[j], arr[j+1] = arr[j+1],  arr[j]

print('Output: ', arr)
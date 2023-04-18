arr = [10,9,5,6,7,4,1,0,3,69,21,1]

"""
Algo
Find minimul value in the the 2nd loop
And swap it with ith value

    Loop 1
       set min_index as ith value
      Loop 2 from i+1 to end
        if jth value < min_index value
           set min_index as j
      swap(arr[j] & arr[min_index])

"""



for i in range(len(arr)):
    min_index = i

    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index],  arr[i]



    
print('Output: ', arr)
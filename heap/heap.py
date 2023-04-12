class MaxHeap:
    def __init__(self):
        self.array = []

    def insert(self, value):
        self.array.append(value)
        index_of_node = len(self.array)-1
        index_of_parent = 0

        while index_of_node > 0:
            index_of_parent = int((index_of_node-1)/2)

            if self.array[index_of_node] > self.array[index_of_parent]:
                self.array[index_of_node], self.array[index_of_parent] = self.array[index_of_parent], self.array[index_of_node]
                index_of_node = index_of_parent
            else:
                break
            

    def remove(self):

        if len(self.array) == 0:
            return None

        if len(self.array) == 1:
            return self.array.pop()

        result = self.array[0]

        self.array[0] = self.array.pop()

        index_of_node = 0
        index_of_left_child = 0
        index_of_right_child = 0

        while index_of_node < len(self.array):
            
            index_of_left_child = (index_of_node * 2) + 1
            index_of_right_child = (index_of_node * 2) + 2

            if index_of_left_child < len(self.array) and self.array[index_of_node] < self.array[index_of_left_child]:
                self.array[index_of_node], self.array[index_of_left_child] = self.array[index_of_left_child], self.array[index_of_node]
                index_of_node = index_of_left_child
            
            elif index_of_right_child < len(self.array) and self.array[index_of_node] < self.array[index_of_right_child]:
                self.array[index_of_node], self.array[index_of_right_child] = self.array[index_of_right_child], self.array[index_of_node]
                index_of_node = index_of_right_child
            else:
                break
            

        return result

    def heapify(self, array, i):
        index_of_left_child = (2 * i) + 1
        index_of_right_child = (2 * i) + 2

        if index_of_left_child < len(array) and array[i] < array[index_of_left_child]:
            array[i], array[index_of_left_child] = array[index_of_left_child], array[i]
            self.heapify(array, index_of_left_child)    
        
        if index_of_right_child < len(array) and array[i] < array[index_of_right_child]:
            array[i], array[index_of_right_child] = array[index_of_right_child], array[i]
            self.heapify(array, index_of_right_child)   

    def buildHeap(self, array):
        start_index = int(len(array)/2)

        for i in range(start_index, -1, -1):
            print(f'self.heapify(array, {i})')
            self.heapify(array, i)



heap = MaxHeap()
heap.insert(15)
heap.insert(9)
heap.insert(30)
heap.insert(3)
heap.insert(39)
heap.insert(1)

# print('Our implementation\n',heap.array)
# print(heap.remove())
# print(heap.remove())
# print(heap.remove())
# print(heap.remove())
# print(heap.remove())
# print(heap.remove())


input_array = [40,10,30,50,60,15]
print(input_array)

heap.buildHeap(input_array)
print(input_array)

# from python_datastructures import MaxHeap

# print('Lib implementation')
# h = MaxHeap([15,9,30,3,39,1])
# print(h.remove())
# print(h.remove())
# print(h.remove())
# print(h.remove())
# print(h.remove())
# print(h.remove())



"""
Concepts

Insertion:
new node is always added at the end of array

parent = (i-1) /2
left_child = (2 * i) + 1
right_child = ((2 * i) + 2


if node.value > parent.value
  swap node and parent

Deletion:
we will always find the required node on root
save root.value in result variable
replace root.value with array.last value
keep swapping new root value till leaf not to again make it heap


"""
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

		index_of_parent = 0
		index_of_left_child = 0
		index_of_right_child = 0

		while index_of_parent < len(self.array):
			
			index_of_left_child = (index_of_parent * 2) + 1
			index_of_right_child = (index_of_parent * 2) + 2

			index_of_smallest_child = index_of_parent

			if index_of_left_child < len(self.array) and self.array[index_of_left_child] > self.array[index_of_smallest_child]:
				index_of_smallest_child = index_of_left_child
			
			if index_of_right_child < len(self.array) and self.array[index_of_right_child] > self.array[index_of_smallest_child]:
				index_of_smallest_child = index_of_right_child
			
			if index_of_smallest_child == index_of_parent:
				break

			self.array[index_of_parent], self.array[index_of_smallest_child] = self.array[index_of_smallest_child], self.array[index_of_parent]
			index_of_parent = index_of_smallest_child 

		return result

	def heapifyDown(self, index_of_parent, array):
		index_of_left_child = (2 * index_of_parent) + 1
		index_of_right_child = (2 * index_of_parent) + 2

		index_of_smallest_child = index_of_parent

		if index_of_left_child < len(array) and array[index_of_left_child] > array[index_of_smallest_child] :
			index_of_smallest_child = index_of_left_child

		if index_of_right_child < len(array) and array[index_of_right_child] > array[index_of_smallest_child] :
			index_of_smallest_child = index_of_right_child

		if index_of_smallest_child != index_of_parent:
			array[index_of_parent], array[index_of_smallest_child] = array[index_of_smallest_child], array[index_of_parent]
			self.heapifyDown(index_of_smallest_child, array)
		
	def buildHeap(self, array):
		index_of_last_non_leaf_node = (len(array)//2) -1 

		for i in range(index_of_last_non_leaf_node, -1, -1):
			self.heapifyDown(i, array)

		return array

heap = MaxHeap()
# heap.insert(9)
# heap.insert(8)
# heap.insert(10)
# heap.insert(29)
# heap.insert(39)
# heap.insert(1)
# heap.insert(100)
# heap.insert(2)
# heap.insert(4)

# print('Our implementation\n',heap.array)
# print(heap.remove())
# print(heap.remove())
# print(heap.remove())
# print(heap.remove())
# print(heap.remove())
# print(heap.remove())
# print(heap.remove())
# print(heap.remove())
# print(heap.remove())
# print(heap.remove())
# print(heap.remove())


input_array = [9,8,10,29,39,1,2,4,100,0]
print('input_array:',input_array,'len: ', len(input_array))

print('heap.array:',heap.array,'len: ', len(heap.array))

heap.array = heap.buildHeap(input_array)

print('heap.array:',heap.array,'len: ', len(heap.array))

print("remove(): ",heap.remove())
print("remove(): ",heap.remove())
print("remove(): ",heap.remove())
print("remove(): ",heap.remove())
print("remove(): ",heap.remove())
print("remove(): ",heap.remove())
print("remove(): ",heap.remove())
print("remove(): ",heap.remove())
print("remove(): ",heap.remove())
print("remove(): ",heap.remove())
print("remove(): ",heap.remove())
print("remove(): ",heap.remove())
# print(input_array)

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
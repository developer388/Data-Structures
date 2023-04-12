from python_datastructures import Queue


"""
Implement stack using queue

trick -  use two queues
		 1 - trick is we have to keep the last added element at front of queue
		 2 - this can only be done if main queue is empty
		 3 - first empty the main queue and move its item to second queue
		 4 - add new element in empty main queue
		 5 - copy element from the second queue to main queue

we have two queues q1 and q2

- q1 is our main queue where we will add the element
- before adding element to q1,
  we will first deqeue all elements from q1 and move them to q2
- after moving all elements we will insert the element in q1
- after adding an element to q1, we will move all the elements from q2 to q1
- to dequeue an element, we will read from q1

"""


class Stack:
	def __init__(self):
		self.q1 = Queue()
		self.q2 = Queue()

	def push(self, value):
		
		while self.q1.isEmpty() != True:
			self.q2.enqueue(self.q1.dequeue().value)

		self.q1.enqueue(value)

		while self.q2.isEmpty() != True:
			self.q1.enqueue(self.q2.dequeue().value)

		return True

	def pop(self):
		return self.q1.dequeue().value



stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)


print("Test on stack: ")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())


print("Test on an list: ")

s = []
s.append(1)
s.append(2)
s.append(3)
s.append(4)

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())


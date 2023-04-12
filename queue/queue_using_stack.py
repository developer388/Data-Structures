"""
Implement queue using stack

algo:
	we will use two stacks, s1 and s2
	in enqueue operation we will keep adding elements to s1
	in dequeue operation we will pop all the elements from s1 and push them to s2
	  we will pop the element from s2 and save it in result variable
	  we will pop all the elements from s2 and push them to s1


"""


class Queue:
	def __init__(self):
		self.s1 = []
		self.s2 = []

	def enqueue(self, value):
		self.s1.append(value)
		return True


	def dequeue(self):

		while len(self.s1) > 0:
			self.s2.append(self.s1.pop())


		result = self.s2.pop()


		while len(self.s2) > 0:
			self.s1.append(self.s2.pop())


		return result


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

print("Result using implemented queue")
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())



"""
Test
"""
from python_datastructures import Queue
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print("Result using actual queue:")
print(q.dequeue().value)
print(q.dequeue().value)
print(q.dequeue().value)
print(q.dequeue().value)
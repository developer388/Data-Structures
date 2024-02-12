"""
Implement stack using queue

we will use two queues called Queue1 and Queue2

push:
- Queue1 is our main queue where we will add the element, before adding element to Queue1,
  we will first deqeue all elements from Queue1 and move them to Queue2
- after moving all elements we will insert the element in Queue1
- after adding an element to Queue1, we will move all the elements from Queue2 to Queue1

pop:
- to pop an element, we will dequeue one element from Queue1

"""

import queue

class Stack:
	def __init__(self):
		self.q1 = queue.Queue()
		self.q2 = queue.Queue()

	def push(self, value):
		
		while self.q1.empty() != True:
			self.q2.put(self.q1.get())

		self.q1.put(value)

		while self.q2.empty() != True:
			self.q1.put(self.q2.get())

		return True

	def pop(self):
		return self.q1.get()



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



'''
class Stack {
    
    constructor() {
        this.q1 = new Array()
        this.q2 = new Array()
    }
    
    push(value) {
        
        while(this.q1.length != 0) {
            this.q2.push(this.q1.shift())
        }
        
        this.q1.push(value)
        
        while(this.q2.length) {
            this.q1.push(this.q2.shift())
        }
    }
    
    pop() {
        return this.q1.shift()
    }
}

const stack = new Stack()

stack.push(1)
stack.push(2)
stack.push(3)

console.log(stack.q1)
//  console.log(stack.pop())
//  console.log(stack.pop())
//  console.log(stack.pop())


'''
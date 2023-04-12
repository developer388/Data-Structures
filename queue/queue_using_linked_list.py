"""
Implement queue using linked list

Trick: we will keep a pointer to head of linked list called front
       we will keep a pointer to tail of linked list called rear

       to dequeue an elment we will read the element at front and set front = front.next
       to enqueue an element we will set the rear to new_node and set rear = rear.next

"""


class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None    

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    
    def enqueue(self, value):
        
        node = LinkedListNode(value)
        
        if self.front == None and self.rear == None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        
        self.length += 1
    
    def dequeue(self):
        
        if self.front == None:
            self.rear = None;
            return None
        
        result = self.front.value
        self.front = self.front.next
        self.length -= 1
        
        if self.front == None:
            self.rear = None;
            
        return result
        
    def length(self):
        return self.length


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

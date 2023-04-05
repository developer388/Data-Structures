// Simple queue using array
class Queue {
    
    constructor(size) {
        if (!size) {
            size = 10
        }
        
        this.arr = new Array(size)
        this.size = 10
        this.front = -1
        this.rear = -1
    }
    
    enqueue(element) {
        if (this.rear == this.size -1) {
            console.log("Queue is full")
            return false
        }
        
        if (this.front == -1) {
            this.front++
        }
        
        this.arr[++this.rear] = element
        return true
    }
    
    dequeue() {
        if ( (this.front === -1 && this.rear === -1) || this.front>this.rear) {
            console.log("Queue is empty")
            return false
        }
        
        return this.arr[this.front++]
    }
}

let q = new Queue(5)
q.enqueue(1)
q.enqueue(2)
console.log(q.dequeue())
console.log(q.dequeue())
console.log(q.dequeue())

/**
  
  https://www.youtube.com/watch?v=O3y6A7WLlao
  
**/


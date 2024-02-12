// Simple queue using array
/*
     front [ , , , , ] rear
    
    the end from where elements are added in the queue is called "rear"
    the end from where elements are removed from the queue is called "front"

    initially both front and rear are set to -1

    during each enqueue() rear is incremented and value is set
    front will always point to first value 

    front is only incremented when we dequque() from the queue

    enqueue() 
         first increment the rear and then set the value
         array[++rear] = value
            
    dequeue()
        read the value at front and then increment it 

*/


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


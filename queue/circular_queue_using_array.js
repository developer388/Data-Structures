class Queue {
    constructor(size) {
            
        if (!size) {
            size = 10
        }
        
        this.size = size
        this.front = -1
        this.rear = -1
        this.capacity = 0
        this.array = new Array(size)
        return true
    }
    
    enqueue(value) {
        
       if (this.capacity === this.size) {
           console.log("Queue is full")
           return false
       } 
       else if (this.capacity === 0 ) {
            this.front = this.rear = 0
       }
       else {
           this.rear = (this.rear + 1) % this.size
       }
       
       this.array[this.rear] = value
       this.capacity++
       return true
    }
    
    dequeue() {
        if (this.capacity === 0) {
            console.log("Queue is empty")
            return false
        }
        else {
          
            let result = this.array[this.front]   
            this.front = (this.front+1) % this.size
            this.capacity--
            return result
        }
    }
}

const queue = new Queue(10)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)
queue.enqueue(9)
queue.enqueue(10)

console.log(queue.dequeue())
console.log(queue.dequeue())
console.log(queue.dequeue())
console.log(queue.dequeue())
console.log(queue.dequeue())
console.log(queue.dequeue())
console.log(queue.dequeue())

console.log(queue.array)

/*

https://www.youtube.com/watch?v=8sjFA-IX-Ww

*/


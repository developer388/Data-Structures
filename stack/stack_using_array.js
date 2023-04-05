class Stack {
    constructor(size) {
            
        if (!size) {
            size = 10
        }
        
        this.size = size
        this.top = -1
        this.array = new Array(size)
        return true
    }
    
    isFull() {
        return this.top === this.size-1
    }
    
    isEmpty() {
        return this.top < 0
    }
    
    push(value) {
       if (this.isFull()) {
           console.log("Stack is full")
           return false
       } else {
            this.array[++this.top] = value
            return true
       }
    }
    
    pop() {
        if (this.isEmpty()) {
            console.log("Stack if empty")
            return false
        }else {
            return this.array[this.top--]        
        }
    }
}

const stack = new Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
console.log(stack.array)

console.log(stack.pop())
console.log(stack.pop())
console.log(stack.pop())
console.log(stack.pop())

console.log(stack.array)



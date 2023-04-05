class Node {
    constructor(element) {
        this.data = element
        this.next = null
    }
}


class Stack {
    constructor(){
        this.top = null
        this.size = 0
    }
    
    push (element) {
        
        let node = new Node(element)
        
        if (this.top === null) {
            this.top = node
        } else {
            node.next = this.top
            this.top = node
        }
        
        this.size++
    }
    
    pop () {
        
        if (this.top === null) {
            console.log('Stack is empty')
            return
        }
       
        let result = this.top.data
        this.top = this.top.next
        this.size--
        return result
    }
    
}

let stack = new Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

console.log(stack.size)
console.log(stack.top)

console.log(stack.pop())
console.log(stack.pop())
console.log(stack.pop())
console.log(stack.pop())




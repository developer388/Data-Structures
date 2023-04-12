/*
Implement stack using linked list

algo:
    inititaly, we will a new node and set the top to new_node
    
    push operation:
    we will create new node and set its next to the top
    we will set the top to newly added node
    
    pop operation:
    we will store the value of top node in result variable
    we will set the top to top.next

*/

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




Array.prototype.dequeue = Array.prototype.shift
Array.prototype.enqueue = Array.prototype.push
Array.prototype.peek = function() {
    return this[this.length-1]
}

class Node {
    constructor (value) {
        this.data = value
        this.left = null
        this.right = null
    }
}

class Tree {
    constructor () {
        this.root = null
    }
}


/*
                1
              /   \
            2      3      
           / \    / \
          4   5  6   7 

DEPTH FIRST SEARCH ALGO
    PREORDER  (DATA, LEFT, RIGHT) : 1, 2, 4, 5, 3, 6, 7
    INORDER   (LEFT, DATA, RIGHT) : 4, 2, 5, 1, 6, 3, 7
    POSTORDER (LEFT, RIGHT, DATA) : 4, 5, 2, 6, 7, 3, 1

BREADTH FIRST SEARCH ALGO
    LEVELORDER                    : 1, 2, 3, 4, 5, 6, 7 
*/

function preOrderTraversal (node) {
    
    // DATA, LEFT, RIGHT
   
    const stack = [], result = []

    while (node !== null || stack.length !== 0) {

        if (node!=null) {
            result.push(node.data)
            stack.push(node)
            node = node.left
        }
        else {
            node = stack.pop()
            node = node.right
        }
    }

    return result
}

function inOrderTraversal (node) {
    
    // LEFT, DATA, RIGHT

    const stack = [], result = []

    while (node !== null || stack.length !== 0) {

        if (node!=null) {            
            stack.push(node)
            node = node.left
        }
        else {
            node = stack.pop()
            result.push(node.data)
            node = node.right
        }
    }

    return result
}

function postOrderTraversal (node) {
    
    // LEFT, RIGHT, DATA

    const stack = [], result = []
    let previous = null

    while (node !== null || stack.length !== 0) {

        if (node!=null) {            
            stack.push(node)
            node = node.left
        }
        else {

            node = stack.peek()

            if (node.right === null || node.right === previous) {
                result.push(node.data)
                stack.pop()
                previous = node
                node = null
            }
            else {
                node = node .right
            }
        }
    }

    return result
}

function levelOrderTraversal (node) {
    const queue = [], result = []
    
    queue.push(node)

    while (queue.length !== 0 ) {
        
        node = queue.dequeue()
        
        result.push(node.data)
        
        if (node.left) {
            queue.enqueue(node.left)
        }

        if (node.right) {
            queue.enqueue(node.right)
        }

    }

    return result
}

const tree = new Tree()
tree.root = new Node(1)
tree.root.left = new Node(2)
tree.root.right = new Node(3)
tree.root.left.left = new Node(4)
tree.root.left.right = new Node(5)
tree.root.right.left = new Node(6)
tree.root.right.right = new Node(7)

console.log("PreOrder Traversal: ", preOrderTraversal(tree.root))
console.log("InOrder Traversal: ", inOrderTraversal(tree.root))
console.log("PostOrder Traversal: ", postOrderTraversal(tree.root))
console.log("LevelOrder Traversal: ", levelOrderTraversal(tree.root))




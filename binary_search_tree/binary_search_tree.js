class Node {
    constructor(value) {
        this.value = value
        this.left = null
        this.right = null
    }
}


class BinaryTree {
    
    constructor() {
        this.root = null
    }
    
    inOrderTraversal(node){
        
        if (node === null) {
            return []
        }
            
        // left -> data -> right
        return this.inOrderTraversal(node.left).concat([node.value]).concat(this.inOrderTraversal(node.right))
    }
    
    inOrderReverseTraversal(node) {
        if (node === null) {
            return []
        }
        
        // right -> data -> left
        return this.inOrderReverseTraversal(node.right).concat([node.value]).concat(this.inOrderReverseTraversal(node.left))
    }
}


class BST extends BinaryTree {
    
    min(node) {

        if (node === null) {
            return null
        }
        
        while(node.left) {
            node = node.left
        }
        
        return node.value
    }
    
    max(node) {
        if (node === null) {
            return null
        }
        
        while(node.right) {
            node = node.right
        }
        
        return node.value
    }
    
    insert(node, value) {
        
        if (node === null) {
            return new Node(value)
        }
        
        if (value < node.value) {
            node.left = this.insert(node.left, value)
        }
        else if (value > node.value) {
            node.right = this.insert(node.right, value)
        }
        
        return node
    } 
    
    delete(node, value) {
        
        if (node === null) {
            return null
        }  
        
        if (value < node.value) {
            node.left = this.delete(node.left, value)
        }
        else if (value > node.value) {
            node.right = this.delete(node.right, value)
        }
        else {
            
            if (node.left === null && node.right === null) {  // has no child
                return null
            }
            
            if (node.left === null || node.right === null) {  // has one child
                return node.left || node.right
            }
            
            node.value = this.min(node.right)                 // has two child
            node.right = this.delete(node.right, node.value)
            
        }
        
        return node
    }
    
    predecessor(value) {
        if (this.root === null) {
            return null
        }
        
        if (this.root.value === value) {
            return null
        }
        
        let node = this.root
        let predecessor = null
        
        while (node) {
            if (value < node.value) {
                node = node.left    
            }  
            else if (value > node.value) {
                predecessor = node.value
                node = node.right
            }
            else {
                if (node.left) {
                    predecessor = this.max(node.left)
                }
                
                break
            }
            
        }
        
        return predecessor
    }
    
    successor(value) {
        if (this.root === null) {
            return null
        }
        
        if (this.root === value) {
            return null
        }
        
        let node = this.root
        let successor = null
        
        while (node) {
            
            if (value < node.value) {
                successor = node.value
                node = node.left
            }
            else if (value > node.value) {
                node = node.right
            }
            else {
                
                if (node.right) {
                    successor = this.min(node.right)
                }
                
                break
            }
        }
        return successor
    }

    kthSmallest(k){
        // left -> data -> right
        const stack = []
        let node = this.root
        
        while (node || stack.length) {
            if (node) {
                stack.push(node)
                node = node.left
            }
            else {
                node = stack.pop()
                
                if (--k === 0) {
                  break
                }
                
                node = node.right
            }
        }
        
        if (k > 0){
            return null
        }
        
        return node.value
    }
    
    kthLargest(k) {
        // right -> data -> left
        const stack = []
        let node = this.root
        
        while (node || stack.length) {
            if (node) {
                stack.push(node)
                node = node.right
            }
            else {
                node = stack.pop()
                
                if (--k === 0) {
                    break
                }
                
                node = node.left
            }
        }
        
        
        if (k > 0){
            return null
        }
        
        return node.value
    }
}


const bst = new BST()

bst.root = bst.insert(bst.root, 30) // set root

const values =  [70,35,50,34,37,32,36,38,39]


values.forEach(function(value){
    bst.insert(bst.root, value)   
})

console.log('inOrderTraversal(): ', bst.inOrderTraversal(bst.root))
console.log('inOrderReverseTraversal(): ', bst.inOrderReverseTraversal(bst.root))
console.log('min():', bst.min(bst.root), '  max():', bst.max(bst.root))

//bst.delete(bst.root, 35)
console.log('inOrderTraversal(): ', bst.inOrderTraversal(bst.root))

console.log('predecessor(32): ', bst.predecessor(32))
console.log('successor(35): ', bst.successor(35))


console.log('kthSmallest(): ', bst.kthSmallest(11))
console.log('kthLargest(): ', bst.kthLargest(10))



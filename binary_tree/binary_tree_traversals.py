from python_datastructures import Queue

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def preOrderTraversal(self):
        "data-> left-> right"
        stack = []
        result = []
        node = self.root

        while node!=None or len(stack)!=0:

            if node!=None:
                result.append(node.value)
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                node = node.right
        
        return result
    
    def inOrderTraversal(self):
        "left-> data-> right"
        stack = []
        result = []
        node = self.root

        while node!=None or len(stack)!=0:

            if node!=None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.value)
                node = node.right
        
        return result

    def postOrderTraversal(self):
        "left -> right -> data"
        stack = []
        result = []
        node = self.root
        previous = None

        while node!=None or len(stack)!=0:

            if (node!=None):
                stack.append(node)
                node = node.left
            else:

                node = stack[-1]

                if node.right==None or node.right==previous: 
                    result.append(node.value)
                    stack.pop()
                    previous = node
                    node = None
                else:
                    node = node.right
        
        return result


    def reverseInOrderTraversal(self):
        "right-> data-> left"
        stack = []
        result = []
        node = self.root

        while node!=None or len(stack)!=0:

            if node!=None:
                stack.append(node)
                node = node.right
            else:
                node = stack.pop()
                result.append(node.value)
                node = node.left
        
        return result

    def levelOrderTraversal(self): 
        node = self.root

        result = []

        if (node is None):
            return result

        queue = Queue()
        queue.enqueue(node)

        while queue.isEmpty() == False:
            node = queue.dequeue().value
            result.append(node.value)

            if node.left:
                queue.enqueue(node.left)

            if node.right:
                queue.enqueue(node.right)

        return result

    def inOrderRecursiveTraversal(self, node):
        if node:
            self.inOrderRecursiveTraversal2(node.left)
            self.inOrderRecursiveTraversal2(node.right)
            print(node.value)           
            
    def inOrderRecursiveTraversal2(self, node):
        if node is None:
            return []

        left_result = self.inOrderRecursiveTraversal3(node.left)
        right_result = self.inOrderRecursiveTraversal3(node.right)
        return left_result + [node.value] + right_result

if __name__ == "__main__":  
    tree = BinaryTree(Node(1))
    tree.root.left = Node(2)
    tree.root.right = Node(3)

    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    print('PreOrderTraversal: ', tree.preOrderTraversal())
    print('InOrderTraversal: ', tree.inOrderTraversal())
    print('PostOrderTraversal: ', tree.postOrderTraversal())
    print('ReverseInOrderTraversal: ', tree.reverseInOrderTraversal())
    print('LevelOrderTraversal: ', tree.levelOrderTraversal())
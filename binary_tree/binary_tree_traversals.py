from queue import Queue

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:

    root = None

    def inOrderTraversalIterative(self):
        
        # LEFT -> DATA -> RIGHT
        
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


    def preOrderTraversalIterative(self):
        
        #  DATA -> LEFT -> RIGHT
        
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
    
    
    def postOrderTraversalIterative(self):
        
        # LEFT -> RIGHT -> DATA

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


    def reverseInOrderTraversalIterative(self):
        
        # RIGHT -> DATA -> LEFT 

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


    def levelOrderTraversalIterative(self): 

        # LEVEL BY LEVEL

        node = self.root

        result = []

        if (node is None):
            return result

        queue = Queue()
        queue.put(node)

        while queue.empty() == False:
            node = queue.get()
            result.append(node.value)

            if node.left:
                queue.put(node.left)

            if node.right:
                queue.put(node.right)

        return result


    def inOrderTraversalRecursive(self, node):

        # LEFT -> DATA -> RIGHT

        if node is None:
            return []

        left_result = self.inOrderTraversalRecursive(node.left)
        right_result = self.inOrderTraversalRecursive(node.right)
        return left_result + [node.value] + right_result


    def preOrderTraversalRecursive(self, node):

        # DATA -> LEFT -> RIGHT

        if node is None:
            return []

        left_result = self.preOrderTraversalRecursive(node.left)
        right_result = self.preOrderTraversalRecursive(node.right)

        return [node.value] + left_result + right_result


    def postOrderTraversalRecursive(self, node):

        # LEFT -> RIGHT -> DATA

        if node is None:
            return []

        left_result = self.postOrderTraversalRecursive(node.left)
        right_result = self.postOrderTraversalRecursive(node.right)

        return left_result + right_result + [node.value]


    def reverseInOrderTraversalRecursive(self, node):
          
          # RIGHT -> DATA -> LEFT

          if node is None:
            return []

          left_result = self.reverseInOrderTraversalRecursive(node.left)
          right_result = self.reverseInOrderTraversalRecursive(node.right)

          return right_result + [node.value] + left_result


if __name__ == "__main__":  
   
    tree = BinaryTree()

    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)

    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    print('InOrderTraversalIterative: ', tree.inOrderTraversalIterative())
    print('PreOrderTraversalIterative: ', tree.preOrderTraversalIterative())
    print('PostOrderTraversalIterative: ', tree.postOrderTraversalIterative())
    print('ReverseInOrderTraversalIterative: ', tree.reverseInOrderTraversalIterative())
    
    print('\nLevelOrderTraversalIterative: ', tree.levelOrderTraversalIterative())

    print('\ninOrderTraversalRecursive: ', tree.inOrderTraversalRecursive(tree.root))
    print('preOrderTraversalRecursive: ', tree.preOrderTraversalRecursive(tree.root))
    print('postOrderTraversalRecursive: ', tree.postOrderTraversalRecursive(tree.root))
    print('reverseInOrderTraversalRecursive: ', tree.reverseInOrderTraversalRecursive(tree.root))
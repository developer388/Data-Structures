import sys
sys.path.append('..')

from binary_tree.binary_tree_traversals import BinaryTree

'''
 Points to remember
 - new node inserted always ends up as the leaf node.



'''

class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


class BinarySearchTree(BinaryTree):
	def __init__(self):
		self.root = None

	def min(self, node):

		if node is None:
			return None

		while node.left:
			node=node.left

		return node.value

	def max(self, node):		

		if Node is None:
			return None

		while node.right:
			node=node.right

		return node.value

	def insert(self, value):		

		if self.root==None:
			self.root = Node(value)
			return True
		
		node = self.root

		while node:
			if value<node.value:									
				if node.left==None:
					node.left = Node(value)
					break
				
				node = node.left					
			else:
				
				if node.right==None:
					node.right = Node(value)
					break
				
				node = node.right
		
		return True

	def insertRecursively(self, node, value):

		if node is None:
			node = Node(value)
			return node

		if value < node.value:
			node.left =  self.insertRecursively(node.left, value)
		else:
			node.right = self.insertRecursively(node.right, value)

		return node


	def delete(self, value):
		node = self.root
		parent = node

		if self.root is None:
			return None		

		while node:

			if value<node.value:  # value is less than node.value; go left				
				parent = node
				node = node.left			

			elif value>node.value: # value is greated than node.value; go right
				parent = node
				node = node.right

			else:										           # value is equal to node.value; process				
				if node.left==None and node.right==None:           # matching node is a leaf node
					if node.value < parent.value:                  # set parent pointer as null
						parent.left = None                         # break from the loop
					elif node.value > parent.value:
						parent.right = None
					else:
						self.root = None					       # match for root node							
					break

				elif node.left==None or node.right==None:	       # matching node has one child
					if node.value < parent.value:				   
						parent.left = node.left or node.right      # set parent pointer to node.next
					elif node.value > parent.value:
						parent.right = node.left or node.right
					else:
						self.root = node.left or node.right        # edge case if node to be deleted is root
					break
				
				else:											   # matching node has two childrens
																   # set node.value to minimum value in right subtree
					node.value = self.min(node.right)              # delete minimum value in right subtree
																   #      case1: node.right.left is null
																   #             which means we have to point parent.pointer to node.next
																   #             break from the loop
					if node.right.left is None:                    #      case2: node.right.left has subtree 
						node.right = node.right.right
						print('node.right.left is null')           #             which means we have to go left in node.right.left
						break                                      #             and set parent.pointer to null
					else:										   #             break from the loop
						print('node.right.left has subtree')
						node = node.right
						
						while node.left:
							parent = node
							node=node.left						
						
						if node.right:                            #      if last left most has right subtree
							parent.left = node.right              #      set parent.left = right subtree
						else:
							parent.left = None					  #      else parent.left = null as it is already pointing to smallest left most value
						break

	def deleteRecursively(self, node, value):

		if node is None:
			return None

		if value < node.value:
			node.left =  self.deleteRecursively(node.left, value)
		elif value > node.value:
			node.right = self.deleteRecursively(node.right, value)
		else:

			if node.left is None and node.right is None:         # node to be deleted is a leaf node
				return None

			if node.left is None or node.right is None:          # node to be deleted has one child
				return node.left or node.right

			node.value = self.min(node.right)                    # node to be deleted has two child nodes
			node.right = self.deleteRecursively(node.right, node.value)

		return node

	def predecessor(self, value):
		"""
		The predecessor of a node in BST is that node that will be visited just before the given node in the inorder traversal of the tree.
		If the given node is visited first in the inorder traversal, then its predecessor is NULL.

        Logic:
		  if matching node has no left subtree, then the immediate smaller value is in parent node
		  if matching node has left subtree, then immediate smaller value is maximum value in left subtree of given value
		"""
		node = self.root
		predecessor = None

		while node:
			if value<node.value:                   # if value is less than node.value go left
				node = node.left
			elif value>node.value:				   # if value is greater than node.value go right
				predecessor = node.value           # by going right we will get the next greater value
				node = node.right				   # hence store the current value is predecessor of next node				
			else:								   # match found for given node
				if node.left:                      # check in left subtree only because we want to read predecessor
					predecessor = self.max(node.left)  # in left subtree, greatest value will be predecessor					
				break
												   # if node has no left, predecessor would have been already set while moving right
					

		return predecessor
						
	def successor(self, value):
		"""
		The successor of a node in BST is that node that will be visited immediately after the given node in the inorder traversal of the tree.
		If the given node is visited last in the inorder traversal, then its successor is NULL.
		
        Logic:
		  if matching node has no right subtree, then the immediate greater value is in parent node
		  if matching node has right subtree, then immediate greater value is minimum value in left subtree 
		

		"""
		node = self.root
		successor = None

		while node:
			if value<node.value:                   # if value is less than node.value go left
				successor = node.value
				node = node.left
			elif value>node.value:				   # if value is greater than node.value go right
				node = node.right				   # hence store the current value is predecessor of next node				
			else:								   # match found for given node
				if node.right:                      # check in left subtree only because we want to read predecessor
					successor = self.min(node.right)  # in left subtree, greatest value will be predecessor					
				break
												   # if node has no left, predecessor would have been already set while moving right

		return successor

	def lowestCommonAncestor(self, p, q):
		node = self.root

		while node:
			if p < node.value and q < node.value:
				node = node.left			
			elif p > node.value and q > node.value:
				node = node.right
			else:
				break
		
		return node.value

	def convertSortedArrayToBST(self, array, start, end):	
		
		if start>end:
			return

		mid =  int((start+end)/2)				

		node = Node(array[mid])
			
		#print(f'{node.value}.left self.convertSortedArrayToBST({mid}, {start}, {mid-1})')
		node.left = self.convertSortedArrayToBST(array, start, mid-1)
		
		#print(f'{node.value}.right self.convertSortedArrayToBST({mid}, {mid+1}, {end})')
		node.right = self.convertSortedArrayToBST(array, mid+1, end)
		return node

bst = BinarySearchTree()


input_values = [30,70,35,50,34,37,32,36,38,39] # sample binary tree illustrated below#

bst.root = bst.insertRecursively(bst.root, 40)

for value in input_values:
	bst.insertRecursively(bst.root, value)

#print('PreOrderTraversal: ',bst.preOrderTraversal(),  len(bst.preOrderTraversal()))
#bst.delete(33)
#print('PreOrderTraversal: ',bst.preOrderTraversal(), len(bst.preOrderTraversal()))

print(bst.root)
print(bst.inOrderTraversalRecursive(bst.root))

bst.deleteRecursively(bst.root, 36)
print(bst.inOrderTraversalRecursive(bst.root))


#print(bst.lowestCommonAncestor(36,39))
# node = bst.convertSortedArrayToBST([1, 2, 3,4,5,6,7,8], 0, 7)

# tree = BinaryTree(node)
# print(tree.preOrderTraversal())



"""
Sample binary search tree

					  40
					 /  \
					/    \
				  30     70
				   `.     /
					 35 50
					/  \
				  34   37
				 /     /  \
			   32     36   38
							\
							39
Level Order [40,30,70,35,50,34,37,32,36,38,39]     






input_values = [2,33,25,40,34,36,39,45] #edge case (difficult)
input_values = [40,30,70,35,20,10, 34, 33,38,32,37,39, 27, 8,12,24,29, 5,9,22,25,28,31,36,45]

"""


































"""
Tested on leetcode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def min(self, node):
        while node.left:
            node=node.left

        return node.val


    def max(self, node):    
        while node.right:
            node=node.right

        return node.val

    
    def deleteNode(self, root, key):
        
        value = key
        node = root
        parent = node
        
        if root is None:
            return None
        
        if root.val==value:
            if root.left==None and root.right==None:
                root=None
                return root          
            
        

        while node:

            if value<node.val:  # value is less than node.val; go left              
                parent = node
                node = node.left            

            elif value>node.val: # value is greated than node.val; go right
                parent = node
                node = node.right

            else:                  # value is equal to node.val; process
                                         
                if node.left==None and node.right==None:    # matching node is a leaf node
                    if node.val<parent.val:             # set parent pointer as null
                        parent.left=None                    # break from the loop
                    else:
                        parent.right=None

                    break

                elif node.left==None or node.right==None:          # matching node.left or matching node.right is null  
                    
                    if node.val==root.val:
                        root = node.left or node.right
                    
                    
                    if node.val<parent.val:                    # either one of the chil of matching node is null 
                        parent.left = node.left or node.right      # set parent pointer to node.next
                    else:
                        parent.right = node.left or node.right
                    break
                
                else:                                              # matching node has two childrens
                                  # set node.val to minimum value in right subtree
                    node.val = self.min(node.right)              # delete minimum value in right subtree
                          #      case1: node.right.left is null
                                                                   #             which means we have to point parent.pointer to node.next
                                                                   #             break from the loop
                    if node.right.left is None:                    #      case2: node.right.left has subtree 
                        node.right = node.right.right
                                   #             which means we have to go left in node.right.left
                        break                                      #             and set parent.pointer to null
                    else:                                          #             break from the loop
                        
                        
                        node = node.right
                        
                        
                        
                        while node.left:
                            parent = node
                            node=node.left
                        
                        
                        if node.right:
                            parent.left = node.right
                        else:                            
                            parent.left = None
                        break
                        
        return root

"""
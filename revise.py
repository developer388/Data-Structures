'''
Pre Order    	Data Left Right
In Order     	Left Data Right
Post Order   	Data Left Right
Reverse InOrder Right Data Left
Level Order     Level by Level

'''

import queue


class Node:
	def __init__(self, value):
		self.data = value
		self.left = None
		self.right = None

class Tree:
	def __init__(self):
		self.root = None

	def levelOrderTraversal(self):
		# level 1 -> level 2 -> level 3
		result = []
		q = queue.Queue()

		q.put(self.root)

		while q.empty() == False:
			node = q.get()

			result.append(node.data)

			if node.left:
				q.put(node.left)

			if node.right:
				q.put(node.right)
		return result


	def preOrderTraversalIterative(self):
		# data -> left -> right

		result = []
		stack = []

		node = self.root

		while node or len(stack) != 0:

			if node:

				result.append(node.data)
				stack.append(node)
				node = node.left

			else:
				node = stack.pop()
				node = node.right

		return result



	def preOrderTraversalRecursive(self, node, result):
		# data -> left -> right

		if node is None:
			return

		result.append(node.data)
		
		self.preOrderTraversalRecursive(node.left, result)
		
		self.preOrderTraversalRecursive(node.right, result)


	def inOrderTraversalIterative(self):
		# left -> data -> right

		result = []
		stack = []

		node = self.root

		while node or len(stack)!=0:

			if node:
				stack.append(node)
				node = node.left
			else:
				node = stack.pop()
				result.append(node.data)
				node = node.right

		return result



	def inOrderTraversalRecursive(self, node, result):
		# left -> data -> right

		if node is None:
			return

		self.inOrderTraversalRecursive(node.left, result)		

		result.append(node.data)

		self.inOrderTraversalRecursive(node.right, result)


	def postOrderTraversalIterative(self):
		# left -> right -> data

		result = []
		stack = []
		previous = None
		node = self.root


		while node or len(stack)!=0:

			if node:
				stack.append(node)
				node = node.left
			else:
				node = stack[-1]

				if node.right==None or node.right == previous:
					node = stack.pop()
					result.append(node.data)
					previous = node
					node = None
				else:
					node = node.right

		return result


	def postOrderTraversalRecursive(self, node, result):
		# left -> right -> data

		if node is None:
			return

		self.postOrderTraversalRecursive(node.left, result)
		
		self.postOrderTraversalRecursive(node.right, result)

		result.append(node.data)

	def inOrderReverseTraversalRecursive(self, node, result):
		# right -> data -> left

		if node is None:
			return

		self.inOrderReverseTraversalRecursive(node.right, result)		

		result.append(node.data)

		self.inOrderReverseTraversalRecursive(node.left, result)





tree = Tree()

tree.root = Node(1)

tree.root.left = Node(2)
tree.root.right = Node(3)

tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

'''
				1
			  /   \
			2      3      
		   / |    / \
		  4  5   6   7 

DEPTH FIRST SEARCH ALGO
	PREORDER  (DATA, LEFT, RIGHT) : 1, 2, 4, 5, 3, 6, 7
	INORDER   (LEFT, DATA, RIGHT) : 4, 2, 5, 1, 6, 3, 7
	POSTORDER (LEFT, RIGHT, DATA) : 4, 5, 2, 6, 7, 3, 1

BREADTH FIRST SEARCH ALGO
	LEVELORDER                    : 1, 2, 3, 4, 5, 6, 7 

'''



# print('LevelOrderTraversal: ', tree.levelOrderTraversal())

# result = []
# tree.preOrderTraversalRecursive(tree.root, result)
# print('preOrderTraversalRecursive: ', result)

# print('preOrderTraversalIterative: ', tree.preOrderTraversalIterative())


# result = []
# tree.inOrderTraversalRecursive(tree.root, result)
# print('\ninOrderTraversalRecursive: ', result)
# print('inOrderTraversalIterative: ', tree.inOrderTraversalIterative())


# result = []
# tree.postOrderTraversalRecursive(tree.root, result)
# print('postOrderTraversalRecursive: ', result)
# print('postOrderTraversalIterative: ', tree.postOrderTraversalIterative())


# result = []
# tree.inOrderReverseTraversalRecursive(tree.root, result)
# print('inOrderReverseTraversalRecursive: ', result)



######### GRAPH #########


class Graph:

	def __init__(self):
		self.graph = {}

	def addVertex(self, vertex):
		self.graph[vertex] = []

	def addEdgeUndirected(self, source, destination):
		self.graph[source].append(destination)
		self.graph[destination].append(source)

	def addEdgeDirected(self, source, destination):
		self.graph[source].append(destination)		

	def addEdgeWeightedDirected(self, source, destination, weight):
		self.graph[source].append((weight, destination))

	def addEdgeWeightedUnDirected(self, source, destination, weight):
		self.graph[source].append((weight,destination))
		self.graph[destination].append((weight, source))



	def depthFirstTraversal(self, source):

		visited = {}

		for vertex in self.graph:
			visited[vertex] = False

		stack = []
		stack.append(source)

		result = []

		while len(stack)!=0:

			vertex = stack.pop()

			if visited[vertex] == False:
				result.append(vertex)
				visited[vertex] = True

			for neighbour in self.graph[vertex]:

				if visited[neighbour] == False:
					stack.append(neighbour)

		return result

	def breadFirstTraversal(self, source):

		visited = {}

		for vertex in self.graph:
			visited[vertex] = False


		q = queue.Queue()
		q.put(source)

		result = []

		while q.empty() == False:

			vertex = q.get()

			if visited[vertex] == False:
				result.append(vertex)
				visited[vertex] = True

			
			for neighbour in self.graph[vertex]:
				if visited[neighbour] == False:
					q.put(neighbour)

		return result


	def topologicalSortUsingDFS(self):


		def dfs(vertex, visited, result):

			visited[vertex] = True

			for neighbour in self.graph[vertex]:

				if visited[neighbour] == False:
					dfs(neighbour, visited, result)

			result.append(vertex)


		visited = {}

		for vertex in self.graph:
			visited[vertex] = False

		result = []

		for vertex in self.graph:

			if visited[vertex] == False:
				dfs(vertex, visited, result)
	
		result.reverse()
		return result


	def topologicalSortUsingInDegree(self):

		in_degree = {}

		for vertex in self.graph:
			in_degree[vertex] = 0

		for vertex in self.graph:

			for neighbour in self.graph[vertex]:
				in_degree[neighbour] += 1

		q = queue.Queue()

		for vertex in in_degree:

			if in_degree[vertex] == 0:
				q.put(vertex)

		result = []
		while q.empty()==False:

			vertex = q.get()

			result.append(vertex)

			for neighbour in self.graph[vertex]:

				in_degree[neighbour] -= 1

				if in_degree[neighbour] == 0:
					q.put(neighbour)

		return result


	def shortestPathUsingBFS(self, source, destination):

		visited = {}
		parent = {}

		for vertex in self.graph:
			visited[vertex] = False
			parent[vertex] = False

		parent[source] = -1

		q = queue.Queue()
		q.put(source)

		while q.empty() == False:

			vertex = q.get()

			for neighbour in self.graph[vertex]:

				if visited[neighbour] == False:
					parent[neighbour] = vertex
					visited[neighbour] = True
					q.put(neighbour)

		print(parent)

		result = []

		while parent[destination] != source:
			result.append(parent[destination])
			destination = parent[destination]

		return result
		

	def shortestPathUsingDijkstra(self, source, destination):

		visited = {}
		distance = {}

		parent = {}
		parent[source] = None

		for vertex in self.graph:
			visited[vertex] = False
			distance[vertex] = float('inf')				

		result = []

		q = []

		import heapq

		heapq.heappush(q, (0, source))

		while len(q)>0:

			weight, vertex = heapq.heappop(q)

			if visited[vertex] == False:

				for neighbour_weight, neighbour_vertex in self.graph[vertex]:

					if weight+neighbour_weight < distance[neighbour_vertex]:
						distance[neighbour_vertex] = weight+neighbour_weight

						parent[neighbour_vertex] = vertex
						heapq.heappush(q, (distance[neighbour_vertex], neighbour_vertex))


		print(parent)
		path = []
		vertex = destination
		
		while vertex is not None:
			path.append(vertex)
			vertex = parent[vertex]
		
		path.reverse()

		return path

	def shortestPathUsingBellmanFord(self, source, destination):

		weight = {}

		for vertex in self.graph:
			weight[vertex] = float('inf')


		weight[source] = 0

		parent = {}
		parent[source] = None

		for i in range(len(self.graph)-1):

			for vertex in self.graph:

				for neighbour_weight, neighbour_vertex in self.graph[vertex]:

					if (weight[vertex]!=float('inf')) and ((weight[vertex]+neighbour_weight) < weight[neighbour_vertex]):
						weight[neighbour_vertex] = weight[vertex]+neighbour_weight
						parent[neighbour_vertex] = vertex

		for vertex in self.graph:

			for neighbour_weight, neighbour_vertex in self.graph[vertex]:

				if (weight[vertex]!=float('inf')) and ((weight[vertex]+neighbour_weight) < weight[neighbour_vertex]):
					
					print('cycle exists')
		
		print(parent)
		path = []
		vertex = destination
		
		while vertex is not None:
			path.append(vertex)
			vertex = parent[vertex]
		
		path.reverse()

		return path

	def minimumSpanningTree(self, source):

		visited = set()

		import heapq

		priority_queue = []

		for weight, neighbour in self.graph[source]:
			heapq.heappush(priority_queue, (weight, source, neighbour))

		mst_edges = []

		while len(visited) < len(self.graph):

			weight, source, destination = heapq.heappop(priority_queue)

			if destination not in visited:
				visited.add(destination)
				mst_edges.append((source, destination, weight))

				for weight, neighbour in self.graph[destination]:
					heapq.heappush(priority_queue, (weight, destination, neighbour))

		return mst_edges

	def minimumSpanningTree2(self, source):

		import heapq

		visited = {}

		for vertex in self.graph:
			visited[vertex] = False

		priority_queue = []

		mst_edges = []

		for weight, neighbour in self.graph[source]:
			heapq.heappush(priority_queue, (weight, source, neighbour))
		
		while len(priority_queue)>0:
			weight, source, neighbour = heapq.heappop(priority_queue)

			if visited[neighbour] == False:

				print('not visited: ',neighbour)

				visited[neighbour] = True
				mst_edges.append((source, neighbour, weight))

				for neighbour_weight, neighbour_vertex in self.graph[neighbour]:
					heapq.heappush(priority_queue, (neighbour_weight, neighbour, neighbour_vertex))
			else:
				print('already visited: ',neighbour)


		return mst_edges

	def disjointSet(self, source):

		parent = {}
		rank = {}

		for vertex in self.graph:
			parent[vertex] = vertex
			rank[vertex] = 0



		def findParent(parent, vertex):
			if parent[vertex] == vertex:
				return vertex

			parent[vertex] =  findParent(parent, parent[vertex])
			return parent[vertex]

		def unionSet(parent, first_vertex, second_vertex):
			first_vertex = findParent(parent, first_vertex)
			second_vertex = findParent(parent, second_vertex)


			if first_vertex == second_vertex:
				return False

			if rank[first_vertex] < rank[second_vertex]:
				parent[first_vertex] = second_vertex

			elif rank[second_vertex] < rank[first_vertex]:
				parent[second_vertex] = first_vertex
			
			else:
				parent[first_vertex] = second_vertex
				rank[second_vertex]+=1

			return True

		sorted_edges = []
		import heapq


		for vertex in self.graph:
			for weight, neighbour in self.graph[vertex]:
				sorted_edges.append((weight, vertex, neighbour))
				# heapq.heappush(sorted_edges,(weight, source, neighbour))




		print('Unsorted Edges: ', sorted_edges)
		sorted_edges.sort()
		print('Sorted Edges  : ', sorted_edges)

		minimum_weight = 0

		result = []

		for edge in sorted_edges:

			weight, source, destination = edge

			if unionSet(parent, source, destination):
				minimum_weight += weight
				result.append(edge)

		# while len(sorted_edges) > 0:

		# 	weight, source, neighbour = heapq.heappop(sorted_edges)

		# 	source_parent = findParent(parent, source)
		# 	neighbour_parent = findParent(parent, neighbour)

		# 	if source_parent != neighbour_parent:
		# 		minimum_weight += weight
		# 		unionSet(parent, source, neighbour_parent)

		return result, minimum_weight

	def findBridgeInGraph(self):

		discovery_time = {}
		lowest_discovery_time = {}
		visited = {}
		time_counter = 0

		for vertex in self.graph:
			discovery_time[vertex] = 0
			lowest_discovery_time[vertex] = 0
			visited[vertex] = False

		def dfs(graph, vertex, visited, discovery_time, lowest_discovery_time, time_counter, parent):
			visited[vertex] = True

			time_counter += 1
			discovery_time[vertex] = lowest_discovery_time[vertex] = time_counter

			for neighbour in graph[vertex]:
				if neighbour == parent:
					continue
				elif visited[neighbour] == False:
					dfs(graph, neighbour, visited, discovery_time, lowest_discovery_time, time_counter, vertex)
					lowest_discovery_time[vertex] = min(lowest_discovery_time[vertex], lowest_discovery_time[neighbour])

					if discovery_time[vertex] < lowest_discovery_time[neighbour]:
						print('Bridge: ', vertex, ' ---- ', neighbour)
				else:
					lowest_discovery_time[vertex] = min(lowest_discovery_time[vertex], discovery_time[neighbour])

		for vertex in self.graph:
			if visited[vertex] == False:
				dfs(self.graph, vertex, visited, discovery_time, lowest_discovery_time, time_counter, -1)

	def findArticulationPointsInGraph(self):

		discovery_time = {}
		lowest_discovery_time = {}
		visited = {}
		time_counter = 0
		articulation_points = []

		for vertex in self.graph:
			discovery_time[vertex] = 0
			lowest_discovery_time[vertex] = 0
			visited[vertex] = False

		def dfs(graph, vertex, visited, discovery_time, lowest_discovery_time, time_counter, parent, articulation_points):
			visited[vertex] = True

			time_counter += 1
			discovery_time[vertex] = lowest_discovery_time[vertex] = time_counter
			children = 0

			for neighbour in graph[vertex]:
				if neighbour == parent:
					continue
				elif visited[neighbour]:
					lowest_discovery_time[vertex] = min(lowest_discovery_time[vertex], discovery_time[neighbour])
				else:
					dfs(graph, neighbour, visited, discovery_time, lowest_discovery_time, time_counter, vertex, articulation_points)
					lowest_discovery_time[vertex] = min(lowest_discovery_time[vertex], lowest_discovery_time[neighbour])

					if discovery_time[vertex] <= lowest_discovery_time[neighbour] and parent!= -2:
						articulation_points.append(vertex)
					children+=1	
			
			if parent == -1 and children > 1:
				articulation_points.append(vertex)


		for vertex in self.graph:
			if visited[vertex] == False:
				dfs(self.graph, vertex, visited, discovery_time, lowest_discovery_time, time_counter, -1, articulation_points)

		return articulation_points



graph = Graph()

# graph.addVertex(1)
# graph.addVertex(2)
# graph.addVertex(3)
# graph.addVertex(4)
# graph.addVertex(5)
# graph.addVertex(6)

# graph.addEdgeUndirected(1,2)
# graph.addEdgeUndirected(1,3)
# graph.addEdgeUndirected(2,6)
# graph.addEdgeUndirected(3,4)
# graph.addEdgeUndirected(6,5)
# graph.addEdgeUndirected(4,5)


# graph.addEdgeDirected(1,2)
# graph.addEdgeDirected(1,3)
# graph.addEdgeDirected(2,6)
# graph.addEdgeDirected(6,5)
# graph.addEdgeDirected(5,4)
# graph.addEdgeDirected(3,4)

# graph.addEdgeWeightedDirected(1,2, 2)
# graph.addEdgeWeightedDirected(2,6, 2)
# graph.addEdgeWeightedDirected(6,5, 2)
# graph.addEdgeWeightedDirected(5,4, 2)
# graph.addEdgeWeightedDirected(1,3, 12)
# graph.addEdgeWeightedDirected(3,4, 12)


# minimum spanning tree

'''
		
		   0 
		2 /6\
		 /   3
		1
	  /	 \
   5 /	3 \
	/      \
   4	    2	

'''

# graph.addVertex(0)
# graph.addVertex(1)
# graph.addVertex(2)
# graph.addVertex(3)
# graph.addVertex(4)

# graph.addEdgeWeightedUnDirected(0,1, 2)
# graph.addEdgeWeightedUnDirected(0,3, 6)
# graph.addEdgeWeightedUnDirected(1,3, 8)
# graph.addEdgeWeightedUnDirected(1,4, 5)
# graph.addEdgeWeightedUnDirected(1,2, 3)
# graph.addEdgeWeightedUnDirected(2,4, 7)

# graph.addVertex(0)
# graph.addVertex(1)
# graph.addVertex(2)
# graph.addVertex(3)

# graph.addEdgeWeightedUnDirected(0,1, 2)
# graph.addEdgeWeightedUnDirected(0,3, 4)
# graph.addEdgeWeightedUnDirected(0,2, 4)
# graph.addEdgeWeightedUnDirected(1,2, 2)
# graph.addEdgeWeightedUnDirected(1,3, 3)
# graph.addEdgeWeightedUnDirected(2,3, 1)


# print('MST: ', graph.disjointSet(0))

# graph.addVertex(0)
# graph.addVertex(1)
# graph.addVertex(2)
# graph.addVertex(3)
# graph.addVertex(4)
# graph.addVertex(5)

# graph.addEdgeUndirected(1,0)
# graph.addEdgeUndirected(1,2)
# graph.addEdgeUndirected(2,0)
# graph.addEdgeUndirected(0,3)
# graph.addEdgeUndirected(3,5)
# graph.addEdgeUndirected(3,4)
# graph.addEdgeUndirected(4,5)

# print('MST: ', graph.findArticulationPointsInGraph())


graph.addVertex(0)
graph.addVertex(1)
graph.addVertex(2)
graph.addVertex(3)
graph.addVertex(4)

graph.addEdgeUndirected(1,0)
graph.addEdgeUndirected(1,2)
graph.addEdgeUndirected(2,0)
graph.addEdgeUndirected(0,3)
graph.addEdgeUndirected(3,4)

# print('MST: ', graph.findArticulationPointsInGraph())




'''
		12
	1	->	2
   /          \
  v            v
3				6
			   / 
  v           v
	4  <-   5

'''

# print('depthFirstTraversal: ', graph.depthFirstTraversal(1))

# print('breadFirstTraversal: ', graph.breadFirstTraversal(1))


# print('topologicalSortUsingDFS: ', graph.topologicalSortUsingDFS())

# print('topologicalSortUsingInDegree: ', graph.topologicalSortUsingInDegree())


# print('shortestPathUsingBFS: ', graph.shortestPathUsingBFS(1,5))


#print('shortestPathUsingDijkstra: ', graph.shortestPathUsingDijkstra(1,4))


#print('shortestPathUsingBellmanFord: ', graph.shortestPathUsingBellmanFord(1,4))


class Graph2:

	def __init__(self):
		#self.graph = [[1, 1, 0, 0, 0],[0, 1, 0, 0, 1],[1, 0, 0, 1, 1],[0, 0, 0, 0, 0],[1, 0, 1, 0, 0]]
		self.graph = [[1,1,1],[1,1,0],[1,0,1]]

	def findIslands(self):
		# start from 0,0

		visited = []

		for i in range(5):
			visited.append([False]*5)

		
		counter = 0
		
		def dfs(graph, x, y, visited):
		
			if (x < 0) or (x > 4) or (y < 0 ) or (y > 4):
				return

			if visited[x][y] == True:
				return

			if graph[x][y] != 1:
				return

			visited[x][y] = True
			print((x,y))
			dfs(graph, x-1, y-1, visited)
			dfs(graph, x-1, y, visited)
			dfs(graph, x-1, y+1, visited)
			
			dfs(graph, x, y-1, visited)           
			dfs(graph, x, y+1, visited)
			
			dfs(graph, x+1, y-1, visited)
			dfs(graph, x+1, y, visited)
			dfs(graph, x+1, y+1, visited)




		for row in range(5):
			for col in range(5):
				if self.graph[row][col] == 1 and visited[row][col]==False:
					print(f'graph[{row}][{col}]={self.graph[row][col]}, counter={counter}')
					dfs(self.graph, row, col, visited)
					counter += 1
		return counter

	def floodFill(self):
		# start from 1,1

		visited = []

		for i in range(5):
			visited.append([False]*3)

		
		counter = 0
		
		def dfs(graph, x, y, visited):
		
			if (x < 0) or (x > 2) or (y < 0 ) or (y > 2):
				return

			if visited[x][y] == True:
				return

			if graph[x][y] != 1:
			 	return

			visited[x][y] = True
			
			if graph[x][y] == 1:
				graph[x][y] = 2
				print((x,y))

			dfs(graph, x-1, y, visited)
			
			dfs(graph, x, y-1, visited)           
			dfs(graph, x, y+1, visited)
			
			dfs(graph, x+1, y, visited)




		
		dfs(self.graph, 1, 1, visited)
		
		return self.graph








	   

graph = Graph2()

print('DFS: ', graph.floodFill())
		

'''
	v(0) v(1) v(2) v(3) v(4) 
v(0)

v(1)

v(2)

v(3)

v(4)

[
	[1, 1, 0, 0, 0],
	[0, 1, 0, 0, 1],
	[1, 0, 0, 1, 1],
	[0, 0, 0, 0, 0],
	[1, 0, 1, 0, 0]
]
'''
class Graph:

	def __init__(self):
		self.graph = {}
	
	def addVertex(self, vertex):
		self.graph[vertex] = []

	def addDirectedEdge(self, source, destination):
		self.graph[source].append(destination)


	def topologicalSortUsingInDegree(self, source):

		#### visited array is not requried ####
		# make a in_degree dictionary
		# set in_degree as 0 of all vertices
		#
		# for each vertex goto its neighbour
		#      for each neighbour increment the in_degree by 1
		#
		# make a empty queue
		# 
		# iterate over each vertex in in_degree dictionary
		# and push the vertices to queue whose in_degree is 0
		# 
		# make a result empty array
		# 
		# while queue is not empty loop
		#   dequeue 1 element from queue and push it to result
		#   for each neighbour of dequeued vertex
		#     decrement the in_degree by 1
		#     if in_degree becomes 0 by decrement operation
		#     push that vertex to queue

		in_degree = {}

		
		for vertex in self.graph:
			in_degree[vertex] = 0

		
		for vertex in self.graph:
			for neighbour in self.graph[vertex]:
				in_degree[neighbour]+=1

		
		from collections import deque
		queue = deque()

		for vertex in in_degree:
			if in_degree[vertex] == 0:
				queue.append(vertex)
		
		result = []

		while len(queue)>0:

			vertex = queue.popleft()
			result.append(vertex)

			for neighbour in self.graph[vertex]:
				in_degree[neighbour]-=1
				if in_degree[neighbour] == 0:
					queue.append(neighbour)

		return result

	def topologicalSortUsingDFS(self, source):

		#### visited array is required ####

		# make an empty visited dictionary
		# make an empty array for storing result
		#
		# for each vertex set visited as False
		# for each vertex 
		#     if vertex is not visited
		#           call depth first search function
		#           passing current_vertex, visited_dictionary, result_array		
		#
		# reverse the result array
		# return the reversed result array
		#
		# define a DFS function
		#    set visited as true for current_vertex
		#
		#    for each neighbour for current vertex
		#        check if neighbour is visited, if not
		#              call dfs with neighbour, visited_dictionary, result_array
		#
		#	 result.append(current_vertex)    
		#
		#


		visited = {}

		for vertex in self.graph:
			visited[vertex] = False


		result = []

		def DFS(vertex, visited, result):
			visited[vertex] = True			

			for neighbour in self.graph[vertex]:
				if visited[neighbour] == False:
					DFS(neighbour, visited, result)

			result.append(vertex)

			


		for vertex in self.graph:
			if visited[vertex] == False:
				DFS(vertex, visited, result)


		result.reverse()
		return result


	def shortestPathUsingBFS(self, source):

		from collections import deque
		queue = deque()
		queue.append(source)


		visited = {}
		for vertex in self.graph:
			visited[vertex] = False


		parent = {}

		result = []
		while len(queue)>0:
			
			vertex = queue.popleft()
			
			if visited[vertex] == False:
				result.append(vertex)
				visited[vertex] = True

			for neighbour in self.graph[vertex]:				
				if visited[neighbour]==False:
					queue.append(neighbour)
					parent[neighbour] = vertex


		shortest_path = {}
		
		for vertex in self.graph:
			if vertex not in shortest_path:
				shortest_path[vertex] = []

			dest = vertex
			while source!=dest:
				shortest_path[vertex].append(parent[dest])
				dest = parent[dest]

		return shortest_path




graph = Graph()

# topo sort
# graph.addVertex('1')
# graph.addVertex('2')
# graph.addVertex('3')
# graph.addVertex('4')
# graph.addVertex('5')
# graph.addVertex('6')
# graph.addVertex('7')

# graph.addDirectedEdge('1','2')
# graph.addDirectedEdge('2','3')
# graph.addDirectedEdge('4','3')
# graph.addDirectedEdge('5','4')
# graph.addDirectedEdge('6','5')
# graph.addDirectedEdge('7','6')


#print('Graph: ', graph.graph)
#print('Result:', graph.topologicalSortUsingInDegree('1'))
#print('Result:', graph.topologicalSortUsingDFS('1'))



# shortest path algo BFS

graph.addVertex('1')
graph.addVertex('2')
graph.addVertex('3')
graph.addVertex('4')
graph.addVertex('5')
graph.addVertex('6')
graph.addVertex('7')
graph.addVertex('8')


graph.addDirectedEdge('1','2')
graph.addDirectedEdge('1','8')
graph.addDirectedEdge('1','7')

graph.addDirectedEdge('2','6')
graph.addDirectedEdge('2','3')
graph.addDirectedEdge('2','4')

graph.addDirectedEdge('3','6')

graph.addDirectedEdge('4','3')
graph.addDirectedEdge('4','5')

graph.addDirectedEdge('7','5')
graph.addDirectedEdge('8','7')

print('result: ', graph.shortestPathUsingBFS('1'))


'''

	shorted path in an unweighted graph ?
	  ans:	BFS


	shortest path in an weighted graph (positive)?
	  ans:	dijkstra algorithm


	shortest path in an weighted graph (can have negatives)?
	  ans:	bellman ford algorithm


'''

# array = [1,2,3,4,5,6,7,8]

# def log(n):
# 	if n>len(array)-1:
# 		return

# 	print(array[n])
# 	log(n+1)
	


# log(0)
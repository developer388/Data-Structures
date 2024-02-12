from queue import Queue
import heapq

class Graph:
	def __init__(self):
		self.graph = {}


	def addVertex(self, vertex):
		self.graph[vertex] = []

	def addDirectedEdge(self, source, destination):
		self.graph[source].append(destination)

	def addUndirectedEdge(self, source, destination):
		self.graph[source].append(destination)
		self.graph[destination].append(source)

	def addWeightedDirectedEdge(self, source, destination, weight):
		self.graph[source].append((weight, destination))

	def addWeightUndirectedEdge(self, source, destination, weight):
		self.graph[source].append((weight, destination))
		self.graph[destination].append((weight, source))


	def DFS(self, source):
		stack = []
		result = []

		visited = {}
		for vertex in self.graph:
			visited[vertex] = False

		stack.append(source)

		while len(stack)>0:

			vertex = stack.pop()

			if visited[vertex] == False:
				result.append(vertex)
				visited[vertex] = True

			for neighbour in self.graph[vertex]:
				if visited[neighbour] == False:
					stack.append(neighbour)

		return result

	def BFS(self, source):
		
		queue = Queue()
		visited = {}

		for vertex in self.graph:
			visited[vertex] = False

		result = []

		queue.put(source)
		
		while queue.empty() == False:

			vertex = queue.get()

			if visited[vertex] == False:
				result.append(vertex)
				visited[vertex] = True

			for neighbour in self.graph[vertex]:
				if visited[neighbour] == False:
					queue.put(neighbour)

		return result
	
	def topologicalSortUsingDFS(self):

		def DFS(vertex, visited, result):
			visited[vertex] = True

			for neighbour in self.graph[vertex]:
				if visited[neighbour] == False:
					DFS(neighbour,visited, result)

			result.append(vertex)

		visited = {}

		for vertex in self.graph:
			visited[vertex] = False

		result = []

		for vertex in self.graph:
			if visited[vertex] == False:
				DFS(vertex, visited, result)

		return result


	def topologicalSortUsingInDegree(self):

		in_degree = {}

		for vertex in self.graph:
			in_degree[vertex] = 0


		for vertex in self.graph:
			for neighbour in self.graph[vertex]:
				in_degree[neighbour] += 1


		queue = Queue()

		for vertex in in_degree:
			if in_degree[vertex] == 0:
				queue.put(vertex)
		

		result = []

		while queue.empty() == False:
			vertex = queue.get()

			result.append(vertex)

			for neighbour in self.graph[vertex]:
				in_degree[neighbour]-=1

				if in_degree[neighbour] == 0:
					queue.put(neighbour)

		return result


	def shortestPathUsingBFS(self, source, destination):

		visited = {}
		parent = {}

		for vertex in self.graph:
			visited[vertex] = False
			parent[vertex] = False

		queue = Queue()
		queue.put(source)


		parent[source] = -1
		visited[source] = True

		while queue.empty()==False:

			vertex = queue.get()
			
			for neighbour in self.graph[vertex]:
				if visited[neighbour]==False:
					visited[neighbour] = True
					parent[neighbour] = vertex
					queue.put(neighbour)

		path = []
		path.append(destination)
		while destination!=source:
			path.append(parent[destination])
			destination = parent[destination]

		print('path', path)
		return path

	def shortestPathInWeightedGraph(self, source, destination):

		def DFS(vertex, visited, result):
			visited[vertex] = True

			for neighbour in self.graph[vertex]:
				if visited[neighbour[1]] == False:
					DFS(neighbour[1], visited, result)

			result.append(vertex)


		visited = {}
		result = []
		distance = {}

		for vertex in self.graph:
			visited[vertex] = False
			distance[vertex] = float('inf')

		# print('visited: ', visited)

		for vertex in self.graph:
			if visited[vertex] == False:
				DFS(vertex, visited, result)


		print('TopoSort: ', result)

		distance[source] = 0
	
		# print('Distance: ', distance)

		while len(result)>0:
			vertex = result.pop()

			if distance[vertex] != float('inf'):
				for neighbour_weight, neighbour_vertex in self.graph[vertex]:
					if distance[vertex]+neighbour_weight < distance[neighbour_vertex]:
						distance[neighbour_vertex] = distance[vertex] + neighbour_weight

		return distance[destination]
		


	def shortestPathUsingDijkstra(self, source, destination):

		visited = {}
		distance = {}
		queue = []

		for vertex in self.graph:
			visited[vertex] = False
			distance[vertex] = float('inf')

		heapq.heappush(queue,(0, source))

		while len(queue)>0:
			current_distance, current_vertex = heapq.heappop(queue)

			print('pop()', current_distance, current_vertex)

			if visited[current_vertex]==False:
				visited[current_vertex] = True

				for neighbour_weight, neighbour_vertex in self.graph[current_vertex]:
					
					if current_distance+neighbour_weight < distance[neighbour_vertex]:
						distance[neighbour_vertex] = current_distance+neighbour_weight
						heapq.heappush(queue, (distance[neighbour_vertex], neighbour_vertex))
				

		print('Distance: ', distance)
		return distance[destination]


	def shortestPathUsingBellmanFord(self, source, destination):

		weight = {}

		for vertex in self.graph:
			weight[vertex] = float('inf')

		weight[source] = 0

		for i in range(len(self.graph)-1):			
			for vertex in self.graph:
				for neighbour_weight, neighbour_vertex in self.graph[vertex]:
					#print(f'vertex: {vertex}, neighbour: {neighbour_vertex}')
					if (weight[vertex]!=float('inf')) and ((weight[vertex] + neighbour_weight) < weight[neighbour_vertex]):
						weight[neighbour_vertex] = weight[vertex] + neighbour_weight


		print('weight: ', weight)

		for vertex in self.graph:
			for neighbour_weight, neighbour_vertex in self.graph[vertex]:
				#print(f'vertex: {vertex}, neighbour: {neighbour_vertex}')
				if (weight[vertex]!=float('inf')) and ((weight[vertex] + neighbour_weight) < weight[neighbour_vertex]):
					print('cycle exists in graph')



		return weight[destination]





graph = Graph()

# graph.addVertex('1')
# graph.addVertex('2')
# graph.addVertex('3')
# graph.addVertex('4')
# graph.addVertex('5')
# graph.addVertex('6')
# graph.addVertex('7')
# graph.addVertex('8')


# graph.addVertex('0')
# graph.addVertex('1')
# graph.addVertex('2')
# graph.addVertex('3')
# graph.addVertex('4')
# graph.addVertex('5')


graph.addVertex('1')
graph.addVertex('2')
graph.addVertex('3')
graph.addVertex('4')
graph.addVertex('5')


# graph.addUndirectedEdge('1','2')
# graph.addUndirectedEdge('1','4')
# graph.addUndirectedEdge('1','3')
# graph.addUndirectedEdge('2','5')
# graph.addUndirectedEdge('3','8')
# graph.addUndirectedEdge('4','6')
# graph.addUndirectedEdge('5','8')
# graph.addUndirectedEdge('6','7')
# graph.addUndirectedEdge('7','8')

# graph.addDirectedEdge('1','2')
# graph.addDirectedEdge('1','4')
# graph.addDirectedEdge('1','3')
# graph.addDirectedEdge('2','5')
# graph.addDirectedEdge('5','7')
# graph.addDirectedEdge('7','6')
# graph.addDirectedEdge('4','7')
# graph.addDirectedEdge('4','8')
# graph.addDirectedEdge('8','6')
# graph.addDirectedEdge('3','6')



# graph.addWeightUndirectedEdge('0','1', 5)
# graph.addWeightUndirectedEdge('0','2', 3)
# graph.addWeightUndirectedEdge('1','2', 2)
# graph.addWeightUndirectedEdge('1','3', 6)
# graph.addWeightUndirectedEdge('2','3', 7)
# graph.addWeightUndirectedEdge('2','4', 4)
# graph.addWeightUndirectedEdge('2','5', 2)
# graph.addWeightUndirectedEdge('3','4', -1)
# graph.addWeightUndirectedEdge('4','5', -2)


# graph.addWeightUndirectedEdge('0','1', 2)
# graph.addWeightUndirectedEdge('0','2', 8)
# graph.addWeightUndirectedEdge('1','4', 6)
# graph.addWeightUndirectedEdge('1','2', 5)
# graph.addWeightUndirectedEdge('2','4', 3)
# graph.addWeightUndirectedEdge('2','3', 2)
# graph.addWeightUndirectedEdge('3','4', 1)
# graph.addWeightUndirectedEdge('3','5', 3)
# graph.addWeightUndirectedEdge('4','5', 9)




graph.addWeightedDirectedEdge('1','2', 6)
graph.addWeightedDirectedEdge('1','3', 5)
graph.addWeightedDirectedEdge('2','4', -1)
graph.addWeightedDirectedEdge('3','2', -2)
graph.addWeightedDirectedEdge('3','4', 4)
graph.addWeightedDirectedEdge('3','5', 3)
graph.addWeightedDirectedEdge('4','5', 3)



# print('DFS: ', graph.DFS('1'))
# print('BFS: ', graph.BFS('1'))
# print('TopologicalSortUsingDFS: ', graph.topologicalSortUsingDFS())
# print('TopologicalSortUsingInDegree: ', graph.topologicalSortUsingInDegree())


#print(graph.graph)

#print('ShortestPathUsingBFS: ', graph.shortestPathUsingBFS('1', '7'))
#print('ShortestPathInWeightedGraph: ', graph.shortestPathInWeightedGraph('0','5'))

print('ShortestPathUsingBellmanFord: ', graph.shortestPathUsingBellmanFord('1','5'))


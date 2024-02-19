from queue import Queue
import heapq

class Graph:
	def __init__(self, *vertices):
		self.adjancency_list = {}

		for vertex in vertices:
			self.adjancency_list[vertex] = []

	def addDirectedEdge(self, source, destination):
		self.adjancency_list[source].append(destination)

	def addUndirectedEdge(self, source, destination):
		self.adjancency_list[source].append(destination)
		self.adjancency_list[destination].append(source)

	def addWeightedDirectedEdge(self, source, destination, weight):
		self.adjancency_list[source].append((weight, destination))

	def addWeightUndirectedEdge(self, source, destination, weight):
		self.adjancency_list[source].append((weight, destination))
		self.adjancency_list[destination].append((weight, source))


	def DFS(self, source):
		stack = []
		result = []

		visited = {}
		for vertex in self.adjancency_list:
			visited[vertex] = False

		stack.append(source)

		while len(stack)>0:

			vertex = stack.pop()

			if visited[vertex] == False:
				result.append(vertex)
				visited[vertex] = True

				for neighbour in self.adjancency_list[vertex]:
					if visited[neighbour] == False:
						stack.append(neighbour)

		return result

	def BFS(self, source):
		
		queue = Queue()
		visited = {}

		for vertex in self.adjancency_list:
			visited[vertex] = False

		result = []

		queue.put(source)
		
		while queue.empty() == False:

			vertex = queue.get()

			if visited[vertex] == False:
				result.append(vertex)
				visited[vertex] = True

				for neighbour in self.adjancency_list[vertex]:
					if visited[neighbour] == False:
						queue.put(neighbour)

		return result
	
	def topologicalSortUsingDFS(self):

		def DFS(vertex, visited, result):
			visited[vertex] = True

			for neighbour in self.adjancency_list[vertex]:
				if visited[neighbour] == False:
					DFS(neighbour,visited, result)

			result.append(vertex)

		visited = {}

		for vertex in self.adjancency_list:
			visited[vertex] = False

		result = []

		for vertex in self.adjancency_list:
			if visited[vertex] == False:
				DFS(vertex, visited, result)

		return result


	def topologicalSortUsingInDegree(self):

		in_degree = {}

		for vertex in self.adjancency_list:
			in_degree[vertex] = 0


		for vertex in self.adjancency_list:
			for neighbour in self.adjancency_list[vertex]:
				in_degree[neighbour] += 1


		queue = Queue()

		for vertex in in_degree:
			if in_degree[vertex] == 0:
				queue.put(vertex)
		

		result = []

		while queue.empty() == False:
			vertex = queue.get()

			result.append(vertex)

			for neighbour in self.adjancency_list[vertex]:
				in_degree[neighbour]-=1

				if in_degree[neighbour] == 0:
					queue.put(neighbour)

		return result


	def shortestPathUsingBFS(self, source, destination):

		visited = {}
		parent = {}

		for vertex in self.adjancency_list:
			visited[vertex] = False
			parent[vertex] = False

		queue = Queue()
		queue.put(source)


		parent[source] = -1
		visited[source] = True

		while queue.empty()==False:

			vertex = queue.get()
			
			for neighbour in self.adjancency_list[vertex]:
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

			for neighbour in self.adjancency_list[vertex]:
				if visited[neighbour[1]] == False:
					DFS(neighbour[1], visited, result)

			result.append(vertex)


		visited = {}
		result = []
		distance = {}

		for vertex in self.adjancency_list:
			visited[vertex] = False
			distance[vertex] = float('inf')

		# print('visited: ', visited)

		for vertex in self.adjancency_list:
			if visited[vertex] == False:
				DFS(vertex, visited, result)


		print('TopoSort: ', result)

		distance[source] = 0
	
		# print('Distance: ', distance)

		while len(result)>0:
			vertex = result.pop()

			if distance[vertex] != float('inf'):
				for neighbour_weight, neighbour_vertex in self.adjancency_list[vertex]:
					if distance[vertex]+neighbour_weight < distance[neighbour_vertex]:
						distance[neighbour_vertex] = distance[vertex] + neighbour_weight

		return distance[destination]
		


	def shortestPathUsingDijkstra(self, source, destination):

		visited = {}
		distance_from_source = {}
		queue = []

		for vertex in self.adjancency_list:
			visited[vertex] = False
			distance_from_source[vertex] = float('inf')

		heapq.heappush(queue,(0, source))

		while len(queue)>0:

			distance_to_vertex, vertex = heapq.heappop(queue)

			if visited[vertex]==False:
				visited[vertex] = True

				for distance_from_vertex_to_neighbour, neighbour in self.adjancency_list[vertex]:
					
					if distance_to_vertex+distance_from_vertex_to_neighbour < distance_from_source[neighbour]:
						distance_from_source[neighbour] = distance_to_vertex + distance_from_vertex_to_neighbour
						heapq.heappush(queue, (distance_from_source[neighbour], neighbour))
				

		return distance_from_source[destination]


	def shortestPathUsingBellmanFord(self, source, destination):

		weight = {}

		for vertex in self.adjancency_list:
			weight[vertex] = float('inf')

		weight[source] = 0

		for i in range(len(self.adjancency_list)-1):			
			for vertex in self.adjancency_list:
				for neighbour_weight, neighbour_vertex in self.adjancency_list[vertex]:
					#print(f'vertex: {vertex}, neighbour: {neighbour_vertex}')
					if (weight[vertex]!=float('inf')) and ((weight[vertex] + neighbour_weight) < weight[neighbour_vertex]):
						weight[neighbour_vertex] = weight[vertex] + neighbour_weight


		print('weight: ', weight)

		for vertex in self.adjancency_list:
			for neighbour_weight, neighbour_vertex in self.adjancency_list[vertex]:
				#print(f'vertex: {vertex}, neighbour: {neighbour_vertex}')
				if (weight[vertex]!=float('inf')) and ((weight[vertex] + neighbour_weight) < weight[neighbour_vertex]):
					print('cycle exists in graph')



		return weight[destination]





graph = Graph(0,1,2,3,4,5,6,7,8)

# graph.addUndirectedEdge(0, 1)
# graph.addUndirectedEdge(0, 2)
# graph.addUndirectedEdge(0, 7)
# graph.addUndirectedEdge(1, 4)
# graph.addUndirectedEdge(2, 4)
# graph.addUndirectedEdge(2, 3)
# graph.addUndirectedEdge(3, 5)
# graph.addUndirectedEdge(3, 6)
# graph.addUndirectedEdge(7, 6)


# dijkstra
graph.addWeightUndirectedEdge(0, 1, 2)
graph.addWeightUndirectedEdge(1, 4, 0)
graph.addWeightUndirectedEdge(4, 5, 0)

graph.addWeightUndirectedEdge(0, 2, 1)
graph.addWeightUndirectedEdge(2, 3, 1)
graph.addWeightUndirectedEdge(3, 5, 1)


# print('DFS(): ', graph.DFS(0))

# print('BFS(): ', graph.BFS(0))


print('Dijkstra: ', graph.shortestPathUsingDijkstra(0, 5))
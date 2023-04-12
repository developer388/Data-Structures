from python_datastructures import Queue

class Graph:
	def __init__(self, vertex_count):
		self.list = []		

		for i in range(vertex_count):
			self.list.append([])

	def addEdge(self, source, destination):
		self.list[source].append(destination)
		self.list[destination].append(source)

	def bfs(self, start):
		result = []
		visited = [False] * len(self.list)
		queue = Queue()
		queue.enqueue(start)

		while queue.isEmpty() == False:
			
			vertex = queue.dequeue().value
				
			if visited[vertex] == False:
				result.append(vertex)
				visited[vertex] = True

				
				for i in range(len(self.list[vertex])):
					if visited[self.list[vertex][i]] == False:
						queue.enqueue(self.list[vertex][i])
				
		return result

	def dfs(self, start):
		result = []
		stack = []
		visited = [False] * len(self.list)

		stack.append(start)

		while len(stack) != 0:
			vertex = stack.pop()

			if visited[vertex] == False:
				result.append(vertex)
				visited[vertex] = True

				for i in range(len(self.list[vertex])):
					if visited[self.list[vertex][i]] == False:
						stack.append(self.list[vertex][i])

		return result

	def print(self):
		for i in range(len(self.list)):
			row = f"{i}: " + str(self.list[i])
			print(row)



graph = Graph(13)

graph.addEdge(0,1)
graph.addEdge(0,4)

graph.addEdge(1,2)
graph.addEdge(1,5)

graph.addEdge(2,3)
graph.addEdge(2,6)

graph.addEdge(3,7)

graph.addEdge(4,8)

graph.addEdge(5,6)
graph.addEdge(5,10)

graph.addEdge(6,11)

graph.addEdge(7,12)

graph.addEdge(8,9)

graph.addEdge(9,10)

graph.addEdge(10,11)

graph.addEdge(11,12)

graph.print()
print('\n\nbfs: \n', graph.bfs(0))

print('\n\ndfs: \n', graph.dfs(0))

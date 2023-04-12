class Graph:
	def __init__(self):
		self.dictionary = {}

	def addVertex(self, vertex):
		if (vertex in self.dictionary) == False:
			self.dictionary[vertex] = []
			return True
		
		return False

	def addEdge(self, source, destination):
		if (source in self.dictionary == False) or (destination in self.dictionary == False):
			print('invalid vertex used')
			return False
		
		self.dictionary[source].append(destination)

graph = Graph()

graph.addVertex('a')
graph.addVertex('b')
graph.addVertex('c')
graph.addVertex('d')

graph.addEdge('a', 'b')
graph.addEdge('a', 'c')
graph.addEdge('b', 'd')
graph.addEdge('c', 'd')


print(graph.dictionary)
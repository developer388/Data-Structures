class Graph:
    def __init__(self, vertex_count):
        self.matrix = []
        for i in range(vertex_count):
            self.matrix.append([0]*vertex_count)

    def addEdge(self, source, destination):
        self.matrix[source][destination] = 1

    def print(self):        
        string = ''

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
               string += str(self.matrix[i][j])

            string +='\n'

        return string


graph = Graph(3)

graph.addEdge(0,1)
graph.addEdge(1,2)
graph.addEdge(0,2)

print(graph.print())

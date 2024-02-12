class Graph:
    def __init__(self, vertex_count):
        self.matrix = []
        for i in range(vertex_count):
            self.matrix.append([0]*vertex_count)

    def addEdge(self, source, destination):
        self.matrix[source][destination] = 1

    def iterativeDFS(self, source):
        
        visited = [False] * len(self.matrix)
        stack = [source]
        result = []

        while len(stack)!=0:

            vertex = stack.pop()

            if visited[vertex] == False:
                result.append(vertex)
                visited[vertex] = True
                
                for neighbour_index in range(len(self.matrix[vertex])): 
                    if (self.matrix[vertex][neighbour_index] == 1) and (visited[neighbour_index] == False):
                        stack.append(neighbour_index)
        return result

    def recursiveDFS(self, result, visited, vertex):
        if visited[vertex] == False:
            result.append(vertex)
            visited[vertex] = True

        for neighbour_index in range(len(self.matrix[vertex])):
            if (self.matrix[vertex][neighbour_index] == 1) and (visited[neighbour_index] == False):
                self.recursiveDFS(result, visited, neighbour_index)

    def recursiveDFS2(self, result, visited, vertex):
        visited[vertex] = True

        for neighbour_index in range(len(self.matrix[vertex])):
            if (self.matrix[vertex][neighbour_index] == 1) and (visited[neighbour_index] == False):
                self.recursiveDFS2(result, visited, neighbour_index)

        result.append(vertex)

    def topologicalSortUsingDFS(self, vertex):

        visited = [False] * len(self.matrix[vertex])
        stack = []

        for v in range(len(self.matrix)):
            if visited[v] == False:
                self.recursiveDFS2(stack, visited, v)

        result = []

        while len(stack)!=0:
            result.append(stack.pop())

        return result

    def topologicalSortUsingBFS(self):

        in_degree = [0] * len(self.matrix)

        for vertex in range(len(self.matrix)):
            for neighbour_index in range(len(self.matrix[vertex])):
                if self.matrix[vertex][neighbour_index] == 1:
                    in_degree[neighbour_index]+=1

        print('in_degree: ', in_degree)

        queue = []

        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)
       
        print('queue: ', queue)

        result = []
        
        while len(queue)!=0:
            vertex = queue.pop(0)
            result.append(vertex)

            for neighbour_index in range(len(self.matrix[vertex])):
                if (self.matrix[vertex][neighbour_index] == 1):
                    in_degree[neighbour_index] -= 1

                    if in_degree[neighbour_index] == 0:
                        queue.append(neighbour_index)

        return result

    def bfs(self, vertex):

        result = []
        queue = [vertex]
        visited = [False] *  len(self.matrix[vertex])

        while len(queue) != 0:
            vertex = queue.pop(0)
            result.append(vertex)
            visited[vertex] = True

            for neighbour_index in range(len(self.matrix[vertex])):
                if (self.matrix[vertex][neighbour_index] == 1) and (visited[neighbour_index] == False):
                    queue.append(neighbour_index)

        return result


            
    def print(self):
        string = ''

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
               string += str(self.matrix[i][j])

            string +='\n'

        return string


graph = Graph(6)

graph.addEdge(2,3)
graph.addEdge(3,1)
graph.addEdge(4,1)
graph.addEdge(4,0)
graph.addEdge(5,0)
graph.addEdge(5,2)


# graph.addEdge(0,3)
# graph.addEdge(0,2)
# graph.addEdge(2,3)
# graph.addEdge(2,1)
# graph.addEdge(3,1)
# graph.addEdge(1,4)
# graph.addEdge(5,1)
# graph.addEdge(5,4)


print('Graph: ', graph.print())

print('IterativeDFS: ', graph.iterativeDFS(5))
print('BFS: ', graph.bfs(5))




visited = [False] * len(graph.matrix[0])
result = []

graph.recursiveDFS(result, visited, 5)
print('RecursiveDFS: ', result)


print('topologicalSortUsingDFS: ', graph.topologicalSortUsingDFS(5))

print('topologicalSortUsingBFS: ', graph.topologicalSortUsingBFS())


from queue import Queue

class Graph:

    vertices = []
    
    def __init__(self, vertices_count):
        
        for i in range(vertices_count):
            self.vertices.append([0]*vertices_count)
            
    def addUndirectedEdge(self, source, destination):
        self.vertices[source][destination] = 1
        self.vertices[destination][source] = 1
        
    def addDirectedEdge(self, source, destination):
        self.vertices[source][destination] = 1
    
    def depthFirstSearchTraversal(self, source):
        
        visited = [False] * len(self.vertices)
    
        stack = []
        stack.append(source)
        
        result = []
        
        while len(stack) != 0:
            
            vertex = stack.pop()
            
            if visited[vertex] == False:
                result.append(vertex)
                visited[vertex] = True
                
            for neighbour_index in range(len(self.vertices[vertex])):
                if (self.vertices[vertex][neighbour_index] == 1) and (visited[neighbour_index] == False):
                    stack.append(neighbour_index)
        return result
    
    def depthFirstSearchRecursive(self, source):
        
        visited = [False] * len(self.vertices)
        
        result = []
        
        def dfs(vertices, visited, vertex, result):
            
            if visited[vertex] == False:
                visited[vertex] = True
                result.append(vertex)
            
            for neighbour_index in range(len(vertices[vertex])):
                if (vertices[vertex][neighbour_index] == 1) and  (visited[neighbour_index] == False):
                    dfs(vertices, visited, neighbour_index, result)
            
        dfs(self.vertices, visited, source, result)
        
        return result
        
    def breadthFirstSearchIterative(self, source):
        
        visited = [False] * len(self.vertices[source])
        
        q = Queue()
        
        q.put(source)
        
        result = []
        
        while q.empty() == False:
            
            vertex = q.get()
            
            if visited[vertex] == False:
                result.append(vertex)
                visited[vertex] = True
                
            for neighbour_index in range(len(self.vertices[vertex])):
                
                if (self.vertices[vertex][neighbour_index] == 1) and (visited[neighbour_index] == False):
                    q.put(neighbour_index)
            
        return result
                    
                
            
graph = Graph(5)

# https://media.geeksforgeeks.org/wp-content/cdn-uploads/undirectedgraph.png
graph.addUndirectedEdge(0,1)
graph.addUndirectedEdge(0,4)

graph.addUndirectedEdge(1,2)
graph.addUndirectedEdge(1,3)
graph.addUndirectedEdge(1,4)

graph.addUndirectedEdge(4,3)
graph.addUndirectedEdge(3,2)


print('DFS: ', graph.depthFirstSearchTraversal(0))
print('DFS: ', graph.depthFirstSearchRecursive(0))

print('DFS: ', graph.breadthFirstSearchIterative(0))



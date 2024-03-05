from queue import Queue
import heapq

class Graph:
    
    def __init__(self, *vertices):
        self.adjacency_list = {}
        
        for vertex in vertices:
            self.adjacency_list[vertex] = []
        
    def addDirectedEdge(self, source, destination):
        self.adjacency_list[source].append(destination)

    def addUndirectedEdge(self, source, destination):
        self.adjacency_list[source].append(destination)
        self.adjacency_list[destination].append(source)
    
    def addUndirectedWeightedEdge(self, source, destination, weight):
        self.adjacency_list[source].append((weight, destination))
        self.adjacency_list[destination].append((weight, source))
    
    def DFS(self, vertex, visited, result):
        
        visited[vertex] = True
        
        for neighbour in self.adjacency_list[vertex]:
            if visited[neighbour] == False:
                self.DFS(neighbour, visited, result)
                
        result.append(vertex)
        
    
    def topologicalSort(self):
        
        visited = {}
        result = []
        
        for vertex in self.adjacency_list:
            visited[vertex] = False
        
        for vertex in self.adjacency_list:
            if visited[vertex] == False:
                self.DFS(vertex, visited, result)
        
        
        return result
        
    def shortestPathUsingBFS(self, source, destination):
        
        visited = {}
        parent = {}
        queue = Queue()
        
        for vertex in self.adjacency_list:
            visited[vertex] = False
            parent[vertex] = False
        
        
        queue.put(source)
        visited[source] = True
        
        while queue.empty() == False:
            
            vertex = queue.get()
            
            for neighbour in self.adjacency_list[vertex]:
                
                if visited[neighbour] == False:
                    visited[neighbour] = True
                    parent[neighbour] = vertex
                    
                    queue.put(neighbour)
                    
                    
        
        print('parnet:', parent)
        
        path = []
        
        path.append(destination)
        
        while destination != source:
            path.append(parent[destination])
            destination = parent[destination]
            
        
        return path
        
    def dijkstra(self, source, destination):
        
        queue = []
        visited = {}
        distance = {}
        
        for vertex in self.adjacency_list:
            visited[vertex] = False
            distance[vertex] = float('inf')
        
        heapq.heappush(queue, (0, source))
        
        while len(queue) > 0:
            
            distance_to_vertex, vertex = heapq.heappop(queue)
            
            if visited[vertex] == False:
                
                for distance_to_neighbour, neighbour in self.adjacency_list[vertex]:
                    
                    if distance_to_vertex + distance_to_neighbour < distance[neighbour]:
                        distance[neighbour] = distance_to_vertex + distance_to_neighbour 
                        
                        heapq.heappush(queue, (distance[neighbour], neighbour))
        
        return distance[destination]
graph = Graph(0,1,2,3,4,5,6)

# graph.addDirectedEdge(0,1)
# graph.addDirectedEdge(0,2)
# graph.addDirectedEdge(1,3)
# graph.addDirectedEdge(2,3)
# graph.addDirectedEdge(3,4)
# graph.addDirectedEdge(4,5)
# graph.addDirectedEdge(5,6)
# print("Graph: ", graph.adjacency_list)
# print("Topo Sort: ", graph.topologicalSort())



# graph.addUndirectedEdge(0,1)
# graph.addUndirectedEdge(0,2)

# graph.addUndirectedEdge(1,5)
# graph.addUndirectedEdge(5,6)

# graph.addUndirectedEdge(2,3)
# graph.addUndirectedEdge(3,4)
# graph.addUndirectedEdge(4,6)

graph.addUndirectedWeightedEdge(0, 1, 2)
graph.addUndirectedWeightedEdge(1, 4, 0)
graph.addUndirectedWeightedEdge(4, 5, 0)

graph.addUndirectedWeightedEdge(0, 2, 1)
graph.addUndirectedWeightedEdge(2, 3, 1)
graph.addUndirectedWeightedEdge(3, 5, 1)


print("Graph: ", graph.adjacency_list)
print("Dijkstra Algorithm: ", graph.dijkstra(0, 5))

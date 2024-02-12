class Graph {
    
    constructor() {
        this.vertex = {}
    }
    
    addVertex(vertex) {
        if (vertex in this.vertex === false) {
            this.vertex[vertex] = []
            return true
        }
        
        return false
    }
    
    addEdge(vertex_a, vertex_b) {
        
        // directed Graph
        
        if ((vertex_a in this.vertex === false) || (vertex_b in this.vertex === false)) {
            console.log('vertex are not present in graph')
            return false
        }    
        
        this.vertex[vertex_a].push(vertex_b)
        
    }
    
    depthFirstTraversal(vertex) {
        
        if (vertex in this.vertex === false) {
         return []   
        }
        
        let visited = {}
        
        for (let key in this.vertex) {
            visited[key] = false
        }
        
        let stack = [vertex]
        let result = []
        
        while (stack.length>0) {
        
            let current_vertex = stack.pop()
            
            if (visited[current_vertex] === false) {
                result.push(current_vertex)
                visited[current_vertex] = true
            }
            
            for (let neighbour of this.vertex[current_vertex]) {
                
                if (visited[neighbour] === false) {
                    stack.push(neighbour)
                }
            }
        }
        
        return result
    }
    
    breadthFirstTraversal(vertex) {
        
        if (vertex in this.vertex === false) {
            return []
        }
        
        let visited = {}
        
        for (let key in this.vertex){
            visited[key] = false
        }
        
        let queue = [vertex]
        
        let result = []
        
        while(queue.length) {
            let current_vertex = queue.shift()
            
            
            if ((visited[current_vertex]) === false) {
                result.push(current_vertex)
                visited[current_vertex] = true
            
            }
            
            for (let neighbour of this.vertex[current_vertex]) {
                
                if (visited[neighbour] === false) {
                    queue.push(neighbour)
                }
            }
        }
        
        return result
     }
     
    topoSortUtil(vertex, visited, result){
        
        visited[vertex] = true
        
        for (let neighbour of this.vertex[vertex]) {
            if(visited[neighbour]===false) {
                this.topoSortUtil(neighbour, visited, result)
            }
        }
        
        result.push(vertex)
    }
    
    topoSort(v){
        let visited = {}
        let stack = []
        let result = []
        
        for (let key in this.vertex) {
            visited[key] = false
        }
        
        for (let vertex in this.vertex) {
            if (visited[vertex] === false)
                this.topoSortUtil(vertex, visited, result)
        }
        
        return result
    }
    
    
    topoSortUsingKahnsAlgorithm(){ 
        
        console.log('Graph: ', this.vertex)
        
        let inDegree = {}
        
        for (let vertex in this.vertex) {
            inDegree[vertex] = 0
        }
        
        console.log('inDegree : ', inDegree)
        
        for (let vertex in this.vertex) {
                
            for (let neighbour of this.vertex[vertex]){
                inDegree[neighbour]+=1
            }
        }
        console.log('inDegree : ', inDegree)
    
        let queue = []
        
        for (let vertex in inDegree) {
            if (inDegree[vertex] === 0) {
                queue.push(vertex)
            }
        }
        
        console.log('Queue: ', queue)
        
        let result = []
        
        while (queue.length>0) {
            let vertex = queue.shift()
            result.push(vertex)
            
            console.log('a', this.vertex[vertex])
            
                
            for (let neighbour of this.vertex[vertex]) {
                inDegree[neighbour] -= 1
                
                if (inDegree[neighbour] === 0){
                    queue.push(neighbour)
                }
            }
        }
        
        return result
        
    }
}

const graph = new Graph()
graph.addVertex('1')
graph.addVertex('2')
graph.addVertex('3')
graph.addVertex('4')
graph.addVertex('5')

graph.addEdge('1', '2')
graph.addEdge('1', '3')
graph.addEdge('2', '4')
graph.addEdge('2', '5')
graph.addEdge('3', '4')
graph.addEdge('4', '5')

console.log('DepthFirstTraversal: ', graph.depthFirstTraversal('1'))
console.log('BreadthFirstTraversal: ', graph.breadthFirstTraversal('1'))
console.log('TopologicalSort: ', graph.topoSort('1'))
console.log('TopologicalSort Kahn\'s Algo: ', graph.topoSortUsingKahnsAlgorithm('1'))




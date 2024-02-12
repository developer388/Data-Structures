//https://leetcode.com/problems/course-schedule-ii/


var findOrder = function(numCourses, prerequisites) {
    
    var in_degree = new Array(numCourses).fill(0)

    console.log('in_degree: ', in_degree)
    
    var graph = {}
    
    for (var i=0; i<numCourses; i++) {
      graph[i] = []
    }

    
    
    for (var i=0; i<prerequisites.length; i++) {
         console.log(prerequisites[i][0], prerequisites[i][1])
         in_degree[prerequisites[i][1]]++
         graph[prerequisites[i][0]].push(prerequisites[i][1])
        
    }
    
    console.log(graph)
    console.log('in_degree: ', in_degree)


    var queue = []

    for (var i=0; i<in_degree.length; i++) {
        if (in_degree[i] === 0) {
            queue.push(i)
        }
    }

    console.log('queue: ', queue)
    
    var result = []
    
    while (queue.length>0) {
        var vertex = queue.shift()
        result.push(vertex)

        for (var i=0; i<graph[vertex].length; i++) {
            in_degree[graph[vertex][i]]--

            if (in_degree[graph[vertex][i]] === 0) {
                queue.push(graph[vertex][i])
            } 
        }
    }

    if (result.length === in_degree.length) 
    	return result.reverse()
    else 
    	return []

};


console.log(findOrder(2, [[1,0]]))
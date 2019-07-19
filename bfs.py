import collections
def bfs(graph, root): 
    visited, queue = set(), collections.deque([root])
    print(queue)
    visited.add(root)
    while queue: 
        vertex = queue.popleft()
        for neighbour in graph[vertex]: 
            if neighbour not in visited: 
                visited.add(neighbour) 
                queue.append(neighbour) 
    print(visited)
    print(queue)
    print(vertex)


graph = {0: [1, 2], 1: [2], 2: [3], 3: [1,2]}
bfs(graph, 0)

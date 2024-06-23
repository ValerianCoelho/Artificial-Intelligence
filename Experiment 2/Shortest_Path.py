def dfsShortestPath(graph):
    paths = []
    visited = []
    stack = [[start]]
    while stack:
        current_path = stack.pop() # pop the last path
        node = current_path[-1] # get the last node from the path
        if node not in visited:
            visited.append(node)
            for neighbour in graph[node]:
                new_path = current_path + [neighbour] 
                stack.append(new_path) 
                if neighbour == goal:
                    paths.append(new_path) # add the new path to the list of destination paths
    return min(paths, key=len)

graph = {
    'A' : ['B', 'C'],
    'B' : ['H', 'D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : ['H', 'I'],
    'H' : [],
    'I' : []
}

start = input("Enter start node : ")
goal = input("Enter goal node  : ")
          
print(f"Shortest DFS Path is : {dfsShortestPath(graph)}")

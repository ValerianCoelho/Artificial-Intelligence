def dfs(graph, start, goal):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node == goal: break
            neighbours = graph[node]
            for neighbour in neighbours:
                stack.append(neighbour)
    return visited

start = "A"
goal = "G"
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": [],
}

print("DFS Traversal :", dfs(graph, start, goal))

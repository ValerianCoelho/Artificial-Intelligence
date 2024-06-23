def dfs(graph, start, goal):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node == goal: break
            neighbours = graph[node]
            stack.extend(reversed(neighbours))
    return visited

start = "A"
goal = "E"
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

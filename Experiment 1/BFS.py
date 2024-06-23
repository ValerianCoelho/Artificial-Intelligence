def bfs(tree, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = tree[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited

start = "A"
tree = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": ["F"], "E": ["F"], "F": []}

print("BFS Traversal :",bfs(tree, start))

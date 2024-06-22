def bfs(tree, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbour = tree[node]
            for i in neighbour:
                queue.append(i)
    return visited

start = "A"
tree = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": ["F"], "E": ["F"], "F": []}

print("BFS Traversal ", bfs(tree, start))

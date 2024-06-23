def bfs_goal(tree, start, goal):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            if node == goal: break
            neighbours = tree[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited

start = "A"
goal = "E"
tree = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": ["F"], "E": ["F"], "F": []}

print("BFS (Goal Search) Traversal :", bfs_goal(tree, start, goal))

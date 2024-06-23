def bfs_goal(tree, start, goal):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            if node == goal: break
            neighbour = tree[node]
            for i in neighbour:
                queue.append(i)
    return visited

start = "A"
goal = "E"
tree = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": ["F"], "E": ["F"], "F": []}

print("BFS Goal Traversal ", bfs_goal(tree, start, goal))

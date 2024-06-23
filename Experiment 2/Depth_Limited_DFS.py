def depth_limited_dfs(graph, start, goal, limit):
    def dfs(current_node, goal, visited, depth):

        if current_node == goal:
            return visited
        if depth >= limit:
            return None

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                result = dfs(neighbor, goal, visited + [neighbor], depth + 1)
                if result is not None:
                    return result

        return None

    return dfs(start, goal, [start], 0)


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": [],
}

start = "A"
goal = "G"
depth_limit = 3

visited = depth_limited_dfs(graph, start, goal, depth_limit)
print(f"Visited: {visited}")

def best_first_search(start, goal, graph):
    visited = []
    open = [([start], 0)]  # this is a list of tuples, where each tuple is a path and its cost
    while open:  # when open is empty, the search is over and there is no solution
        print(open)
        path, cost = open.pop(0)
        node = path[-1]  # the current node is the last node in the path
        if node == goal:  # if the current node is the goal, return the path
            return path
        if node not in visited:
            visited.append(node)
            for neighbour, neighbour_heuristic, neighbour_cost in graph[node]:
                new_path = path + [neighbour]
                new_cost = cost + neighbour_cost
                open.append((new_path, new_cost))
            open.sort(key=lambda x: x[1] + neighbour_heuristic)
    return None


start = "S"
goal = "G"

# format: {node: [(neighbour, heuristic, cost)]}
graph = {
    "S": [("A", 6, 1), ("B", 2, 4)],
    "A": [("B", 2, 2), ("C", 1, 5), ("G", 0, 12)],
    "B": [("C", 1, 2)],
    "C": [("G", 0, 3)],
    "G": [],
}

print(best_first_search(start, goal, graph))

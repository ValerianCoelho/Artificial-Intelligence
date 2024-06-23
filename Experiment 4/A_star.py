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
            for neighbour, neighbour_cost in graph[node]:
                new_path = path + [neighbour]
                new_cost = cost + neighbour_cost
                open.append((new_path, new_cost))
            open.sort(key=lambda x: x[1] + heuristic[x[0][-1]])
    return None

start = "S"
goal = "G"

# format: {node: [(neighbour, cost)]}
graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("B", 2), ("C", 5), ("G", 12)],
    "B": [("C", 2)],
    "C": [("G", 3)],
    "G": [],
}
heuristic = {
    "S": 7,
    "A": 6,
    "B": 2,
    "C": 1,
    "G": 0,
}

print(best_first_search(start, goal, graph))

def best_first_search(start, goal, graph):
    visited = []
    open = [[start]]  # this is a list of paths
    while open:  # when open is empty, the search is over and there is no solution
        print(open)
        path = open.pop(0)
        node = path[-1]  # the current node is the last node in the path
        if node == goal:  # if the current node is the goal, return the path
            return path
        if node not in visited:
            visited.append(node)
            for neighbour in graph[node]:
                new_path = path + [neighbour]
                open.append(new_path)
            open.sort(key=lambda x: heuristic[x[-1]])
    return None


start = "A"
goal = "H"

# format: {node: [(neighbour, heuristic)]}
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": ["H"],
    "F": ["H"],
    "G": ["H"],
    "H": []
}
heuristic = {
    "A": 10,
    "B": 12,
    "C": 4,
    "D": 8,
    "E": 7,
    "F": 6,
    "G": 2,
    "H": 0,

}

print(best_first_search(start, goal, graph))

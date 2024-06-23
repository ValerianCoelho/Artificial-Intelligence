
def best_first_search(start, goal, graph):
    visited = []
    open = [([start], 0)] # this is a list of tuples, where each tuple is a path and its heuristic
    while open: # when open is empty, the search is over and there is no solution
        print(open)
        path, heuristic = open.pop(0)
        node = path[-1] # the current node is the last node in the path
        if node == goal: # if the current node is the goal, return the path
            return path
        if node not in visited:
            visited.append(node)
            for neighbour, neighbour_heuristic in graph[node]:
                new_path = path + [neighbour]
                new_heuristic = heuristic + neighbour_heuristic
                open.append((new_path, new_heuristic))
            open.sort(key = lambda x: x[1])
    return None


start = "A"
goal = "H"

graph = {
    'A' : [('B', 12), ('C', 4)],
    'B' : [('D', 8), ('E', 7)],
    'C' : [('F', 6), ('G', 2)],
    'D' : [],
    'E' : [('H', 0)],
    'F' : [('H', 0)],
    'G' : [('H', 0)]
}

print(best_first_search(start, goal, graph))
def three_jug_problem(capacity_a, capacity_b, capacity_c, target_a, target_b):
    visited = set()
    queue = [(0, 0, 0)]
    parent = {(0, 0, 0): None}
    
    while queue:
        state = queue.pop(0)
        a, b, c = state
        
        if a == target_a and b == target_b:
            # To find the path, we backtrack from the current state
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            path.reverse()
            return f"Solution found: {path}"
        
        if state in visited:
            continue
        
        visited.add(state)
        
        # Generate all possible states from the current state
        possible_states = set()
        
        # Fill jugs
        possible_states.add((capacity_a, b, c))
        possible_states.add((a, capacity_b, c))
        possible_states.add((a, b, capacity_c))
        
        # Empty jugs
        possible_states.add((0, b, c))
        possible_states.add((a, 0, c))
        possible_states.add((a, b, 0))
        
        # Pour water between jugs
        # Pour A to B
        pour_a_b = min(a, capacity_b - b)
        possible_states.add((a - pour_a_b, b + pour_a_b, c))
        
        # Pour A to C
        pour_a_c = min(a, capacity_c - c)
        possible_states.add((a - pour_a_c, b, c + pour_a_c))
        
        # Pour B to A
        pour_b_a = min(b, capacity_a - a)
        possible_states.add((a + pour_b_a, b - pour_b_a, c))
        
        # Pour B to C
        pour_b_c = min(b, capacity_c - c)
        possible_states.add((a, b - pour_b_c, c + pour_b_c))
        
        # Pour C to A
        pour_c_a = min(c, capacity_a - a)
        possible_states.add((a + pour_c_a, b, c - pour_c_a))
        
        # Pour C to B
        pour_c_b = min(c, capacity_b - b)
        possible_states.add((a, b + pour_c_b, c - pour_c_b))
        
        for new_state in possible_states:
            if new_state not in visited and new_state not in parent:
                parent[new_state] = state
                queue.append(new_state)
    
    return "No solution found"

# Example usage:
capacity_a = 8
capacity_b = 5
capacity_c = 3
target_a = 4
target_b = 4
result = three_jug_problem(capacity_a, capacity_b, capacity_c, target_a, target_b)
print(result)

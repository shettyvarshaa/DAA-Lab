import itertools
import sys

def tsp(graph):
    num_nodes = len(graph)
    min_cost = sys.maxsize
    optimal_route = []
    
    for perm in itertools.permutations(range(num_nodes)):
        cost = sum(graph[perm[i - 1]][perm[i]] for i in range(num_nodes))
        if cost < min_cost:
            min_cost = cost
            optimal_route = perm
            
    return optimal_route, min_cost

# Example usage
graph = [
    [0, 10, 20, 30],
    [10, 0, 5, 15],
    [20, 5, 0, 8],
    [30, 15, 8, 0]
]

optimal_route, total_cost = tsp(graph)
print("Optimal Route:", optimal_route)
print("Total Cost:", total_cost)

#OUTPUT
'''
    Optimal Route: (0, 1, 2, 3)
    Total Cost: 53
'''
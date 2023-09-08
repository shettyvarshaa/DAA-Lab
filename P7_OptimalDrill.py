import heapq

def optimal_drilling_time(diameters):
    heapq.heapify(diameters)  # Convert list to a min-heap
    
    total_time = 0
    
    while len(diameters) > 1:
        smallest = heapq.heappop(diameters)
        second_smallest = heapq.heappop(diameters)
        
        total_time += smallest + second_smallest
        heapq.heappush(diameters, smallest + second_smallest)
    
    return total_time

# Sample data
hole_diameters = [4, 3, 2, 6]

# Calculate optimal drilling time
time = optimal_drilling_time(hole_diameters)
print(f"Optimal Drilling Time: {time}")

#OUTPUT

'''
    Optimal Drilling Time: 29
'''
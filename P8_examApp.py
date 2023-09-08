from collections import defaultdict
def exam_schedule(subjects, connections):
    graph = defaultdict(list)   
    for sub1, sub2 in connections:
        graph[sub1].append(sub2)
        graph[sub2].append(sub1)    
    color_map = {}
    avail = set(range(1, len(subjects) + 1))
    
    for subject in subjects:
        used = {color_map[neighbour] for neighbour in graph[subject] if neighbour in color_map}
        availa = (avail - used).pop()
        color_map[subject] = availa
    
    return color_map, max(color_map.values())

subjects = ['maths', 'phy', 'chem', 'bio']
connections = [('maths', 'phy'), ('maths', 'chem'), ('maths', 'bio'), ('phy', 'chem'),('phy','bio')]
color_map, color_val = exam_schedule(subjects, connections)
print(color_map)

#OUTPUT

''' 
    {'maths': 1, 'phy': 2, 'chem': 3, 'bio': 3}
'''
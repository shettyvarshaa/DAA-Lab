import sys

def prims(adj_mat):
    num = len(adj_mat)
    key = [sys.maxsize] * num
    parent = [None] * num
    key[0] = 0
    parent[0] = -1
    for _ in range(num):
        u = min((key[v], v) for v in range(num) if not mst_set[v])[1]
        mst_set[u] = True
        for v in range(num):
            if adj_mat[u][v] > 0 and not mst_set[v] and key[v] > adj_mat[u][v]:
                key[v], parent[v] = adj_mat[u][v], u
    mst = []
    for v in range(1, num):
        mst.append((parent[v], v, adj_mat[v][parent[v]]))
    return mst
adj_mat = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]
mst_set = [False] * len(adj_mat)
mst = prims(adj_mat)
print(mst)

#OUTPUT
'''
    [(0, 1, 2), (1, 2, 3), (0, 3, 6), (1, 4, 5)]
'''
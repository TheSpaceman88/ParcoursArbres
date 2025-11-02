from typing import List, Tuple
from graph import Graph

def floyd_warshall(g: Graph) -> Tuple[List[str], List[List[float]]]:
    nodes = list(g.nodes.keys())
    n = len(nodes)
    idx = {u: i for i, u in enumerate(nodes)}
    INF = float("inf")
    D = [[INF] * n for _ in range(n)]
    for i in range(n):
        D[i][i] = 0.0
    for u, nbrs in g.adj.items():
        for v, w in nbrs:
            i, j = idx[u], idx[v]
            if w < D[i][j]:
                D[i][j] = w
    for k in range(n):
        for i in range(n):
            dik = D[i][k]
            if dik == INF:
                continue
            for j in range(n):
                nd = dik + D[k][j]
                if nd < D[i][j]:
                    D[i][j] = nd
    return nodes, D

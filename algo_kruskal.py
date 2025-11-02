from typing import List, Tuple
from graph import Graph, DSU, Edge

def kruskal_mst(g: Graph) -> Tuple[float, List[Edge]]:
    if g.directed:
        raise ValueError("Kruskal requires an undirected graph.")
    dsu = DSU(g.nodes.keys())
    edges = sorted(list(g.edges()), key=lambda e: e.w)
    cost = 0.0
    mst: List[Edge] = []
    for e in edges:
        if dsu.union(e.u, e.v):
            mst.append(e)
            cost += e.w
    return cost, mst

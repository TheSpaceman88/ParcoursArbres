import heapq
from typing import List, Tuple
from graph import Graph, Edge

def prim_mst(g: Graph, start: str) -> Tuple[float, List[Edge]]:
    if g.directed:
        raise ValueError("Prim requires an undirected graph.")
    seen = {start}
    pq = []
    for v, w in g.adj[start]:
        heapq.heappush(pq, (w, start, v))
    mst: List[Edge] = []
    cost = 0.0
    while pq and len(seen) < len(g.nodes):
        w, u, v = heapq.heappop(pq)
        if v in seen:
            continue
        seen.add(v)
        mst.append(Edge(u, v, w))
        cost += w
        for x, wx in g.adj[v]:
            if x not in seen:
                heapq.heappush(pq, (wx, v, x))
    return cost, mst

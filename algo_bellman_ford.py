from typing import Dict, Tuple
from graph import Graph

def bellman_ford(g: Graph, src: str) -> Tuple[Dict[str, float], bool]:
    nodes = list(g.nodes.keys())
    dist = {u: float("inf") for u in nodes}
    dist[src] = 0.0
    for _ in range(len(nodes) - 1):
        updated = False
        for e in g.edges():
            if dist[e.u] + e.w < dist[e.v]:
                dist[e.v] = dist[e.u] + e.w
                updated = True
            if not g.directed and dist[e.v] + e.w < dist[e.u]:
                dist[e.u] = dist[e.v] + e.w
                updated = True
        if not updated:
            break
    neg_cycle = False
    for e in g.edges():
        if dist[e.u] + e.w < dist[e.v]:
            neg_cycle = True
            break
    return dist, neg_cycle

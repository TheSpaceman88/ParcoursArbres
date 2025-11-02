import heapq
from typing import Dict, Tuple, List
from graph import Graph

def dijkstra(g: Graph, src: str) -> Tuple[Dict[str, float], Dict[str, str]]:
    dist = {n: float("inf") for n in g.nodes}
    prev: Dict[str, str] = {}
    dist[src] = 0.0
    pq: List[Tuple[float, str]] = [(0.0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in g.adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))
    return dist, prev

def reconstruct_path(prev: Dict[str, str], src: str, dst: str) -> List[str]:
    if src == dst:
        return [src]
    if dst not in prev:
        return []
    path = [dst]
    while path[-1] != src:
        path.append(prev[path[-1]])
    path.reverse()
    return path

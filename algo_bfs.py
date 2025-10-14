from collections import deque
from typing import List
from graph import Graph

def bfs(g: Graph, start: str) -> List[str]:
    seen = {start}
    q = deque([start])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v, _ in g.adj[u]:
            if v not in seen:
                seen.add(v)
                q.append(v)
    return order

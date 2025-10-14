from typing import List
from graph import Graph

def dfs(g: Graph, start: str) -> List[str]:
    seen, order = set(), []
    def rec(u: str):
        seen.add(u)
        order.append(u)
        for v, _ in g.adj[u]:
            if v not in seen:
                rec(v)
    rec(start)
    return order

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Iterable, Any

Weight = float

@dataclass
class Node:
    id: str
    data: dict = field(default_factory=dict)

@dataclass(frozen=True)
class Edge:
    u: str
    v: str
    w: Weight = 1.0

class Graph:
    def __init__(self, directed: bool = False):
        self.directed = directed
        self.nodes: Dict[str, Node] = {}
        self.adj: Dict[str, List[Tuple[str, Weight]]] = {}

    def add_node(self, node_id: str, **data: Any) -> None:
        if node_id not in self.nodes:
            self.nodes[node_id] = Node(node_id, data)
            self.adj[node_id] = []
        else:
            self.nodes[node_id].data.update(data)

    def add_edge(self, src: str, dst: str, weight: Weight = 1.0) -> None:
        if src not in self.nodes: self.add_node(src)
        if dst not in self.nodes: self.add_node(dst)
        self.adj[src].append((dst, weight))
        if not self.directed:
            self.adj[dst].append((src, weight))

    def edges(self) -> Iterable[Edge]:
        if self.directed:
            for u, nbrs in self.adj.items():
                for v, w in nbrs:
                    yield Edge(u, v, w)
        else:
            seen = set()
            for u, nbrs in self.adj.items():
                for v, w in nbrs:
                    key = tuple(sorted((u, v)))
                    if key in seen: 
                        continue
                    seen.add(key)
                    yield Edge(u, v, w)

    # Utils arbre (optionnels)
    def is_connected(self) -> bool:
        if not self.nodes:
            return True
        start = next(iter(self.nodes))
        seen, stack = set(), [start]
        while stack:
            u = stack.pop()
            if u in seen: 
                continue
            seen.add(u)
            for v, _ in self.adj[u]:
                if v not in seen:
                    stack.append(v)
        return len(seen) == len(self.nodes)

    def is_tree_undirected(self) -> bool:
        if self.directed:
            return False
        V = len(self.nodes)
        E = sum(len(nbrs) for nbrs in self.adj.values()) // 2
        return self.is_connected() and E == V - 1

class DSU:
    def __init__(self, items: Iterable[str]):
        self.parent = {x: x for x in items}
        self.rank = {x: 0 for x in items}
    def find(self, x: str) -> str:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, a: str, b: str) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb: return False
        if self.rank[ra] < self.rank[rb]: ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]: self.rank[ra] += 1
        return True

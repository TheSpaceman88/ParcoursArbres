````markdown
# Base propre et flexible pour un graphe en Python

```python
from dataclasses import dataclass, field
from typing import Dict, List, Tuple

@dataclass
class Node:
    id: str
    data: dict = field(default_factory=dict)

@dataclass
class Graph:
    nodes: Dict[str, Node] = field(default_factory=dict)
    adj: Dict[str, List[Tuple[str, float]]] = field(default_factory=dict)
    directed: bool = False

    def add_node(self, node_id: str, **data):
        if node_id not in self.nodes:
            self.nodes[node_id] = Node(node_id, data)
            self.adj[node_id] = []

    def add_edge(self, src: str, dst: str, weight: float = 1.0):
        if src not in self.nodes: self.add_node(src)
        if dst not in self.nodes: self.add_node(dst)
        self.adj[src].append((dst, weight))
        if not self.directed:
            self.adj[dst].append((src, weight))
````

👉 Tes algorithmes (BFS, Dijkstra, etc.) ne dépendront que du dictionnaire `adj`.
Les objets `Node` te servent simplement à stocker des **métadonnées** (position, type, couleur, capacité, etc.).

---

## 🧭 Exemple d’utilisation

```python
g = Graph()
g.add_edge("A", "B", 5)
g.add_edge("A", "C", 2)
g.add_edge("B", "D", 4)
g.add_edge("C", "D", 1)
```

```
```

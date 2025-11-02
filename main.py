from graph import Graph
from algo_bfs import bfs
from algo_dfs import dfs
from algo_dijkstra import dijkstra, reconstruct_path
from algo_bellman_ford import bellman_ford
from algo_kruskal import kruskal_mst
from algo_prim import prim_mst
from algo_floyd_warshall import floyd_warshall


def build_france_graph(undirected: bool = True) -> Graph:
    g = Graph(directed=not undirected)
    g.add_edge("Rennes", "Caen", 75)
    g.add_edge("Rennes", "Nantes", 45)
    g.add_edge("Rennes", "Paris", 110)
    g.add_edge("Nantes", "Paris", 80)
    g.add_edge("Nantes", "Bordeaux", 90)
    g.add_edge("Bordeaux", "Paris", 150)
    g.add_edge("Bordeaux", "Lyon", 100)
    g.add_edge("Caen", "Paris", 50)
    g.add_edge("Caen", "Lille", 65)
    g.add_edge("Paris", "Lille", 70)
    g.add_edge("Paris", "Dijon", 60)
    g.add_edge("Paris", "Nancy", 120)
    g.add_edge("Dijon", "Lyon", 70)
    g.add_edge("Dijon", "Nancy", 75)
    g.add_edge("Dijon", "Grenoble", 90)
    g.add_edge("Lyon", "Grenoble", 40)
    g.add_edge("Lyon", "Nancy", 75)
    g.add_edge("Nancy", "Grenoble", 80)
    return g

if __name__ == "__main__":
    g_u = build_sample_graph(undirected=True)

    print("BFS Rennes:", bfs(g_u, "Rennes"))
    print("DFS Rennes:", dfs(g_u, "Rennes"))

    dist, prev = dijkstra(g_u, "Rennes")
    print("Dijkstra dist:", dist)
    print("Path Rennes->Lyon:", reconstruct_path(prev, "Rennes", "Lyon"))

    dist_bf, neg = bellman_ford(g_u, "Rennes")
    print("Bellman-Ford dist:", dist_bf, "neg_cycle:", neg)

    cost_k, mst_k = kruskal_mst(g_u)
    print("Kruskal cost:", cost_k, "edges:", mst_k)

    cost_p, mst_p = prim_mst(g_u, "Rennes")
    print("Prim cost:", cost_p, "edges:", mst_p)

    nodes, D = floyd_warshall(g_u)
    print("FW nodes:", nodes)
    for i, row in enumerate(D):
        print(nodes[i], row)

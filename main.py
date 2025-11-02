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
    g_u = build_france_graph(undirected=True)

    print("\n" + "="*40)
    print("BFS (Parcours en largeur)")
    print("="*40)
    print("Départ : Rennes")
    print("Ordre de visite :", bfs(g_u, "Rennes"))

    print("\n" + "="*40)
    print("DFS (Parcours en profondeur)")
    print("="*40)
    print("Départ : Rennes")
    print("Ordre de visite :", dfs(g_u, "Rennes"))

    print("\n" + "="*40)
    print("Dijkstra (Plus court chemin pondéré)")
    print("="*40)
    dist, prev = dijkstra(g_u, "Rennes")
    print("Distances depuis Rennes :")
    for k, v in dist.items():
        print(f"  {k:<10} → {v}")
    path = reconstruct_path(prev, "Rennes", "Lyon")
    print("\nChemin Rennes → Lyon :", " → ".join(path))

    print("\n" + "="*40)
    print("Bellman-Ford (Chemins pondérés / négatifs)")
    print("="*40)
    dist_bf, neg = bellman_ford(g_u, "Rennes")
    for k, v in dist_bf.items():
        print(f"  {k:<10} → {v}")
    print(f"\nCycle négatif détecté : {'Oui' if neg else 'Non'}")

    print("\n" + "="*40)
    print("Kruskal (Arbre couvrant minimal)")
    print("="*40)
    cost_k, mst_k = kruskal_mst(g_u)
    print(f"Coût total : {cost_k}")
    print("Arêtes sélectionnées :")
    for e in mst_k:
        print(f"  {e.u} - {e.v} ({e.w})")

    print("\n" + "="*40)
    print("Prim (Arbre couvrant minimal)")
    print("="*40)
    cost_p, mst_p = prim_mst(g_u, "Rennes")
    print(f"Coût total : {cost_p}")
    print("Arêtes sélectionnées :")
    for e in mst_p:
        print(f"  {e.u} - {e.v} ({e.w})")

    print("\n" + "="*40)
    print("Floyd-Warshall (Tous les plus courts chemins)")
    print("="*40)
    nodes, D = floyd_warshall(g_u)
    print("Matrice des distances :\n")
    header = "      " + "  ".join(f"{n:>8}" for n in nodes)
    print(header)
    for i, row in enumerate(D):
        line = f"{nodes[i]:>6} " + " ".join(f"{d:8.1f}" if d != float('inf') else "     ∞" for d in row)
        print(line)


from graph import Graph
from main import build_france_graph
from algo_bfs import bfs
from algo_dijkstra import dijkstra, reconstruct_path
from algo_kruskal import kruskal_mst
import json

def export_interactive_graph(graph: Graph, output="graph_interactif.html"):
    # --- Conversion du graphe ---
    nodes = [{"id": n, "label": n} for n in graph.nodes]
    edges = []
    added = set()
    for u, nbrs in graph.adj.items():
        for v, w in nbrs:
            if not graph.directed and (v, u) in added:
                continue
            added.add((u, v))
            edges.append({"from": u, "to": v, "label": str(w), "color": "gray"})

    # --- Pré-calcul des chemins (pour éviter d’appeler Python depuis JS) ---
    bfs_path = bfs(graph, "Paris")
    dist, prev = dijkstra(graph, "Paris")
    dijkstra_path = reconstruct_path(prev, "Paris", "Grenoble")
    cost, mst_edges = kruskal_mst(graph)
    kruskal_edges = [(e.u, e.v) for e in mst_edges]

    html = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>Graphe interactif - Algo</title>
  <script src="https://unpkg.com/vis-network@9.1.2/dist/vis-network.min.js"></script>
  <link href="https://unpkg.com/vis-network@9.1.2/styles/vis-network.min.css" rel="stylesheet" />
  <style>
    body {{ font-family: Arial, sans-serif; text-align:center; }}
    #mynetwork {{ width: 100%; height: 85vh; border: 1px solid lightgray; margin-top:10px; }}
    button {{ margin: 5px; padding: 10px 15px; font-weight: bold; }}
  </style>
</head>
<body>
  <h2>Visualisation des algorithmes de graphe</h2>
  <div>
    <button onclick="runBFS()">BFS (Largeur)</button>
    <button onclick="runDijkstra()">Dijkstra</button>
    <button onclick="runKruskal()">Kruskal (MST)</button>
    <button onclick="resetColors()">Réinitialiser</button>
  </div>
  <div id="mynetwork"></div>

  <script>
    const nodes = new vis.DataSet({json.dumps(nodes)});
    const edges = new vis.DataSet({json.dumps(edges)});
    const container = document.getElementById('mynetwork');
    const network = new vis.Network(container, {{nodes, edges}}, {{
      edges: {{ font: {{ align: 'middle' }}, smooth: true }},
      nodes: {{ color: {{ background: '#9ecfff', border: '#555' }}, shape: 'ellipse' }},
      physics: {{ stabilization: true }}
    }});

    const bfsPath = {json.dumps(bfs_path)};
    const dijkstraPath = {json.dumps(dijkstra_path)};
    const kruskalEdges = {json.dumps(kruskal_edges)};

    function colorEdges(pathNodes, color) {{
      const allEdges = edges.get();
      for (let e of allEdges) {{
        e.color = 'gray';
        if (pathNodes) {{
          for (let i = 0; i < pathNodes.length - 1; i++) {{
            const a = pathNodes[i], b = pathNodes[i+1];
            if ((e.from === a && e.to === b) || (e.from === b && e.to === a)) {{
              e.color = color;
            }}
          }}
        }}
      }}
      edges.update(allEdges);
    }}

    function runBFS() {{
      colorEdges(bfsPath, 'orange');
      alert('BFS depuis Paris :\\n' + bfsPath.join(' → '));
    }}

    function runDijkstra() {{
      colorEdges(dijkstraPath, 'red');
      alert('Dijkstra Paris → Grenoble :\\n' + dijkstraPath.join(' → '));
    }}

    function runKruskal() {{
      const allEdges = edges.get();
      for (let e of allEdges) {{
        e.color = kruskalEdges.some(([a,b]) =>
          (e.from === a && e.to === b) || (e.from === b && e.to === a)
        ) ? 'green' : 'gray';
      }}
      edges.update(allEdges);
      alert('Kruskal : arbre couvrant minimal surligné en vert');
    }}

    function resetColors() {{
      const allEdges = edges.get();
      for (let e of allEdges) e.color = 'gray';
      edges.update(allEdges);
    }}
  </script>
</body>
</html>
"""
    with open(output, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Fichier généré : {output}")

if __name__ == "__main__":
    g = build_france_graph()
    export_interactive_graph(g)


```markdown
# Projet : Visualisation d’algorithmes de graphes

Ce projet met en œuvre et visualise plusieurs **algorithmes fondamentaux sur les graphes** à l’aide de **Python** et d’une **interface web interactive**.

---

## Sommaire
1. [Description du projet](#-description-du-projet)
2. [Algorithmes implémentés](#-algorithmes-implémentés)
3. [Structure du projet](#-structure-du-projet)
4. [Installation](#-installation)
5. [Utilisation](#-utilisation)
6. [Résultats](#-résultats)
7. [Améliorations possibles](#-améliorations-possibles)
8. [Auteur](#-auteur)

---

## Description du projet

L’objectif du projet est de comparer et illustrer différents **algorithmes de parcours et d’optimisation** sur un graphe représentant un réseau de **villes françaises** connectées par des routes pondérées.

Les calculs sont effectués en **Python**, tandis que les résultats peuvent être **visualisés directement dans le navigateur** via un fichier HTML interactif utilisant **Vis.js**.

---

## Algorithmes implémentés

| Algorithme | Type | Description | Web |
|-------------|------|--------------|------|
| **BFS** (*Breadth-First Search*) | Parcours | Explore le graphe en largeur | ✅ |
| **DFS** (*Depth-First Search*) | Parcours | Explore le graphe en profondeur | ❌ |
| **Dijkstra** | Chemin minimal | Plus court chemin pondéré sans poids négatifs | ✅ |
| **Kruskal** | Arbre couvrant minimal | Relie tous les sommets avec un coût minimal | ✅ |
| **Prim** | Arbre couvrant minimal | Variante de Kruskal partant d’un sommet | ❌ |
| **Bellman-Ford** | Chemins pondérés | Gère les poids négatifs | ❌ |
| **Floyd-Warshall** | Tous chemins | Trouve tous les plus courts chemins entre paires | ❌ |

✅ = disponible dans la version web  
❌ = implémenté en Python uniquement

---

## Structure du projet

```

/ParcoursArbres
├── graph.py                # Définition du graphe et structures de données
├── algo_bfs.py             # BFS
├── algo_dfs.py             # DFS
├── algo_dijkstra.py        # Dijkstra
├── algo_kruskal.py         # Kruskal
├── algo_prim.py            # Prim
├── algo_bellman_ford.py    # Bellman-Ford
├── algo_floyd_warshall.py  # Floyd-Warshall
├── main.py                 # Tests console (avec mise en forme lisible)
├── gui_html.py             # Génération du graphe interactif en HTML
└── graph_interactif.html   # Fichier généré, à ouvrir dans le navigateur

````

---

## Installation

Aucune dépendance externe nécessaire pour la version web.  
Python ≥ 3.10 suffit.


## Utilisation

### 🔹 1. Exécution console

Lancez :

```bash
python main.py
```

Vous verrez dans la console un affichage clair :

```
BFS (Parcours en largeur)
DFS (Parcours en profondeur)
Dijkstra (Plus court chemin)
Bellman-Ford (Poids négatifs)
Kruskal (MST)
Prim (MST)
Floyd-Warshall (Tous chemins)
```

---

### 2. Génération de l’interface web

```bash
python gui_html.py
```

Cela crée le fichier :

```
graph_interactif.html
```

Ouvrez-le dans votre navigateur pour :

* déplacer les nœuds,
* zoomer sur le graphe,
* cliquer sur les boutons :

  * **BFS** → parcours en largeur
  * **Dijkstra** → plus court chemin
  * **Kruskal** → arbre couvrant minimal
  * **Réinitialiser** → restaure les couleurs

---

## Résultats observés

Exemple de sortie :

* **BFS (Rennes)** → exploration des villes couche par couche.
* **Dijkstra (Rennes → Lyon)** → chemin le plus court : `Rennes → Paris → Dijon → Lyon`.
* **Kruskal** → arbre couvrant minimal totalisant environ **640 unités**.

Les chemins apparaissent :

* 🟠 en **orange** pour BFS,
* 🔴 en **rouge** pour Dijkstra,
* 🟢 en **vert** pour Kruskal.

---

## Améliorations possibles

* Intégrer DFS, Prim, Bellman-Ford et Floyd-Warshall à la version web.
* Ajouter la sélection dynamique du **nœud de départ/arrivée** directement dans l’interface.
* Comparer les **temps d’exécution** des algorithmes.
* Ajouter des **statistiques graphiques** (longueur moyenne, coût total, etc.).

---

## Auteurs

**Nom :** Sarah ARNAUD & Alexandre POISSONNEAU
**Groupe :** I1 APP LSI 1
**Projet :** Algorithmes et théorie des Graphes


def bfs(G, s):
    couleur = {s: 'vert' for s in G}
    P = {}
    P[s] = None
    couleur[s] = 'orange'
    Q = [s]
    while Q:
        u = Q.pop(0)
        for v in G[u]:
            if couleur[v] == 'vert':
                couleur[v] = 'orange'
                P[v] = u
                Q.append(v)
        couleur[u] = 'rouge'
    print("{")
    for node, parent in P.items():
        print(f"    '{node}': '{parent}',")
    print("}")

graphe = {
    'a': ['b', 'c'],
    'b': ['a', 'd'],
    'c': ['a', 'e'],
    'd': ['b', 'f'],
    'e': ['c'],
    'f': ['d']
}

bfs(graphe, 'd')


#bfs croissant
def bfs_croissant(G, s):
    P = {}  # Dictionnaire des parents
    P[s] = None  # La racine n'a pas de parents
    Q = [s]  # File pour stocker les sommets à visiter
    visited = []  # Liste pour stocker les sommets visités dans l'ordre croissant

    while Q:
        u = Q.pop(0)  # Retirer le premier sommet de la file (BFS)
        visited.append(u)  # Ajouter le sommet visité à la liste
        for v in G[u]:  # Parcours des voisins dans l'ordre croissant
            if v not in P:  # Si le voisin n'a pas été visité
                P[v] = u  # Enregistrer le parent du voisin v comme étant le sommet u
                Q.append(v)  # Ajouter le voisin à la file pour le visiter ensuite

    return P, visited


# bfs decroissant

def bfs_decroissant(G, s):
    P = {}  # Dictionnaire des parents
    P[s] = None  # La racine n'a pas de parents
    Q = [s]  # File pour stocker les sommets à visiter
    visited = []  # Liste pour stocker les sommets visités dans l'ordre décroissant

    while Q:
        u = Q.pop(0)  # Retirer le premier sommet de la file (BFS)
        visited.append(u)  # Ajouter le sommet visité à la liste
        for v in reversed(G[u]):  # Parcours des voisins en ordre décroissant
            if v not in P:  # Si le voisin n'a pas été visité
                P[v] = u  # Enregistrer le parent du voisin v comme étant le sommet u
                Q.append(v)  # Ajouter le voisin à la file pour le visiter ensuite

    return P, visited[::-1]  # Inverser l'ordre de la liste pour avoir l'ordre décroissant


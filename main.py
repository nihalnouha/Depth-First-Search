# def dfs(G, s):
#     couleur = {s: 'vert' for s in G}  # couleur des sommets
#     P = {}  # dictionnaire des peres
#     P[s] = None  # la racine n'a pas de peres
#     couleur[s] = 'orange'  # on passe la racine à orange
#     Q = [s]  # Premier elt de la pile
#     while Q:
#         u = Q[-1]
#         R = [y for y in G[u] if couleur[y] == 'vert']
#         if R:
#             v = R[0]
#             couleur[v] = 'orange'
#             P[v] = u
#             Q.append(v)
#         else:
#             Q.pop()
#             couleur[u] = 'rouge'
#     return P





# graphe = {
#     'a': ['b', 'c'],
#     'b': ['a', 'd'],
#     'c': ['a', 'e'],
#     'd': ['b', 'f'],
#     'e': ['c'],
#     'f': ['d']
# }

# P=dfs(graphe,'d')
# print(P)


def dfs_croissant(G, s):
    couleur = {s: 'vert' for s in G}  # couleur des sommets
    P = {}  # dictionnaire des parents
    P[s] = None  # la racine n'a pas de peres
    couleur[s] = 'orange'  # on passe la racine à orange
    Q = [s]  # Premier elt de la pile
    visited = []  # Liste pour stocker les sommets visités dans l'ordre croissant

    while Q:
        u = Q.pop()  # Retirer le sommet u de la pile
        visited.append(u)  # Ajouter le sommet u à la liste des sommets visités dans l'ordre croissant
        for v in G[u]:
            if couleur[v] == 'vert':  # Si le voisin n'a pas été visité
                couleur[v] = 'orange'  # Marquer le voisin v comme en cours de traitement
                P[v] = u  # Enregistrer le parent du voisin v comme étant le sommet u
                Q.append(v)  # Ajouter le voisin v à la pile pour le visiter ensuite
        couleur[u] = 'rouge'  # Marquer le sommet u comme complètement traité

    return P, visited

graphe_numerique = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2, 6],
    5: [3],
    6: [4]
}

g= {
    "a":["b","c","D"],
    "b" :["a","e"],
    "c" :["a","b"],
    "D" :["a","e"],
    "e" :["D","f"],
    "f" :["e"]
}
graph_difficile = {
    '1': ['2', '6'],
    '2': ['1', '3', '7'],
    '3': ['2', '4', '8'],
    '4': ['3', '5', '9'],
    '5': ['4', '8'],
    '6': ['1', '10'],
    '7': ['2', '11'],
    '8': ['3', '5', '9', '12'],
    '9': ['4', '8'],
    '10': ['6', '11'],
    '11': ['7', '10'],
    '12': ['8']
}


P, visited_croissant = dfs_croissant(graphe_numerique, 1)  # 1 est le sommet de départ
print("Parcours DFS en ordre croissant:", visited_croissant)



def dfs_decroissant(G, s):
    couleur = {s: 'vert' for s in G}  # couleur des sommets
    P = {}  # dictionnaire des parents
    P[s] = None  # la racine n'a pas de peres
    couleur[s] = 'orange'  # on passe la racine à orange
    Q = [s]  # Premier elt de la pile
    visited = []  # Liste pour stocker les sommets visités dans l'ordre décroissant

    while Q:
        u = Q.pop()  # Retirer le sommet u de la pile
        visited.append(u)  # Ajouter le sommet u à la liste des sommets visités
        for v in reversed(G[u]):  # Parcourir les voisins en ordre inverse
            if couleur[v] == 'vert':  # Si le voisin n'a pas été visité
                couleur[v] = 'orange'  # Marquer le voisin v comme en cours de traitement
                P[v] = u  # Enregistrer le parent du voisin v comme étant le sommet u
                Q.append(v)  # Ajouter le voisin v à la pile pour le visiter ensuite
        couleur[u] = 'rouge'  # Marquer le sommet u comme complètement traité

    return P, visited[::-1]  # renverser la liste pour obtenir l'ordre décroissant

P, visited_decroissant = dfs_decroissant(g, 'a')  # 1 est le sommet de départ
print("Parcours DFS en ordre décroissant:", visited_decroissant)

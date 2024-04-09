from collections import deque

def lrg_dec(graph, debut):
    visited = set() 
    file = deque([debut]) # on me notre sommet au debut de la file 
    visited.add(debut) # et on l'ajoute dans la list des noeud visiter

    while file : # tant que la file n'est pas vide
        
        # defiler le premier noeud et l'ajouter a notre parcour
        noeud = file.popleft() 
        print(noeud, end=' ') 
 #enfiler les voisins de le neoud traiter 
        for voisin in graph[noeud]: 
                if voisin not in visited: # si il n'est pas visiter on l'ajoute dans la file 
                    file.append(voisin)
                    visited.add(voisin)

    # Verifier si tous les neoud sont visiter 
    for noeud in graph:
        if noeud not in visited:
            print(noeud, end=' ')

def rev(graph):
    graph = dict(reversed(list(graph.items())))
    for key in graph:
        graph[key] = graph[key][::-1]
    return graph


# Example usage
graph = {
    '1': ['2', '4', '5'],
    '2': ['3', '4'],
    '3': ['1'],
    '4': ['3'],
    '5': ['4'],
    '6': ['8'],
    '7': ['5'],
    '8': ['6', '7']
}
graph2 = {
     0 : [1],
    1 : [4,5], 
    2 : [0, 3],
    3 : [1, 7], 
    4 : [], 
    5 : [7], 
    6 : [3], 
    7 : [5,6,8],
    8 : [5]   
    
}
graphe_numerique = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2, 6],
    5: [3],
    6: [4]
}

graph3 = {
    1 : [3], 
    2 : [4, 8, 9],
    3 : [5, 6], 
    4 : [5, 8], 
    5 : [3, 8], 
    6 : [5, 4], 
    7 : [1, 2, 3, 4, 6], 
    8 : [10], 
    9 : [7], 
    10 : [2, 9]   
}
g = {
    "A":["b","c","e"],
    "b" :["D","f"],
    "c" :["g"],
    "D" :[],
    "e" :["f"],
    "f" :[],
    "g": []
}
graph_difficile = {
   1 :[2,4,5],
   2:[4],
   3:[1],
   4:[3],
   5:[4],
   6:[7,8],
   7:[5],
   8:[6]
}
# Call BFS starting from each unvisited node
print("Parcour en largeur :")
graph = rev(graph_difficile)
lrg_dec(graph, 1)
from collections import deque # Le module deque est utilisé pour créer une file "FIFO"

def lrg(graph, debut):
    visited = set() # Un ensemble pour suivre les nœuds déjà visités.
    file = deque([debut]) # on ajoute sommet au debut de la file 
    visited.add(debut) # et on l'ajoute dans la list des noeud visiter

    while file : # tant que la file n'est pas vide
        
        # defiler le premier noeud et l'ajouter a notre parcour
        noeud = file.popleft() # Le premier nœud de la file est retiré par file.popleft(), et il est ajouté à la liste des sommets visités.
        print(noeud, end=' ') 
#enfiler les voisins de le noeud traiter 
        for voisin in graph[noeud]: 
                if voisin not in visited: # si il n'est pas visiter on l'ajoute dans la file 
                    file.append(voisin)
                    visited.add(voisin)

    # Apres que la file est vide on verifier si tous les noeuds sont visiter 
    for noeud in graph:
        if noeud not in visited:
            print(noeud, end=' ')

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
graph3 = {
    1 : [3], 
    2 : [4, 8, 9],
    3 : [5, 6], 
    4 : [5, 8], 
    5 : [3, 8], 
    6 : [5, 4], 
    7 : [2, 3, 4, 6], 
    8 : [10], 
     9 : [7], 
    10 : [2, 9]
    
    
    
}
graphe_numerique = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2, 6],
    5: [3],
    6: [4]
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
print("parcour en largeur croissant")
lrg(graph_difficile, 1)


# Une liste utilisée comme pile pour suivre les sommets à explorer. Les sommets sont empilés lorsqu'ils sont visités et défilés lorsqu'ils sont explorés
pile = []
parcour = list() # Une liste utilisée pour stocker l'ordre des sommets visités pendant le parcours.

def pfr_cr(graph, debut):
    
    # empiler le sommet
    pile.append(debut) 
    
    
    #tester si le noeud n'est pas dans la pile ou si il n'a pas de successeur 
    for noeud in graph[debut]:
        if ( noeud not in pile) or (len(graph[noeud])==0):
            pfr_cr(graph, noeud) # si oui on appel la fonction dont le debut est le noeud 
    
    resultat = pile.pop() # depiler la dernier element 
    if resultat not in parcour: # tester si l'element existe dans le parcours
        parcour.append(resultat) # on l'ajoute dans le parcour
    
    #tester si la pile est vide
    if not pile :
        for i in graph:
            if i not in parcour : # verifier si tous les noeud est dans le parcours, si non on appel reccursivement de la fonction
                pfr_cr(graph, i)
    return parcour


graph = {
    '1': ['2', '4', '5'],
    '2': ['3', '4'],
    '3': ['1'],
    '4': [],
    '5': ['4'],
    '6': ['8'],
    '7': ['5'],
    '8': ['6', '7']
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
graphe_numerique = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2, 6],
    5: [3],
    6: [4]
}

print("Le parcour est :", pfr_cr(graph_difficile, 1))

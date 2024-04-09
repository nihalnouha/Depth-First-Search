pile = []
parcour = list() 

def pfr_dec(graph, debut):
    
    # empiler le sommet
    pile.append(debut) 
    
    #tester si le noeud n'est pas dans la pile ou si il n'a pas de successeur 
    for noeud in graph[debut]:
        if ( noeud not in pile) or (len(graph[noeud])==0):
            pfr_dec(graph, noeud) # si oui on appel la fonction dont le debut est le neoud 
    
    resultat = pile.pop() # depiler la dernier element 
    if resultat not in parcour: # tester si l'element existe dans le parcours
        parcour.append(resultat) # on l'ajoute dans le parcour
    
    #tester si la pile est vide
    if not pile :
        for i in graph:
            if i not in parcour : # verifier si tous les noeud est dans le parcours, si non on appel la fonction
                pfr_dec(graph, i)
    return parcour

def rev(graph):
    graph = dict(reversed(list(graph.items()))) # . Cela inverse l'ordre des paires clé-valeur du dictionnaire
    #ce qui revient à inverser les associations sommet-liste de successeurs
    for key in graph:
        graph[key] = graph[key][::-1]
    return graph
        
        
#Le graph 
graph = {
    "1": ["2", "4", "5"],
    "2": ["3", "4"],
    "3": ["1"],
    "4": ["3"],
    "5": ["4"],
    "6": ["7","8"],
    "7": ["5"],
    "8": ["4","6", "7"]
}
g= {
    "a":["b","c","D"],
    "b" :["a","e"],
    "c" :["a","b"],
    "D" :["a","e"],
    "e" :["D","f"],
    "f" :["e"]
}
graphe_numerique = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2, 6],
    5: [3],
    6: [4]
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
graph = rev(graph_difficile)
print("Le parcour est :", pfr_dec(graph, 1))

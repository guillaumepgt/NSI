#
# Chapitre 8 - Exercices Newbie 2 et 3
#

""" 
    #Génération des graphes d'exemple
    
    On pourra tester les fonctions [calcul de densité, graphe non-orienté] 
    avec les exemples contenus dans les variables `exemple_liste_X` et 
    `exemple_matrice_X` du fichier `graphes_newbie.py`. 
    Les graphe décrit dans `exemple_liste_1` est le même que dans 
    `exemple_matrice_1`, et ainsi de suite. 
"""

from random import sample, randint

# Définition et génération des graphes exemples
# Ce code n'a pas besoin d'être étudié par les élèves
#
orientes   = [ False,  True,  True, False, True, True ]
nb_sommets = [    10,   300,   100,   100,  200,  200 ]
densites   = [    .9,    .2,     1,     1,   .5,   .7 ]

graphes_exemples = []

for oriente, sommets, densite in zip( orientes, 
                                      nb_sommets, 
                                      densites ):
    
    # print(f"{oriente=},\t{sommets} sommets,\t{densite=}")
    
    sommets = { f"S{s}" for s in range(sommets) }
    liste = {s: [] for s in sommets}
    _densite = densite/2 if (not oriente) else densite
    
    for s in sommets:
        
        if densite == 1:
            liste[s] += list(sommets - {s})
            
        else:
            
            jeu_sommets = sommets - set(liste[s]) - {s}

            # print(f"{len(sommets)=}, {len(jeu_sommets)=}, {int(round(len(sommets)*_densite))=}")

            voisins = sample( jeu_sommets, 
                              min( int(round(len(sommets) * _densite)),
                                   len(jeu_sommets) 
                                 ) 
                            )
            
            liste[s] += voisins

        if not oriente and densite < 1:
            for v in voisins: 
                if s not in liste[v]:
                    liste[v].append(s)
            
    matrice = { s1: {s2: (s2 in liste[s1]) for s2 in sommets} for s1 in sommets }
    
    graphes_exemples.append( (liste, matrice) )
    
exemple_liste_1, exemple_matrice_1 = graphes_exemples[0]
exemple_liste_2, exemple_matrice_2 = graphes_exemples[1]
exemple_liste_3, exemple_matrice_3 = graphes_exemples[2]
exemple_liste_4, exemple_matrice_4 = graphes_exemples[3]
exemple_liste_5, exemple_matrice_5 = graphes_exemples[4]
exemple_liste_6, exemple_matrice_6 = graphes_exemples[5]

def densite(graphe):
    A, S =0, 0
    for sommet in graphe:
        S+=1
        A+=len(sommet)
    return A/(S*(S+1))

print(densite([[1,2,3],[0],[0,3]]))
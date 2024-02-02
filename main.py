import numpy as np
import random as rnd
import copy as cp

# Dimension de la grille
n=2
m=2

Herbe = 0
Mouton=1
Loup=2

#La grille contient des listes d'animaux
Grille   = [[[] for k in range(m)]for i in range(n)]
Grille_2 = [[[] for k in range(m)]for i in range(n)]



class Animal :
    def __init__(self,espece,energie):
        self.energie = energie
        self.espece =espece
        
    def depense(self):
        if self.energie > 0 :
            self.energie -= 1
        

def deplace_animaux() :

    for i in range(n):
        for j in range(m):
            Grille_2[i][j] =[]
            
    for i in range(n):
        for j in range(m):
            for animal in Grille[i][j]:
                dx = rnd.randint(-1,1)
                dy = rnd.randint(-1,1)
                
                x= min (max (i+dx,0), n-1)
                y= min (max (j+dy,0), m-1)
                Grille_2[x][y].append(animal)
    return Grille_2
    

def mange_animaux(chaine_alimentaire):
    for i in range(n):
        for j in range(m):

            
            liste_animaux = Grille[i][j]
            #On trie la liste d'animaux par espèce croissante
            liste_animaux = liste_animaux.sort(key = lambda animal : -animal.espece)
            chaine_alimentaire(liste_animaux)

def chaine_alimentaire(liste_animaux) :
    # L'animal n'a aucune capture, il cherche une proie
    for animal in liste_animaux :
        capture = None
        for proie in liste_animaux :
            if proie.espece == animal.espece -1 :
                capture = proie
                break
        if proie != None:
            animal.energie += 16
            liste_animaux.remove(proie)

    return
        


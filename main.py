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
    Grille = cp.deepcopy(Grille_2)


Grille[0][0].append(Animal(Loup, 5, (0,0)))
Grille=deplace_animaux()

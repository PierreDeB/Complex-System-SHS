import numpy as np
import random as rnd
import copy as cp
import test_proie_predateur

# Dimension de la grille
n=2
m=2

Vide = -1
Herbe = 0
Mouton=1
Loup=2

#La grille contient des listes d'animaux
Grille   = [[[] for k in range(m)]for i in range(n)]



class Animal :
    def __init__(self,espece,energie):
        self.energie = energie
        self.espece =espece
        
    def depense(self):
        if self.energie > 0 :
            self.energie -= 1
        

def deplace_animaux() :
    
    Grille_2 =[[[] for i in range(n) ] for j in range(m)]
            
    for i in range(n):
        for j in range(m):
            for animal in Grille[i][j]:
                dx = rnd.randint(-1,1)
                dy = rnd.randint(-1,1)
                
                x= min (max (i+dx,0), n-1)
                y= min (max (j+dy,0), m-1)
                Grille_2[x][y].append(animal)
    
    for i in range(n):
        for j in range(m):
            Grille[i][j] = Grille_2[i][j] 
    

def mange_animaux(chaine_alimentaire):
    for i in range(n):
        for j in range(m):
            
            liste_animaux = Grille[i][j]
            #On trie la liste d'animaux par espèce croissante
            liste_animaux.sort(key = lambda animal : -animal.espece)
            chaine_alimentaire(liste_animaux)

def chaine_alimentaire(liste_animaux):
    # L'animal n'a aucune capture, il cherche une proie
    for animal in liste_animaux :
        capture = None
        for proie in liste_animaux:
            if proie.espece == animal.espece -1 :
                capture = proie
                break
        if capture != None:
            animal.energie += 16
            liste_animaux.remove(capture)
        
    return
        
def retire_morts():
    for i in range(n):
        for j in range(m):
            Grille[i][j] =[animal for animal in Grille[i][j] if animal.energie>0]

def reproduction () :
    for i in range(n):
        for j in range(m):
            liste = cp.copy(Grille[i][j])
            for animal in Grille[i][j]:
                if animal.espece != 0 and rnd.randrange(1,16)<=1:
                    bebe = Animal(animal.espece, 16)
                    liste.append(bebe)
            Grille[i][j] = liste
                
def tour ():
    deplace_animaux()
    mange_animaux(Grille,chaine_alimentaire)
    retire_morts(Grille)
    reproduction(Grille)



# Inutile    
def simulation(Grille):
    for k in range(100):
        tour(Grille)
    return



    

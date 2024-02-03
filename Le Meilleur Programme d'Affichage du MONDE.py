from tkinter import *
import random as rd

## Paramètres de la simulation

n = 5 # nombre de lignes
m = 5 # nombre de colonnes
taille_grille = 700
couleur_grille = 'green'

proba_herbe = 3/4 # juste pour faire des tests, je ne compte pas laisser

longueur_case = int(taille_grille/m)
hauteur_case = int(taille_grille/n)

## Création de la fenêtre

fenetre = Tk()
fenetre.title("Simulation")

fenetre.geometry(str(taille_grille+200)+"x"+str(taille_grille+40))

## Création de l'interface graphique

texte = Label(fenetre,text = "Simulation d'un système proie-prédateur (mais seulement avec de l'herbe)")
texte.grid(row = 0, column = 0)

affichage_grille = Canvas(fenetre,width = taille_grille+10,height = taille_grille+10)
affichage_grille.grid(row = 1, column = 0)

## Fonctions d'affichage

def creation_grille():
    for i in range(n+1):
        pas = int(i*taille_grille/n)
        affichage_grille.create_line(10,pas+10,taille_grille+10,pas+10,fill = couleur_grille,width = 1)
    for j in range(m+1):
        pas = int(j*taille_grille/m)
        affichage_grille.create_line(pas+10,10,pas+10,taille_grille+10,fill = couleur_grille,width = 1)

def dessine_cercle(canv,x,y,rad,color = 'black'):
    canv.create_oval(x-rad,y-rad,x+rad,y+rad,width = 0,fill = color)

def remplir_case(i,j,color = 'green',circle = True):
    if circle:
        rayon = min(longueur_case,hauteur_case)/2 - 10
        x,y = (j+1/2)*taille_grille/m+10,(i+1/2)*taille_grille/n+10
        dessine_cercle(affichage_grille,x,y,rayon,color)
    else:
        x1,y1 = (j*taille_grille/m)+10,(i*taille_grille/n)+10
        x2,y2 = x1+(taille_grille/m),y1+(taille_grille/n)
        affichage_grille.create_rectangle(x1,y1,x2,y2,width = 0,fill = color)

def init():
    for i in range(n):
        for j in range(m):
            p = rd.random()
            if p <= proba_herbe:
                remplir_case(i,j,color = 'green',circle = False)
            else:
                remplir_case(i,j,color = 'brown',circle = False)

def affichage(grille):
    print("pas fini")
    # Je pourrais compléter quand je saurais sous quelle forme se présentera la grille


## Lancement de la simulation

init()
fenetre.mainloop()


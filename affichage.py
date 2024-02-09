from tkinter import *
import random as rd

## Paramètres de la simulation

n = 50 # nombre de lignes
m = 50 # nombre de colonnes
taille_grille = 700
couleur_grille = 'black'
affiche_grille = False

couleur_animal = ['green', 'pink', 'black', 'orange']
longueur_case = taille_grille/m
hauteur_case = taille_grille/n


## Création de la fenêtre

fenetre = Tk()
fenetre.title("Simulation")
fenetre.geometry(f"{taille_grille+200}x{taille_grille+60}")


## Création de l'interface graphique

taille_canvas = taille_grille + 10
affichage_grille = Canvas(fenetre, width = taille_canvas, height = taille_canvas)
affichage_grille.pack(side = "bottom")


## Fonctions d'affichage

def creation_grille():
    for i in range(n + 1):
        y = i * taille_grille/n + 10
        affichage_grille.create_line(10, y, taille_canvas, y, fill = couleur_grille, width = 1)
    for j in range(m + 1):
        x = j * taille_grille/m + 10
        affichage_grille.create_line(x, 10, x, taille_canvas, fill = couleur_grille, width = 1)

def dessine_cercle(canv, x, y, rad, color = 'black'):
    canv.create_oval(x-rad, y-rad, x+rad, y+rad, width = 0, fill = color)

def remplir_case_cercle(i, j, color = 'white'):
    rayon = 0.45 * min(longueur_case, hauteur_case)
    x, y = (j+1/2) * taille_grille/m + 10, (i+1/2) * taille_grille/n + 10
    dessine_cercle(affichage_grille, x, y, rayon,color)

def remplir_case_rectangle(i, j, color = 'green'):
    x1, y1 = j * taille_grille/m + 10, i * taille_grille/n + 10
    x2, y2 = x1 + taille_grille/m, y1 + taille_grille/n
    affichage_grille.create_rectangle(x1, y1, x2, y2, width = 0, fill = color)

    if affiche_grille:
        creation_grille()

def ajout_ligne():
    global n
    global hauteur_case
    n += 1
    hauteur_case = taille_grille/n
    init()
    if affiche_grille:
        creation_grille()

def suppr_ligne():
    global n
    global hauteur_case
    global affiche_grille
    if n > 1:
        n -= 1
        hauteur_case = taille_grille/n
        init()
    if affiche_grille:
        creation_grille()

def ajout_colonne():
    global m
    global longueur_case
    global affiche_grille
    m += 1
    longueur_case = taille_grille/m
    init()
    if affiche_grille:
        creation_grille()

def suppr_colonne():
    global m
    global longueur_case
    global affiche_grille
    if m > 1:
        m -= 1
        longueur_case = taille_grille/m
        init()
    if affiche_grille:
        creation_grille()

def switch_grille():
    global affiche_grille
    affiche_grille = not affiche_grille
    if affiche_grille:
        creation_grille()


def affichage(grille):
    k, l = len(grille), len(grille[0])
    for i in range(k):
        for j in range(l):
            herbe, animal = grille[i][j]
            if herbe:
                remplir_case_rectangle(i, j, color = 'green')
            else :
                remplir_case_rectangle(i, j, color = 'orange')
            if animal >= 0:
                remplir_case_cercle(i, j, color = couleur_animal[animal])
    if affiche_grille:
        creation_grille()


## Boutons


show_grid = Button(fenetre, text = "Show/Hide grid", command = switch_grille)
show_grid.pack(side = "left")

add_row = Button(fenetre, text = "Add row", command = ajout_ligne)
add_row.pack(side = "left")

del_row = Button(fenetre, text = "Delete row", command = suppr_ligne)
del_row.pack(side = "left")

add_col = Button(fenetre, text = "Add column", command = ajout_colonne)
add_col.pack(side = "left")

del_col = Button(fenetre, text = "Delete column", command = suppr_colonne)
del_col.pack(side = "left")

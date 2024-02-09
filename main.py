import affichage as aff
import proie_predateur as prp 

def simulation(n):
    for k in range(n):
        prp.tour()
        prp.affichage()
    return

def tour_affiche():
    prp.tour()
    aff.affichage()

step = Button(aff.fenetre, text = "Step", command = tour_affiche)
step.pack(side = "right")

simulation()
aff.fenetre.mainloop()

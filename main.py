import affichage as aff
import proie_predateur as prp 

interrupteur_simulation = False

def simulation(n):
    for k in range(n):
        prp.tour()
        prp.affichage()
    return

def tour_affiche():
    prp.tour()
    aff.affichage()

def switch_simulation():
    interrupteur_simulation = not interrupteur_simulation

def simule_auto():
    if interrupteur_simulation:
        tour_affiche

step = Button(aff.fenetre, text = "Step", command = tour_affiche)
step.pack(side = "right")

run_stop = Button(aff.fenetre, text = "Run/Stop simulation", command = switch_simulation)
run_stop.pack(side = "right")

simulation()
aff.fenetre.after_idle(simule_auto)
aff.fenetre.mainloop()

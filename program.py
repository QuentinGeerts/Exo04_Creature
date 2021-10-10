from models.creature import Creature
from models.dresseur import Dresseur
import random


def choisir_creature(dresseur) :
    terminer = False
    while not terminer:
        position = random.randrange(0, dresseur.nb_creature)
        terminer = dresseur.changer_creature(position)



d1 = Dresseur("Deborah")
d1.ajouter_creature(Creature("mh", 15, 10, 5, 1))
d1.ajouter_creature(Creature("Louison", 18, 6, 10, 2))
d1.ajouter_creature(Creature("jordan", 30, 1, 1, 10))

d2 = Dresseur("Alan")
d2.ajouter_creature(Creature("nico", 15, 5, 10, 1))
d2.ajouter_creature(Creature("marc", 20, 2, 1, 10))
d2.ajouter_creature(Creature("francois", 20, 7, 3, 3))

d1.debuter_match()
d2.debuter_match()

print("Combat")
print(d1.creature_active)
print(d2.creature_active)
print()

while not(d1.est_vaincu or d2.est_vaincu):

    # 0 changer, 1 esquive, 2 se proteger, 3 attaque
    choix1 = random.randrange(0, 4)
    choix2 = random.randrange(0, 4)

    # Changement
    if choix1 == 0 :
        choisir_creature(d1)
        print("d1 changement")
    if choix2 == 0 :
        choisir_creature(d2)
        print("d2 changement")


    # esquive
    if choix1 == 1:
        d1.ordonner_esquive()
        print("d1 esquive")
    if choix2 == 1:
        d2.ordonner_esquive()
        print("d2 esquive")

    # attaquer
    if choix1 == 2:
        d1.ordonner_defense()
        print("d1 defense")
    if choix2 == 2:
        d2.ordonner_defense()
        print("d2 defense")

    if choix1 == 3 and choix2 == 3:
        print("d1 & d2 attaque")

        if d1.creature_active.vitesse > d2.creature_active.vitesse:
            d_ini = d1
            d_sec = d2
        else :
            d_ini = d2
            d_sec = d1

        d_ini.ordonner_attaque(d_sec.creature_active)
        if not d_sec.creature_active.est_ko:
            d_sec.ordonner_attaque(d_ini.creature_active)

    elif choix1 == 3 :
        print("d1 attaque")
        d1.ordonner_attaque(d2.creature_active)
    elif choix2 == 3:
        print("d2 attaque")
        d2.ordonner_attaque(d1.creature_active)

    d1.creature_active.terminer_tour()
    d2.creature_active.terminer_tour()


    if(not d1.est_vaincu and d1.creature_active.est_ko):
        choisir_creature(d1)
        print("d1 ko - switch")

    if (not d2.est_vaincu and d2.creature_active.est_ko):
        choisir_creature(d2)
        print("d2 ko - switch")

    print(" - Fin de tour")
    print(d1.creature_active)
    print(d2.creature_active)
    print()



d1.terminer_match()
d2.terminer_match()

if not d1.est_vaincu:
    print("d1 Win")
else:
    print("d2 Win")

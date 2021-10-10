import random


class Creature:

    def __init__(self, nom, pdv, force, vitesse, armure):
        if (pdv + force + vitesse + armure) > 42:
            raise ValueError()

        self.__nom = nom
        self.__pdv = pdv
        self.__force = force
        self.__vitesse = vitesse
        self.__armure = armure
        self.__armure_max = armure
        self.__mode_esquive = False
        self.__mode_protection = False

    # region Propriétés
    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def pdv(self):
        return self.__pdv

    @property
    def est_ko(self):
        return self.__pdv <= 0

    @property
    def force(self):
        return self.__force

    @property
    def vitesse(self):
        return self.__vitesse

    @property
    def taux_esquive(self):
        esquive = 20 * (self.vitesse / 10)

        if self.__mode_esquive:
            esquive += 50

        return esquive

    @property
    def armure(self):
        return self.__armure

    # endregion

    # region Méthode
    def preparer_esquive(self):
        self.__mode_esquive = True

    def se_proteger(self):
        self.__armure = self.__armure_max
        self.__mode_protection = True

    def attaquer(self, cible):

        degats = self.__force

        if random.randint(1, 100) <= 5:
            degats *= 2

        cible.subir_attaque(degats)

    def subir_attaque(self, degats):

        if random.randint(1, 100) > self.taux_esquive:
            self.subir_degats(degats)

    def subir_degats(self, degats):

        if self.__mode_protection:
            degats /= 2

        if self.__armure >= degats:
            self.__armure -= degats
        else:
            self.__pdv -= degats - self.__armure
            self.__armure = 0

    def terminer_tour(self):
        self.__mode_protection = False
        self.__mode_esquive = False
    # endregion

    # region methode spécials
    def __str__(self):
        return "{0} (pv:{1} ar:{2}/{3})".format(self.nom, self.pdv, self.armure, self.__armure_max)
    # endregion

class Dresseur:

    def __init__(self, nom):
        self.__nom = nom
        self.__limite_creature = 6
        self.__creatures = list()
        self.__creature_active = None

    # region Propriétés
    @property
    def nom(self):
        return self.__nom

    @property
    def creatures(self):
        return tuple(self.__creatures)

    @property
    def creature_active(self):
        return self.__creature_active

    @property
    def nb_creature(self):
        return len(self.__creatures)

    @property
    def est_vaincu(self):
        vaincu = True
        i = 0
        while vaincu and i < len(self.__creatures):
            if not self.__creatures[i].est_ko:
                vaincu = False
            i += 1

        return vaincu

    # endregion

    # region Methodes
    def ajouter_creature(self, creature):
        if len(self.__creatures) < self.__limite_creature:
            self.__creatures.append(creature)

    def debuter_match(self):
        if self.est_vaincu:
            raise ValueError()  # TODO Create custom error

        en_cours = True
        i = 0
        while en_cours:
            if not self.__creatures[i].est_ko:
                self.__creature_active = self.__creatures[i]
                en_cours = False
            i += 1

    def terminer_match(self):
        self.__creature_active = None

    def ordonner_attaque(self, creature):
        self.creature_active.attaquer(creature)

    def ordonner_esquive(self):
        self.creature_active.preparer_esquive()

    def ordonner_defense(self):
        self.__creature_active.se_proteger()

    def changer_creature(self, position):

        if not self.__creatures[position].est_ko:
            self.__creature_active = self.__creatures[position]
            return True

        return False

    # endregion


    # region methode spécials
    def __str__(self):
        nb_ok = 0
        for creature in self.__creatures:
            if not creature.est_ko:
                nb_ok += 1

        return "{0} a {1} creatures dont {2} pret au combat".format(self.nom, self.nb_creature, nb_ok)
    # endregion

class SokobanController:
    """
    TODO - fonction changement de direction - mise en place timer  et mise a jour du model - gestion des evenements
    TODO - de la vue et gerer deplacement caisse - methode pour ajouter les differentes valeur a la matrice :
    TODO - 0 = case libre   1 = joueur, 2 = mur, 3 = trou(objectif rien de personnel hein)
    PS: hesitez pas a ajouter des idéee
    """

    def __init__(self):
        self.__model = None
        self.__view = None

    def setView(self, view):
        self.__view = view

    def setModel(self, model):
        self.__model = model

    def movement(self, dir):
        print(self.__model.getMatrix())
        if not self.victoire():
            if self.verifMurPerso(dir):
                if self.verifCaisses(dir):
                    self.__model.setCoordoneePerso(
                        [self.__model.getCoordonneePerso()[0] + dir[0], self.__model.getCoordonneePerso()[1] + dir[1]]
                    )
                    self.__model.addPas()

                    self.__model.update(self.__model.getMatrix())
                elif not self.verifCaisses(dir):
                    if self.verifMurCaisse(dir):
                        if self.verifCaisseCaisse(dir):
                            indice = self.obtenirLaCaisseABouger(dir)

                            self.__model.modifierCaisse(
                                indice, [
                                    self.__model.getCaisse()[indice][0] + dir[0],
                                    self.__model.getCaisse()[indice][1] + dir[1]
                                ])
                            self.__model.setCoordoneePerso(
                                [self.__model.getCoordonneePerso()[0] + dir[0],
                                 self.__model.getCoordonneePerso()[1] + dir[1]]
                            )
                            self.__model.addPas()
                            self.__model.update(self.__model.getMatrix())
                            self.__view.caisseBouger()
                            if self.victoire():
                                self.__view.victoireSon()
                            self.caisseAObjectif(indice)
                    print(self.__model.getPas())
    def caisseAObjectif(self,i):
        caisse = self.__model.getCaisse()[i]
        trou = self.__model.getTrou()
        for j in trou:
            if caisse == j:
                self.__view.objectif()
    
    def obtenirLaCaisseABouger(self, coo):
        caisse = self.__model.getCaisse()
        perso = self.__model.getCoordonneePerso()
        for i in range(len(caisse)):
            if perso[0] + coo[0] == caisse[i][0] and perso[1] + coo[1] == caisse[i][1]:
                return i

    def verifMurPerso(self, dir):
        matrice = self.__model.getMatrix()
        cooPerso = self.__model.getCoordonneePerso()
        if matrice[cooPerso[0] + dir[0]][cooPerso[1] + dir[1]] != 2:
            return True
        return False

    def verifMurCaisse(self, dir):
        matrice = self.__model.getMatrix()
        cooPerso = self.__model.getCoordonneePerso()
        if matrice[cooPerso[0] + (dir[0]) * 2][cooPerso[1] + (dir[1]) * 2] != 2:
            return True
        return False

    def verifCaisseCaisse(self, dir):
        cooPerso = self.__model.getCoordonneePerso()
        for element in self.__model.getCaisse():
            if element[0] == cooPerso[0] + (dir[0]) * 2 and element[1] == cooPerso[1] + (dir[1]) * 2:
                return False
        return True

    def verifCaisses(self, dir):
        cooPerso = self.__model.getCoordonneePerso()
        cooCaisse = self.__model.getCaisse()
        for elements in cooCaisse:
            if elements[0] == cooPerso[0] + dir[0] and elements[1] == cooPerso[1] + dir[1]:
                return False
        return True

    def victoire(self):
        caisse = self.__model.getCaisse()
        caisse.sort()
        trou = self.__model.getTrou()
        trou.sort()
        print(trou)
        for i in range(len(caisse)):
            if caisse != trou:
                print(caisse[0], caisse[1])
                return False
        return True

    def changeLevel1(self):
        self.__model.updateNiveau(1)

        self.__model.resetPas()



    def changeLevel2(self):
        self.__model.updateNiveau(2)
        self.__model.resetPas()


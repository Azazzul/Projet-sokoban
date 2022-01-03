# 0 = case libre   1 = joueur,, 2 = mur, 3 = trou(objectif rien de personnel hein), 4 caisse
class SokobanModel:
    def __init__(self, level):
        assert level == 1 or level == 2
        self.__controller = None
        self.__view = None
        self.__caisses = []
        self.__trou = []
        self.__step = 0
        if level == 1:
            self.__matrix = [
                [5, 5, 2, 2, 2, 5, 5, 5, 5],
                [5, 5, 2, 3, 2, 5, 5, 5, 5],
                [5, 5, 2, 0, 2, 2, 2, 2, 5],
                [2, 2, 2, 0, 0, 0, 3, 2, 5],
                [2, 3, 0, 0, 0, 2, 2, 2, 5],
                [2, 2, 2, 2, 0, 2, 5, 5, 5],
                [5, 5, 5, 2, 3, 2, 5, 5, 5],
                [5, 5, 5, 2, 2, 2, 5, 5, 5],
                [5, 5, 5, 5, 5, 5, 5, 5, 5]
            ]
            self.__coordonneePerso = [3, 4]
            self.__caisses = [[2, 3], [3, 5], [4, 3], [4, 4]]
        else:
            self.__matrix = [
                [5, 5, 5, 2, 2, 2, 2, 2, 5],
                [5, 2, 2, 2, 0, 0, 0, 2, 5],
                [5, 2, 3, 0, 0, 0, 0, 2, 5],
                [5, 2, 2, 2, 0, 0, 3, 2, 5],
                [5, 2, 3, 2, 2, 0, 0, 2, 2],
                [5, 2, 0, 2, 0, 3, 0, 0, 2],
                [5, 2, 0, 0, 3, 0, 0, 3, 2],
                [5, 2, 0, 0, 0, 3, 0, 0, 2],
                [5, 2, 2, 2, 2, 2, 2, 2, 2]
            ]
            self.__coordonneePerso = [2, 3]
            self.__caisses = [[2, 4], [3, 5], [4, 5], [6, 2], [6, 5], [6, 4], [6, 6]]

        for x in range(len(self.__matrix)):
            for y in range(len(self.__matrix[0])):
                if self.__matrix[x][y] == 3:
                    self.__trou.append([x, y])

    def getCoordonneePerso(self):
        return self.__coordonneePerso

    def setCoordoneePerso(self, coo):
        self.__coordonneePerso = coo

    def setView(self, view):
        self.__view = view

    def update(self, matrix):
        self.__matrix = matrix
        self.__view.update()

    def getCaisse(self):
        return self.__caisses

    def modifierCaisse(self, indice, caisse):
        self.__caisses[indice] = caisse

    def getTrou(self):
        return self.__trou

    def getMatrix(self):
        return self.__matrix

    def updateNiveau(self, level):
        self.__caisses = []
        self.__trou = []
        if level == 1:
            self.__matrix = [
                [5, 5, 2, 2, 2, 5, 5, 5, 5],
                [5, 5, 2, 3, 2, 5, 5, 5, 5],
                [5, 5, 2, 0, 2, 2, 2, 2, 5],
                [2, 2, 2, 0, 0, 0, 3, 2, 5],
                [2, 3, 0, 0, 0, 2, 2, 2, 5],
                [2, 2, 2, 2, 0, 2, 5, 5, 5],
                [5, 5, 5, 2, 3, 2, 5, 5, 5],
                [5, 5, 5, 2, 2, 2, 5, 5, 5],
                [5, 5, 5, 5, 5, 5, 5, 5, 5]
            ]
            self.__coordonneePerso = [3, 4]
            self.__caisses = [[2, 3], [3, 5], [4, 3], [4, 4]]
        else:
            self.__matrix = [
                [5, 5, 5, 2, 2, 2, 2, 2, 5],
                [5, 2, 2, 2, 0, 0, 0, 2, 5],
                [5, 2, 3, 0, 0, 0, 0, 2, 5],
                [5, 2, 2, 2, 0, 0, 3, 2, 5],
                [5, 2, 3, 2, 2, 0, 0, 2, 2],
                [5, 2, 0, 2, 0, 3, 0, 0, 2],
                [5, 2, 0, 0, 3, 0, 0, 3, 2],
                [5, 2, 0, 0, 0, 3, 0, 0, 2],
                [5, 2, 2, 2, 2, 2, 2, 2, 2]
            ]
            self.__coordonneePerso = [2, 3]
            self.__caisses = [[2, 4], [3, 5], [4, 5], [6, 2], [6, 4], [6, 5], [6, 6]]
        for x in range(len(self.__matrix)):
            for y in range(len(self.__matrix[0])):
                if self.__matrix[x][y] == 3:
                    self.__trou.append([x, y])
        self.__view.resetGridCaisse()
        self.__view.update()

    def addPas(self):
        self.__step += 1

    def getPas(self):
        return self.__step

    def resetPas(self):
        self.__step = 0

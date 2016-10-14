from core import Environnement as e

class Reseau(e.Environnement):
    """docstring for Reseau"""
    def __init__(self):
        super(Reseau, self).__init__()
        self.reseau = self.grille[:]
        self.lesAgentsReseau = []

    def ajouteReseau(self,reseauElement) :
        self.reseau[reseauElement.gety()][reseauElement.getx()] = reseauElement
        self.lesAgentsReseau.append(reseauElement)

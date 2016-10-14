from Trains import Rail as r

class ReseauCreator(object):
    """docstring for ReseauCreator"""
    def __init__(self, pathname,env):
        super(ReseauCreator, self).__init__()
        self.env = env
        self.pathname = pathname
        self.table = []
        self.lecture()

    def lecture(self) :
        f = open(self.pathname,'r')
        for line in f :
            ligne = line.split()
            ligneInt = []
            for element in ligne :
                ligneInt.append(int(float(element)))
                self.table.append(ligneInt)

    def construitReseaux(self) :
        # Plus tard il faut tester si la ligne corespond à un rail simple/aiguillage/feu etc
        for ligne in self.table :
            x = ligne[0]
            y = ligne[1]
            entree = [ligne[2],ligne[3]]
            sortie = [ligne[4],ligne[5]]
            rail = r.Rail(x,y,self.env)
            self.env.ajouteReseau(rail)

        for agent in self.env.lesAgentsReseau :
            agent.observeVoisins()


      
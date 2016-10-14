from core import Agent

class Rail(Agent.Agent):
    """docstring for Rail"""
    def __init__(self,x,y,env,entree,sortie):
        super(Rail, self).__init__()
        self.x = x
        self.y = y
        self.env = env
        self.entree = entree # list [x,y] ou rail, je ne le sais pas
        self.sortie = sortie

    def tellTrain(self,train) :
        if train.precedent == self.entree :
            train.futurX = self.sortie[0]
            train.futurY = self.sortie[1]
        else :
            train.futurX = self.entree[0]
            train.futurY = self.entree[1]

    def decide(self) :
        pass

    def update(self) :
        pass

    def place_agent(self,fenetre):
        raise NotImplementedError

    def coordMoore(self) :
        '''
        renvoie la liste [[x,y]] de ses 4(max) voisins
        '''
        lesPas = [[0,1][0,-1][1,0][-1,0]]
        res = []
        for pas in lesPas :
            (futurX, futurY) = self.x + pas[0] , self.y + pas[1]
            if not (futurX == -1 or futurY == -1 or futurX == len(self.env[0]) or futurY == len(self.env)) :
                res.append([futurX,futurY])
        return res


    def observeVoisins(self) :
        lesVoisins = self.coordMoore()
        for voisin in lesVoisins :
            x = voisin[0]
            y = voisin[1]
from core import Agent

class Train(Agent.Agent):
    """docstring for Train"""
    def __init__(self,x,y,env,direction):
        super(Train, self).__init__()
        self.x = x
        self.y = y
        self.prec = self.env.reseaux[self.y][self.x].entree
        self.futurX = None
        self.futurY = None
        self.env = env

    def decide(self) :
        self.env.reseaux[self.y][self.x].tellTrain(self)
        
    def update(self) :
        self.env.grille[self.y][self.x] = None
        self.x = self.futurX
        self.y = self.futurY
        self.env.grille[self.y][self.y] = self 
    

    def cercle(self,fenetre,x, y, r, coul ='black'):
        '''
        tracé d'un cercle de centre (x,y) et de rayon r
        Fonction reprise sur http://python.developpez.com/cours/TutoSwinnen/?page=Chapitre8
        '''
        fenetre.can.create_oval(x-r, y-r, x+r, y+r, outline='black', fill=coul, tag='agent')
        
        
    def place_agent(self,fenetre) :
        self.cercle(fenetre, self.x*fenetre.caseX + fenetre.caseX/2, self.y * fenetre.caseY + fenetre.caseY / 2,min(fenetre.caseX,fenetre.caseY)/2 ,coul='#FFEE00')
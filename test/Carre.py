import sys
sys.path.append('..')

from trains import Train
from trains import Rail
from core import SMA 
from core import Environnement as e

gridSizeX=50
gridSizeY=50
canvasSizeX=800
canvasSizeY=600

def construitCarre(x,y,longueur, pathname) :
    lesLignes = []
    xActuel = x
    yAcuel = y
    for i in range(4) :
        for j in range(longueur)




enoughDefenders = 4
defenderLife = 100

#fenetre = w.Window(gridSizeX=gridSizeX,gridSizeY=gridSizeY,canvasSizeX=canvasSizeX,canvasSizeY=canvasSizeY,boxSize=None,windowbg='black',title="Simulation de particules")
fenetre = WindowGame.WindowGame(gridSizeX=gridSizeX,gridSizeY=gridSizeY,canvasSizeX=canvasSizeX,canvasSizeY=canvasSizeY)

from main5 import main
import numpy as np
from stats import diagramme_bande, pie_chart

grid = np.full((100, 100), None, dtype=object)

nbPlex = 5775
nbApparts = 1890
nbEpiceries = 300
nbBureaux = 200
nbEcole = 80*6
nbLoisirs = 160*2 
nbBoutique = 300
nbRetail = 100*2

etagesPlex = 3
etagesApparts = 6

targetPopulation = 10000

#main(grid.shape[0], grid.shape[1], nbEcole, nbLoisirs, nbEpiceries, nbBoutique, nbBureaux, nbRetail, nbPlex, etagesPlex, nbApparts, etagesApparts, targetPopulation)

diagramme_bande(nbEcole, nbLoisirs, nbEpiceries, nbBoutique, nbBureaux, nbRetail, nbPlex, etagesPlex, nbApparts, etagesApparts, targetPopulation)
pie_chart(nbEcole, nbLoisirs, nbEpiceries, nbBoutique, nbBureaux, nbRetail, nbPlex, etagesPlex, nbApparts, etagesApparts, targetPopulation)
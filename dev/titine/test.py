from main5 import main
import numpy as np
from stats import diagramme_bande, pie_chart

grid = np.full((10, 10), None, dtype=object)

nbPlex = 5
nbApparts = 18
nbEpiceries = 3
nbBureaux = 20
nbEcole = 6
nbLoisirs = 13
nbBoutique = 6
nbRetail = 6

etagesPlex = 3
etagesApparts = 6

targetPopulation = 10000

main(grid.shape[0], grid.shape[1], nbEcole, nbLoisirs, nbEpiceries, nbBoutique, nbBureaux, nbRetail, nbPlex, etagesPlex, nbApparts, etagesApparts, targetPopulation)

#diagrammes
#diagramme_bande(nbEcole, nbLoisirs, nbEpiceries, nbBoutique, nbBureaux, nbRetail, nbPlex, etagesPlex, nbApparts, etagesApparts, targetPopulation)
#pie_chart(nbEcole, nbLoisirs, nbEpiceries, nbBoutique, nbBureaux, nbRetail, nbPlex, etagesPlex, nbApparts, etagesApparts, targetPopulation)
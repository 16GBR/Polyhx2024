# -*- coding: utf-8 -*-
import numpy as np

def blocsAPlacer(grid, targetPopulation, portionCommerciale, portionCommunautaire, portionMinParcs, populationEtageApparts, populationEtagePlex):
    
    blocsDispos = grid.sum()
    
    blocsCommu = int(portionCommunautaire*blocsDispos)
    nbCommu = blocsCommu // (1*6 + 2*2)
    restantCommu = blocsCommu % (1*6 + 2*2)
    nbEcole = nbCommu
    nbLoisirs = 2*nbCommu + restantCommu // 2 + (restantCommu % 2)
    
    blocsCommer = int(portionCommerciale*blocsDispos)
    nbCommer = blocsCommer // (3*1 + 3*1 + 2*1 + 1*2)
    restantCommer = blocsCommer % (3*1 + 3*1 + 2*1 + 1*2)
    nbEpiceries = 3*nbCommer + restantCommer // 2 + (restantCommer % 2)
    nbBoutique = 3*nbCommer
    nbBureaux = 2*nbCommer + restantCommer // 2
    nbRetail = nbCommer
    
    blocsHabitationsMax = blocsDispos - blocsCommer - blocsCommu - portionMinParcs*blocsDispos
    nbPlex = 3*blocsHabitationsMax // 4
    nbApparts = blocsHabitationsMax // 4
    targetPopulation -= 3*populationEtagePlex*nbPlex
    if targetPopulation < 5*populationEtageApparts*nbApparts:
        targetPopulation += populationEtagePlex*nbPlex
        if targetPopulation < 4*populationEtageApparts*nbApparts:
            targetPopulation += 2*populationEtagePlex*nbPlex
            return grid, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, targetPopulation
        else:
            etagesPlex = 2
            etagesApparts = int(targetPopulation/(nbApparts*populationEtageApparts))+1
            nbApparts = targetPopulation // (etagesApparts*populationEtageApparts) + 1
            targetPopulation += 2*populationEtagePlex*nbPlex
    else:
        etagesPlex=3
        etagesApparts = int(targetPopulation/(nbApparts*populationEtageApparts))+1
        nbApparts = targetPopulation // (etagesApparts*populationEtageApparts) + 1
        targetPopulation += 3*populationEtagePlex*nbPlex
        
    return grid, nbEcole, nbLoisirs, nbEpiceries, nbBoutique, nbBureaux, nbRetail, int(nbPlex), etagesPlex, int(nbApparts), etagesApparts, int(targetPopulation)
        
            
        
    
print(blocsAPlacer(np.ones((30, 30)), 30000, 0.1, 0.08, 0.05, 20, 10))
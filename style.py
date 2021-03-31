# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 15:25:19 2021

@author: Zakaria
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dtst = pd.read_csv("style.csv")

axe_abcisse = np.arange(0,20)
droite_c = dtst.iloc[:, 0].values
droite_d = dtst.iloc[:, 1].values
droite_e = dtst.iloc[:, 2].values

#Labeliser l'Axe et le Titre
plt.title("Evolution du Portefeuille")
plt.xlabel("Temps")
plt.ylabel("Montant du capital")

#Ploter les différentes droites
plt.plot(axe_abcisse,droite_c)
plt.plot(axe_abcisse,droite_d)
plt.plot(axe_abcisse,droite_e)

#Ajouter une annotation à une position du graphe
plt.annotate(s="faible croissance", xy =[2,1])
plt.annotate(s="forte croissance u benefice", xy =[4,6])
plt.annotate(s="forte croissance du PIB", xy =[12,15])

#Ajout de Légende
#le parametre loc permet de positionner la légende
plt.legend(["Evolution du chiffre d'affaire","Croissance du bénéfice","Croissance du PIB"], loc=0)

#Style de l'arriere plan
plt.style.use(["dark_background","fast"])

#Sauvegarder le graphe
plt.savefig("style.pdf", format='pdf')




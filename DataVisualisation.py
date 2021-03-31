# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 14:37:53 2021

@author: Zakaria
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dtst = pd.read_csv('graph_1.csv')

axe_abcisse = dtst.iloc[:,0]
axe_ordonne = dtst.iloc[:,-1]

#Mise en place de graphe simple
plt.plot(axe_abcisse, axe_ordonne)

#Labeliser l'Axe et le Titre
plt.title("Evolution du Portefeuille")
plt.xlabel("Temps")
plt.ylabel("Montant du capital")

#Formater la couleur de la ligne
plt.plot(axe_abcisse, axe_ordonne, color='green')

#Sauvegarder le graphique
plt.savefig('illustration_graph_1.pdf', format='pdf')


# -*- coding: utf-8 -*-
"""
Created on Fri May 24 17:20:49 2019

@author: 2017-1099
"""
import os
import matplotlib.pyplot as plt

os.chdir('C:\\Users\\matth_000\\Desktop\\ruzzle_solve')
source=open('out.txt','r')
out = open('dico.txt','w')

lines = [line.rstrip('\n') for line in source]
compt = 0
N = len(lines)



#for i in range(N):
#    n = len(lines[i])
#    if n > 14 or n == 1:
#        del lines[i]
#        compt +=1

#decomenter cette ligne pour analyser la grille
#
#lines=[wordingrid[i][0] for i in range(len(wordingrid))]
comptmot = [0]*30
N = len(lines)
for i in range(N):
    n = len(lines[i])
    comptmot[n-1]+=1

nbcar = [i for i in range(1,31)]

plt.bar(nbcar,comptmot)
plt.show()
    
    

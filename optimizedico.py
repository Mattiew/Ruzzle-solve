# -*- coding: utf-8 -*-
"""
Created on Fri May 24 17:20:49 2019

@author: 2017-1099
"""
import os

os.chdir('Z:\\Config\\Bureau\\Ruzzle solve')
source=open('out.txt','r')
out = open('dico.txt','w')

lines = [line.rstrip('\n') for line in source]
compt = 0
N = len(lines)
for i in range(N):
    n = len(lines[i])
    if n > 14 or n == 1:
        del lines[i]
        compt +=1
    
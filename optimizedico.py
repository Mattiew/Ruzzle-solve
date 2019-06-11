# -*- coding: utf-8 -*-
"""
Created on Fri May 24 17:20:49 2019

@author: 2017-1099
"""
import os

os.chdir('D:\Documents\Ruzzle-solve-master')
source=open('out.txt','r')
out = open('dico.txt','w')
keptword=[]
lines = [line.rstrip('\n') for line in source]
compt = 0
N = len(lines)
for i in range(N-1):
    n = len(lines[i])
    if n <= 10 and n != 1:
        keptword.append(lines[i])
        out.write(lines[i]+"\n")
        compt +=1

source.close()
out.close()

# -*- coding: utf-8 -*-
"""
Created on Wed May 22 15:39:10 2019

@author: matth_000
"""
import os 

os.chdir('C:\\Users\\matth_000\\Desktop\\ruzzle_solve')
source=open('listefrancais.txt','r')
out = open('out.txt','r')

textsource=source.read()
textout=out.read()
source.close()
out.close()


textsource=textsource.lower()
textsource = textsource.replace('1','')
textsource = textsource.replace('2','')
textsource = textsource.replace('4','')
textsource = textsource.replace('3','')
textsource = textsource.replace('5','')
textsource = textsource.replace('6','')
textsource = textsource.replace('7','')
textsource = textsource.replace('8','')
textsource = textsource.replace('9','')
textsource = textsource.replace('0','')
textsource = textsource.replace('*','')
textsource = textsource.replace('[','')
textsource = textsource.replace(']','')

textsource = textsource.replace('(','')
textsource = textsource.replace(')','')
textsource = textsource.replace('\"','')
textsource = textsource.replace('.','')
textsource = textsource.replace(',','')
textsource = textsource.replace('-',' ')
textsource = textsource.replace(';','')
textsource = textsource.replace('!','')
textsource = textsource.replace('?','')
textsource = textsource.replace('é','e')
textsource = textsource.replace('è','e')
textsource = textsource.replace('ê','e')
textsource = textsource.replace('î','i')
textsource = textsource.replace('ï','i')
textsource = textsource.replace('à','a')
textsource = textsource.replace('\'',' ')
textsource = textsource.replace('    ',' ')
textsource = textsource.replace('   ',' ')
textsource = textsource.replace('  ',' ')
textsource = textsource.replace(':',' ')

newword = textsource.split()
oldword = textout.split('\n')
new = newword+oldword
new1= list(set(new))
new1.sort()

out = open('out.txt','w')
for i in new1:
    out.write(i.upper()+"\n")
out.close()
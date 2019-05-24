# -*- coding: utf-8 -*-
import numpy as np
import os
from copy import copy

class grid:
    
    def __init__(self):
        self.letters = []
        self.point =[]
        self.bonus=[]
    
    def setLetter(self,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p):
        self.letters = [[a,b,c,d],[e,f,g,h],[i,j,k,l],[m,n,o,p]]
        
    def setpoint(self,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p):
        self.point = [[a,b,c,d],[e,f,g,h],[i,j,k,l],[m,n,o,p]]
    
    def setbonus(self,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p):
        self.bonus = [[a,b,c,d],[e,f,g,h],[i,j,k,l],[m,n,o,p]]
    
    def pos(self,caractere):
        res=[]
        for i in range(4):
            for j in range(4):
                if self.letters[i][j].upper()==caractere.upper():
                    res.append([i,j])
        return res
    
    def voisin(self,pos):
        if pos[0]==0:
            if pos[1]==0:
                vois=[[0,1],[1,0],[1,1]]
            elif pos[1] == 3:
                vois = [[0,2],[1,2],[1,3]]
            else:
                j=pos[1]
                vois = [[0,j-1],[1,j-1],[1,j],[1,j+1],[0,j+1]]
        elif pos[0]==3:
            if pos[1]==0:
                vois=[[3,1],[2,0],[2,1]]
            elif pos[1] == 3:
                vois = [[3,2],[2,2],[2,3]]
            else:
                j=pos[1]
                vois = [[3,j-1],[2,j-1],[2,j],[2,j+1],[3,j+1]]
        else:
            i=pos[0]
            j=pos[1]
            if pos[1]==0:
                vois=[[i-1,0],[i-1,1],[i,1],[i+1,1],[i+1,0]]
            elif pos[1] == 3:
                vois = [[i-1,3],[i-1,2],[i,2],[i+1,2],[i+1,3]]
            else:
                vois = [[i-1,j-1],[i,j-1],[i+1,j-1],[i+1,j],[i+1,j+1],[i,j+1],[i-1,j+1],[i-1,j]]
        
        lettrevois=[]
        for x in vois:
            lettrevois.append(self.letters[x[0]][x[1]])
        return [lettrevois,vois]
    def modify(self,pos,car):
        self.letters[pos[0]][pos[1]]=car
            
game  = grid()
#game.setLetter('c','v','e','l','r','e','t','a','l','l','i','o','u','t','e','s')

os.chdir('C:\\Users\\matth_000\\Desktop\\ruzzle_solve')
dico=open("out.txt","r")
word=dico.read()
liste=word.split('\n')
dico.close()

game.setpoint(1,1,1,1,1,1,3,1,6,1,1,4,1,2,1,2)

wordingrid=[]
nbmot=len(liste)
compt=0
k2=0


for currentword in liste:
    
    game.setLetter('e','r','t','e','o','u','s','r','p','n','e','l','n','m','a','m') #c'est vhiant il faudrait poutot faire une copie
    compt+=1

    k1=k2
    k2=round(10000*compt/nbmot)/100
    if k1!=k2:
        print(k2)
        
    isingrid = 1
    n=0
    N= len(currentword)
    letterpos = game.pos(currentword[n])
    
    
    if letterpos==[]:
        isingrid=0
        
    for position in letterpos:
        copygame = copy( game)
        nextpos=position
        trace=[]
        while isingrid:
#        print('tag2')
            trace.append(nextpos)
            copygame.modify(nextpos,'done')
            
            lettrevoisine = game.voisin(nextpos)
            n+=1
            if n==N:
                    
                    wordingrid.append([currentword,trace])
                    isingrid=0
                    
            elif currentword[n].lower() in lettrevoisine[0]:
                nextind = lettrevoisine[0].index(currentword[n].lower())
                nextpos = lettrevoisine[1][nextind]
                
                
                
            
            else:
                isingrid = 0
                
        

tword=np.transpose(wordingrid)
point=[]
i=0
for currentword in tword[1]:
    s=0
    for p in currentword:
        s+=game.point[p[0]][p[1]]
    wordingrid[i].append(s)
    i+=1
    


            
        
    

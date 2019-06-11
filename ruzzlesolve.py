# -*- coding: utf-8 -*-
#%%importation des bibliothèques
import numpy as np
import os
from copy import copy
from time import time



#%%on defini la classe grid

class grid:
    """Classe definissant totalement une grille de jeu ruzzle. On stock les informations dans un tableau 4x4
    une information relative a une case se trouve dans la position correspondante
    La classe possede 3 attributs:
        grid.letters: les lettres de la grille de jeu
        grid.point: les points correspondants a chaque case
        grid.bonus: si des bonus existe il seront stocké dans ce tableau
        
        la classe possede 6 methodes
        grid.setLetter pour initialiser une grille
        grid.setpoint pour initialiser les points d'une grille
        grid.setbonus pour initialiser les bonus eventuels
        grid.pos donne les positions dans la grille d'un caractère donné
        grid.voisin renvois la position et la valeur des cases voisines d'une case donnée
        grid.modify modifie une case donnée de la grille"""

    
    def __init__(self):
        self.letters = []
        self.point =[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.bonus=[]
    
    def setLetter(self,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p):
        self.letters = [[a,b,c,d],[e,f,g,h],[i,j,k,l],[m,n,o,p]]
        
    def setpoint(self):
        for i in range(4):
            for j in range(4):
                car = self.letters[i][j]
                if car.upper() =="a".upper():
                    self.point[i][j] = 1
                    
                elif car.upper() =="b".upper():
                    self.point[i][j] = 3
                
                elif car.upper() =="c".upper():
                    self.point[i][j] = 3
                    
                elif car.upper() =="d".upper():
                    self.point[i][j] = 2
                
                elif car.upper() =="e".upper():
                    self.point[i][j] = 1
                
                elif car.upper() =="f".upper():
                    self.point[i][j] = 4
                
                elif car.upper() =="g".upper():
                    self.point[i][j] = 8
                
                elif car.upper() =="h".upper():
                    self.point[i][j] = 4
                
                elif car.upper() =="i".upper():
                    self.point[i][j] = 1
                
                elif car.upper() =="j".upper():
                    self.point[i][j] = 1
                
                elif car.upper() =="k".upper():
                    self.point[i][j] = 5
                
                elif car.upper() =="l".upper():
                    self.point[i][j] = 1
                
                elif car.upper() =="n".upper():
                    self.point[i][j] = 1
                
                elif car.upper() =="m".upper():
                    self.point[i][j] = 2
                
                elif car.upper() =="o".upper():
                    self.point[i][j] = 1
                
                elif car.upper() =="p".upper():
                    self.point[i][j] = 4
                
                elif car.upper() =="q".upper():
                    self.point[i][j] = 8
                
                elif car.upper() =="r".upper():
                    self.point[i][j] = 1
                
                elif car.upper() =="s".upper():
                    self.point[i][j] = 1
                
                elif car.upper() =="t".upper():
                    self.point[i][j] = 1
                
                elif car.upper() =="u".upper():
                    self.point[i][j] = 1
                
                elif car.upper() =="v".upper():
                    self.point[i][j] = 1
                
                elif car.upper() =="w".upper():
                    self.point[i][j] = 4
                
                elif car.upper() =="x".upper():
                    self.point[i][j] = 1
                
                elif car.upper() =="y".upper():
                    self.point[i][j] = 4
                
                elif car.upper() =="z".upper():
                    self.point[i][j] = 10
                
                
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
       
#%%on commence par creer un grille de jeu et on d"clare les variables utiles 'D:\\Documents\\Ruzzle-solve-master'
def solve(path):
    game  = grid()
    game.setLetter('a','c','l','s','a','s','o','r','b','t','a','q','e','u','u','i')
    game.setpoint()
    
    #on ouvre le dictionnaire et on extrait les données
    os.chdir(path)
    dico=open("dico.txt","r")
    word=dico.read()
    liste=word.split('\n')
    dico.close()
    
    
    top=time() #debut chrono
    wordingrid=[] #mots dans la grille et leurs infos
    nbmot=len(liste) #nombre de mots dans le dico a tester
    compt=0 #nombre de mots testés
    k2=0 #variable tampon
    
    #liste pour faire des test
    #'e','r','t','e','o','u','s','r','p','n','e','l','n','m','a','m'
    
    
    
    for currentword in liste:
        
        game.setLetter('a','c','l','s','a','s','o','r','b','t','a','q','e','u','u','i') #c'est vhiant il faudrait poutot faire une copie
        compt+=1
        
    #permet l'affichage de la progression
        k1=k2
        k2=round(10*compt/nbmot)*10
        if k1!=k2:
            print(k2)
            
        isingrid = 1
        n=0
        N= len(currentword)
        letterpos = game.pos(currentword[n])
        
        
        if letterpos==[]:
            isingrid=0
            
        for position in letterpos:
            copygame = copy(game)
            nextpos=position
            trace=[]
            while isingrid:
    #        print('tag2')
                trace.append(nextpos)
                copygame.modify(nextpos,'done')
                
                lettrevoisine = game.voisin(nextpos)
                n+=1
                if n==N:
                        
                        
                        worddata=[currentword,trace]
                        s=0
                        for p in trace:
                            s+=game.point[p[0]][p[1]]
                        if n>5:
                            s+=0
                        elif n ==5:
                            s+=5
                        elif n==6:
                            s+=10
                        elif n==7:
                            s+=15
                        elif n==8:
                            s+=20
                        elif n>=9:
                            s+=25
                        
                        
                        sl = s/len(trace)
                        
                        worddata.append(s)
                        worddata.append(sl)
                        
                        lwig= len(wordingrid)
                        i=0
                        
                        if lwig ==0:
                            wordingrid.append(worddata)
                    
                        while i < lwig:
                            if wordingrid[i][3] > sl:
                                i+=1
                            else:
                                wordingrid.insert(i,worddata)
                                i=lwig
                            
                        isingrid=0
                        
                        
                elif currentword[n].lower() in lettrevoisine[0]:
                    nextind = lettrevoisine[0].index(currentword[n].lower())
                    nextpos = lettrevoisine[1][nextind]
                    
                    
                    
                
                else:
                    isingrid = 0
                    
            
    print(time()-top)
    return wordingrid    




            
        
    

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:31:51 2019

@author: Matthieu
"""

import socket

hote = "localhost" #mettre "192.168.0.23"
port = 12800

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))

msg_a_envoyer = b""
while msg_a_envoyer != b"fin":
    msg_a_envoyer = input("moi : ")
    # Peut planter si vous tapez des caractères spéciaux
    msg_a_envoyer = msg_a_envoyer.encode()
    # On envoie le message
    connexion_avec_serveur.send(msg_a_envoyer)
    msg_recu = connexion_avec_serveur.recv(1024)
    print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents
    msg_recu = connexion_avec_serveur.recv(1024)
    print("server : {}".format(msg_recu.decode()))
    connexion_avec_serveur.send(b"----------------------recu----------------------")
    
print("Fermeture de la connexion")
connexion_avec_serveur.close()

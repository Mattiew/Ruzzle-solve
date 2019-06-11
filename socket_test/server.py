# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:10:40 2019

@author: Matthieu
"""

import socket

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

connexion_avec_client, infos_connexion = connexion_principale.accept()

msg_recu = b""
while msg_recu != b"fin" or msg_a_envoyer != b"fin":
    msg_recu = connexion_avec_client.recv(1024)
    # L'instruction ci-dessous peut lever une exception si le message
    # Réceptionné comporte des accents
    print('client : {}'.format(msg_recu.decode()))
    connexion_avec_client.send(b"----------------------recu----------------------")
    
    if msg_recu != b"fin":
        msg_a_envoyer = input("moi : ")
        msg_a_envoyer = msg_a_envoyer.encode()
        connexion_avec_client.send(msg_a_envoyer)
        msg_recu = connexion_avec_client.recv(1024)
        print(msg_recu.decode())
        
print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()

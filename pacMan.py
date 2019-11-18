
from event import *
from fonction_annexe import *
from time import sleep
from time import time
from random import randint


pacMan = initialise_pacMan()

fantomes = initialise_fantomes()
            
cerise = { "x":10 , "y":10 , "image" : './image/pacman_droite.png' }


points = []#initialise_point()
superPoints = []#initialise_superPoint()
cerises = []#initialise_cerise()
murs = [] #initialise_murs()
            
terrain = { "TAILLE_LARGEUR" : 600 , "TAILLE_LARGEUR" : 600, "TAILLE_CASE_HAUTEUR":30, "TAILLE_CASE_LARGEUR":40 ,"murs":murs}


initialiseJeu(pacMan,fantomes,points,superPoints,cerises)
cree_fenetre(terrain["TAILLE_LARGEUR" ],terrain["TAILLE_LARGEUR"])

while gameOver(pacMan):

    # affichage des objets

    efface_tout()
    afficheJeu(terrain,pacMan,fantomes,points,superPoints,cerises)
    mise_a_jour()
    
            
    
    # gestion des événements
    evenement = donne_ev()
    type = type_ev(evenement)
    
    if type == 'Quitte':
        break
        
    elif type == 'Touche':
        
        pacMan["direction"] = change_direction(pacMan, touche(evenement)) # direction
        for i in range(0,len(fantomes)):
            for j in range(0,len(murs)):
                if collision_pacMan_fantome(pacMan, fantome) :
                    fantomes[i]["direction"] =  change_direction_fantome(fantomes[i])# direction
    
    #deplacement
    deplace_personnage(pacMan,fantomes)
    teleportation(pacMan,terrain["TAILLE_LARGEUR" ],terrain["TAILLE_LARGEUR"])
    collision(pacMan,fantomes,points,superPoints,cerises)
    
    # attente avant rafraîchissement
    sleep(1/pacMan["vitesse"])
    
ferme_fenetre()

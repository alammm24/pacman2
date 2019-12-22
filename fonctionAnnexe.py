from event import *
from fonction_annexe import *
from time import sleep
from time import time
from random import randint
import pygame

def teleportation(personnage,largeur_terrain,longeur_terrain):
    """ Cette fonction permet de passer d'un cote du mur et de reapparaitre de l'autre """

    if 0 >personnage["x"]:
            personnage["x"]= largeur_terrain
            
    elif personnage["x"] > largeur_terrain:
            personnage["x"] = 0
            
    elif 0 > personnage["y"]:
            personnage["y"] = longeur_terrain
            
    elif personnage["y"] > longeur_terrain:
            personnage["y"] = 0
            
    
def deplace_personnages(pacMan,fantomes,murs):
    deplace_pac_man(pacMan,murs)
    deplace_fantomes(fantomes,murs)
    
def deplace_pac_man(personnage,murs) :
   
    if valide_deplacement(personnage,murs) :
        deplace_personnage(personnage)

def deplace_fantomes(fantomes,murs) :
    for fantome in fantomes:
        deplace_fantome(fantome,murs)
        
def deplace_fantome(personnage,murs) :
    
    if valide_deplacement(personnage,murs) :
        deplace_personnage(personnage)
    else :
        while not valide_deplacement(personnage,murs) :
            change_direction_fantome(fantome)
            deplace_personnage(personnage)

def deplace_personnage(personnage) :
    personnage["x"]+= personnage["direction"][0]
    personnage["y"]+= personnage["direction"][1]
    
    
def valide_deplacement(personnage,murs) :
    for i in murs :
        if (i[0] == personnage["x"]+ personnage["direction"][0]) and  (i[1] == personnage["y"]+ personnage["direction"][1]) :
            return False
    
    return True
    

def change_direction_pac_man(pacMan, touche):
    
    if touche == 'Up':  # flèche haut pressée
        pacMan["image"] = './image/pacman_haut.png'
        pacMan["direction"]=[0, -10]
        
    elif touche == 'Down': # flèche bas pressée
        pacMan["image"] = './image/pacman_bas.png'
        pacMan["direction"]= [0, 10]
        
    elif touche == 'Left': # flèche gauche pressée
        pacMan["image"] = './image/pacman_gauche.png'
        pacMan["direction"]= [-10, 0]
        
    elif touche == 'Right':  # flèche droite pressée
        pacMan["image"] = './image/pacman_droite.png'
        pacMan["direction"]=[10, 0]
        
    else :                 #afin de pas provoque une erreur si on appuie pas sur autre touche
        pacMan["direction"]= pacMan["direction"]
        
    

def change_direction_fantome(fantome):
    rand = randint(0,5)
    direction = [[0, -10],[0, 10],[-10, 0],[10, 0]]
    fantome["direction"] = direction[rand]

def initialise_fantomes(fantomes):
    fantomes.append({ "x":300 , "y":300 , "image" : './image/pacman_bleu.png' , "vitesse" :10 ,"vulnerable" : False, "direction" : [10,0]})
    fantomes.append({ "x":270 , "y":300 , "image" : './image/pacman_jaune.png' , "vitesse" :10,"vulnerable" : False, "direction" : [10,0]})
    fantomes.append({ "x":330 , "y":300 , "image" : './image/pacman_rose.png' , "vitesse" :10,"vulnerable" : False, "direction" : [10,0]})
    fantomes.append({ "x":300 , "y":270 , "image" : './image/pacman_rouge.png' , "vitesse" :10,"vulnerable" : False, "direction" : [10,0]})    

def reinitialise_fantomes(fantomes):
    fantomes[0] = { "x":300 , "y":300 , "image" : './image/pacman_bleu.png' , "vitesse" :10 ,"vulnerable" : False, "direction" : [10,0]}
    fantomes[1] = { "x":270 , "y":300 , "image" : './image/pacman_jaune.png' , "vitesse" :10,"vulnerable" : False, "direction" : [10,0]}
    fantomes[2] = { "x":330 , "y":300 , "image" : './image/pacman_rose.png' , "vitesse" :10,"vulnerable" : False, "direction" : [10,0]}
    fantomes[3] =  { "x":300 , "y":270 , "image" : './image/pacman_rouge.png' , "vitesse" :10,"vulnerable" : False, "direction" : [10,0]}


    

def initialise_pacMan():
    ''' '''
    return { "x":10 , "y":10 , "image" : './image/pacman_droite.png' , "vie": 3, "vitesse" :100, "score":0 , "direction" : [10,0]}

def initialise_coordonne_pacMan(pacMan):
    ''' '''
    pacMan["x"] = 100
    pacMan["y"] = 100
    
    return pacMan

def initialise_coordonne_fantome(fantome):
    ''' '''
    fantome["x"] = 100
    fantome["y"] = 100
    


def initialiseJeu(pacMan,fantomes,points,superPoints,cerises):
    initialise_points()
    initialise_superPoints()
    initialise_cerises()
    initialise_fantomes(fantomes)
    initialise_pacMan()


        
def collision(pacMan,fantomes,points,superPoints,cerises):
    
    for fantome in fantomes:
        collision_pacMan_fantome(pacMan, fantome,fantomes)
    
    for point in points:
        collision_pacMan_point(pacMan, point)
    
    for cerise in cerises:
        collision_pacMan_cerise(pacMan, cerise)
    
    for superPoint in superPoints:    
        collision_pacMan_superPoint(pacMan, superPoint,fantomes)
        
        
def collision_pacMan_fantome(pacMan, fantome,fantomes):
    
   
    if (fantome["vulnerable"] == False) and (fantome["x"] == pacMan["x"]) and (fantome["y"] == pacMan["y"] ) :
        pacMan["vie"] += -1 
        initialise_coordonne_pacMan(pacMan)
        reinitialise_fantomes(fantomes) # on initialises tous les fantomes
        
    if (fantome["vulnerable"] == True) and ( fantome["x"] == pacMan["x"] and fantome["y"] == pacMan["y"] ) :
        initialise_coordonne_fantome(fantome)


    

def collision_pacMan_point(pacMan, point):
    
    if ( point["x"] == pacMan["x"] and point["y"] == pacMan["y"] ) :
        pacMan["score"] += -1

def collision_pacMan_cerise(pacMan, cerise):
    if ( cerise["x"] == pacMan["x"] and cerise["y"] == pacMan["y"] ) :
        pacMan["vitesse"] += 10

def collision_pacMan_superPoint(pacMan, superPoint,fantomes):
    
    if ( superPoint["x"] == pacMan["x"] and superPoint["y"] == pacMan["y"] ) :
        for i in range(0,len(fantomes)) :
            fantomes[i]["vulnerable"] = True
        
    
        
def dessine_terrain(terrain,pacMan):
    rectangle(0,0,terrain["TAILLE_LARGEUR"],terrain["TAILLE_LARGEUR"],remplissage = "black")
    
    for i in range(0,len(terrain["murs"])):
        afficheElement(terrain["murs"][i])
        
    # texte (pacMan["score"])
    # texte (pacMan["vie"])
    pass 


    
def afficheElement(element):
    # a,b = pixel_vers_case(personnage["x"],personnage["y"]) 
    # x, y = case_vers_pixel(a,b)
    image(element["x"],element["y"],element["image"], ancrage='center', tag='')
    
def afficheJeu(terrain,pacMan,fantomes,points,superPoints,cerises) :
    """ Cette fonction ajoute une nouvelle tête et supprime le corp pour donner l'impression de déplacement """
    
    dessine_terrain(terrain,pacMan) #Attention d'abord dessine terrain puis les personnages
    
    afficheElement(pacMan)
    
    for i in range(0,len(fantomes)):
        afficheElement(fantomes[i])
    
    for i in range(0,len(points)):
        afficheElement(points[i])
    
    for i in range(0,len(cerises)):
        afficheElement(cerises[i])
    
    for i in range(0,len(superPoints)):    
        afficheElement(superPoints[i])
    
def gameOver(pacMan):
    if pacMan["vie"] != 0 :
        return True
    return False
    
# def change_direction_fantomes(fantomes,murs,pacMan) :
#     for i in range(0,len(fantomes)):
#         for j in range(0,len(murs)):
#             if collision_pacMan_fantome(pacMan, fantome) :
#                 change_direction_fantome(fantomes[i])# direction
    
# def collision_fantome_mur(pacMan, mur):
#     if (fantome["x"] == mur["x"]) and (fantome["y"] == mur["y"] ) :
#         return True
#     return False
        
    
# def case_vers_pixel(x, y,terrain):
#     return x * terrain["TAILLE_CASE_LARGEUR"], y * terrain["TAILLE_CASE_HAUTEUR"]
# 
# def pixel_vers_case(x, y) :
#      return x // terrain["TAILLE_CASE_LARGEUR"], y //terrain["TAILLE_CASE_HAUTEUR"]
#     
# def pixel_vers_case_vers_pixel(x,y) :
#     x,y = pixel_vers_case(x,y)
#     x,y = case_vers_pixel(x,y)
#     return x,y 
#     
# def case_vers_pixel_vers_case(x,y) :
#     x,y = case_vers_pixel(x,y)
#     x,y = pixel_vers_case(x,y)
#     return x,y 



def menu() :
    pass
    
def initialise_points() :
    ''' '''
    pass
    
def initialise_superPoints() :
    ''' '''
    pass
    
def initialise_cerises() :
    ''' '''
    pass

def initialise_murs() :
    pass
    
def mode():
    mode_multijoueur()
    mode_contre_la_montre()
    mode_classsique()
    
def mode_multijoueur():
    pass

def mode_contre_la_montre():
    pass

def mode_classsique() :
    pass

def regle_jeu():
    pass

def jouer():
    pass

def rejouer():
    initialiseJeu(pacMan,fantomes,points,superPoints,cerises)

def meilleur_score():
    pass


        


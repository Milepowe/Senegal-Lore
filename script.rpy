# Vous pouvez placer le script de votre jeu dans ce fichier.

init python:
    from math import sqrt

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define lockedin = Character('???', color="#d4d4d4")
define mc = Character("[playername]",color="#0084ff")
define eliza = Character("Elizabeth",color="#034888")
define HIMgor = Character("Igor",color="#001930")

# Le jeu commence ici
label start:
    play music "character_creation.mp3" fadein 2.0

# 3D stage for the master layers
    camera:
        perspective True

    show lock_avatar at center with fade:
        zpos -200
        warp sqrt 3.5 zpos 0

    lockedin "Salut. Tu es en ce moment dans un dimension qui va te\npermettre de rejondre l'autre monde."
    lockedin "Et pour le rejoindre, tu vas devoir me donner\nquelques informations sur ta personne."
    
    lockedin "Quel est ton nom ?"

    # input qui donne le nom du joueur 
    python :
        while True :
            playername = renpy.input("Ton nom (sans espaces, 10 charactères max):")
            
            if playername != "" and playername not in " " and len(playername) < 10:
                break

    show lock_avatar :
        warp sqrt 0.5 xpos 350
    
    show screen show_created_name(playername)

    lockedin "Tu viens de rentrer ton nom, merci beaucoup."
    lockedin "Maintenant, je vais utiliser ma PUISSANCE pour\nte tp dans l'autre monde."

    menu :
        lockedin "T'es prêt du coup ?"

        "Oui." :
            lockedin "D'accord. Prépare toi."
        
        "Non" :
            lockedin "You ARE going to BRAZILLLL !!!"

    return

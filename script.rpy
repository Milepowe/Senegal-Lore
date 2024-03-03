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
        playername = ""
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


    
    # ON VA L'REPRENDRE UN JOUR

    #si le nom du joueur est "Elizabeth" il sera change pour "Elizabeth Wannabe"
    # if playername == "Elizabeth":
    #     play music "Circustheme.mp3"

    #     show elizabeth at left:
    #         zpos 200 
    #         linear 1.0 xpos 200 

    #     eliza "Nuh uh you're not me"
    #     eliza "There can't be two Elizabeth in this world"

    #     show elizabeth:
    #         linear 1.0 xpos 200 

    #     hide elizabeth

    #     $ playername = "Elizabeth Wannabe"
    #     $ Elizabeth_Flag = True

    # # [playername] est pour utiliser la variable playername
    # lockedin "Bienvenu dans le locked in realm, [playername]"
    # lockedin "Le lock in sont les raisons par lequelles le {b}grind se revele."
    # lockedin "Seuls ceux qui sont locked in, peuvent achever leur lock in."
    # lockedin "Atteindre son grind exige beaucoup de grind et une energie de sigma a toute epreuve."

    # #ouvre un menu qui a deux choix oui ou non et affiche le texte correspondant
    # menu:
    #     lockedin "es-tu un hunter?"

    #     "oui":
    #         mc "Oui monsieur je suis bel et bien un hunter."
    #         lockedin "Que ton grind soit rempli de grind."

    #     "non":
    #         mc "Qu'est-ce un hunter? je me sens tres faible."
    #         lockedin "Ta sentence est d'etre la plus grande des merguez, tu me decois beaucoup futur hunter."

    # hide lock_avatar

    # if Elizabeth_Flag == True:
    #     show igor
    #     HIMgor "Holy shit. \nYou fucking suck kid."
    #     HIMgor "Don't blame the AI for your awful tactics\nWhat fucking knob uses Act Freely"
    #     HIMgor "Use buffs dumbass,put down the\nguidebook and pickup some common sense"
    #     HIMgor "This game isn't even hard\n do not name yourself Elizabeth do you have some fetsih or something"
    #     HIMgor "you idiot"

    return

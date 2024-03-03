# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define lockedin = Character('The Lock In Avatar', color="#999898")
define mc = Character("[playername]",color="#0084ff")
define eliza = Character("Elizabeth",color="#034888")
define HIMgor = Character("Igor",color="#001930")
# Le jeu commence ici
label start:
# j'ai juste fait un ctrl+c ctrl+v
    camera:
        perspective True
    transform zbg:
        zpos -100 zzoom True
    
    scene lock_realm

    show lock_avatar at center:
        zpos 0
        linear 1.0 zpos 200

    lockedin "Quel est ton nom inconnu au bataillon?"
    # input qui donne le nom du joueur
    $ playername = renpy.input("Quel est ton nom compatriote?")

    #si le nom du joueur est "Elizabeth" il sera change pour "Elizabeth Wannabe"
    if playername == "Elizabeth":
        play music "Circustheme.mp3"
        show elizabeth at left:
            zpos 200 
            linear 1.0 xpos 200 
        eliza "Nuh uh you're not me"
        eliza "There can't be two Elizabeth in this world"
        hide elizabeth
        $ playername = "Elizabeth Wannabe"
        $ Elizabeth_Flag = True
    # [playername] est pour utiliser la variable playername
    lockedin "Bienvenu dans le locked in realm, [playername]"

    lockedin "Le lock in sont les raisons par lequelles le {b}grind se revele."

    lockedin "Seuls ceux qui sont locked in, peuvent achever leur lock in."

    lockedin "Atteindre son grind exige beaucoup de grind et une energie de sigma a toute epreuve."

    #ouvre un menu qui a deux choix oui ou non et affiche le texte correspondant
    menu:
        lockedin "es-tu un hunter?"

        "oui":
            mc "Oui monsieur je suis bel et bien un hunter."
            lockedin "Que ton grind soit rempli de grind."
        "non":
            mc "Qu'est-ce un hunter? je me sens tres faible."
            lockedin "Ta sentence est d'etre la plus grande des merguez, tu me decois beaucoup futur hunter."
    hide lock_avatar
    if Elizabeth_Flag == True:
        show igor
        HIMgor "Holy shit. \nYou fucking suck kid."
        HIMgor "Don't blame the AI for your awful tactics\nWhat fucking knob uses Act Freely"
        HIMgor "Use buffs dumbass,put down the\nguidebook and pickup some common sense"
        HIMgor "This game isn't even hard\n do not name yourself Elizabeth do you have some fetsih or something"
        HIMgor "you idiot"



    return

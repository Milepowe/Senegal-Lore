# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define lockedin = Character('the lock in avatar', color="#999898")
define mc = Character("[playername]",color="#0084ff")


# Le jeu commence ici
label start:
    scene lock_realm

    show lock_avatar
    lockedin "quel est ton nom inconnu au bataillon?"

    $ playername = renpy.input("quel est ton nom?")

    lockedin "bienvenu dans le locked in realm [playername]"

    lockedin "the lock in is the means by which the {b}grind is revealed"

    lockedin "only those who are locked in can achieve their lock in"

    lockedin "attaining one's grind requires a lot of grind and unfailing sigma energy"

    menu:
        lockedin "es-tu un hunter"

        "oui":
            lockedin "que ton grind soit rempli de grind"
        "non":
            lockedin "ta sentence est d'etre la plus grande des merguez"




    return

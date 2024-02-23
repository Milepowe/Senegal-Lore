# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define lockedin = Character('the lock in avatar', color="#999898")


# Le jeu commence ici
label start:
    scene lock_realm

    show lock_avatar

    lockedin "the lock in is the means by which the grind is revealed"

    lockedin "only those who are locked in can achieve their lock in"

    lockedin "attaining one's grind requires a lot of grind and unfailing sigma energy"


    return

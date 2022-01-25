import random

def selectionLettres(monMot):
    #Permet de choisir 2 lettres successives à partir d'une position aléatoire
    positionAlea=random.randint(0, len(monMot)-2)
    #On génère une position à partir de laquelle prendre 2 lettres, de la position 0 à la longueur du mot - 2 (Le -2 permet de ne pas prendre la derière lettre du mot parce qu'il n'y a pas de 2ème lettre qui la suit)
    return monMot[positionAlea:positionAlea+2]
    #Permet de retourner 2 lettres à partir de la position aléatoire (d'où le + 2)


vies=3;
score=0;
mots = [] #Liste pour stocker les mots du fichier dictionnaire
with open('dictionnaire_francais.txt') as fichier:
    mots = fichier.read().splitlines()
    #On lit le fichier et on stock les mots. (.splitlines() permet de résoudre un problème de retour à la ligne qui s'ajoute après chaque mot)

while vies > 0:   #On joue tant qu'on a toutes nos vies
    mot= random.choice(mots)  #On choisi un mot aléatoire
    lettresAtrouver=selectionLettres(mot) #On selectionne 2 lettres à partir du mot
    motPropose = input(f"Trouvez un mot contenant ({lettresAtrouver}) ")

    if lettresAtrouver in motPropose:  #Il faut deja que le mot proposé par le joueur contienne les 2 lettres
        if motPropose in mots :   #Verifier que le mot proposé par le joueur est dans le dictionnaire
            score+=1
            print(f"Bravo ! votre score est de: {score} ")
        else:
            vies-=1
            print(f"Mot inexistant ! vies restantes: {vies}")
    
    else: 
        print(f"Le mot proposé ne contient pas les lettres ({lettresAtrouver})")
        vies-=1


#Quelques idées améliorer le jeu
#Ajouter un choix de difficulté (Facile, Moyen, Difficile), Facile: 4 lettres proposées, Moyen: 3 lettres, Difficile: 2 lettres
#Perdre si on ne trouve pas un mot avant 5 secondes
#Ajouter une interface
#Plusieurs joueurs

#Source du dictionnaire de mots http://www.pallier.org
# Écrivez un programme pendu.py, qui permet à l’utilisateur de faire une partie du célèbre
# jeu le pendu dans le terminal.
# Le programme devra dans un premier temps demander au joueur le niveau avec lequel il
# souhaite jouer. Il aura un nombre de vies en fonction du niveau choisi (exemple
# débutant 10, intermédiaire 7, expert 4). Vous êtes libres de choisir le nombre de vies par
# niveau.
# Le programme devra donc choisir aléatoirement un mot dans le dictionnaire disponible
# ici, et afficher :
# - Le nombre de vies restantes au joueur
# - Les lettres déjà proposées par le joueur (dans le mode débutant et intermédiaire.
# En expert, la liste n’apparaîtra pas)
# - Des “_” pour remplacer les lettres non trouvées
# - Les lettres proposées qui se trouvent dans le mot
# La partie prend fin lorsque le joueur a trouvé le mot, ou qu’il n’a plus de vie.


#import la fonction random
import random

#Choisir dans le fichier dico un mot au hasard
with open("C:\\Users\\jiyel\\Desktop\\PLATEFORME\\PYTHON\\EXO_2\\LE PENDU\\dico_france.txt", "r", encoding="UTF-8") as file:
    dico=file.read()
    choix=dico.split()

#print(random.choice(choix))

#d = open("dico_france.txt", "r") 
#y = d.read
# solution = random.choice(choix)

# et donc crée une variable “vie” qui diminue avec le nombre d’erreur effectuer
deb = "1"
inter="2"
exp="3"

#Créer une condition ou le niveau choisis affiche le nombre de vie correspondant #(10, 7, 4)
nivdeb=10
nivint=7
nivexp=4

solution = random.choice(choix)
affichage = ""
lettres_trouvees = ""
liste =[]

for l in solution:
    affichage = affichage + "_ "

print(">> Bienvenue dans le pendu <<")
while True  : 
#Tout autre choix que 1,2 ou 3 fera revenir à la question initiale : "à quel niveau souhaites-tu jouer"
    niveau=input("Bonjour, à quel niveau souhaites-tu jouer? Débutant [1], Intermédiaire [2] ou Expert [3] : ")
#faire un input qui permet au joueur de choisir son niveau : 
#"Bonjour, à quel niveau souhaites-tu jouer? Débutant [1], Intermédiaire [2] ou Expert [3] : "
    if niveau == deb:
            
            while nivdeb > 0:
                print("Nombre de vie(s) :",nivdeb)
                print("\nMot à deviner : ", affichage)
                proposition = input("Quelle lettre proposes-tu? : ")[0:1].lower()
                liste = liste + [proposition]
                print("lettre déja choisis : ",liste)

                if proposition in solution:
                    lettres_trouvees = lettres_trouvees + proposition
                    print("-> Bien vu!")
                else:
                    nivdeb = nivdeb - 1
                    print("-> Mauvaise réponse!\n")
                    if nivdeb<=0:
                        print(" ==========Y= ")
                    if nivdeb<=1:
                        print(" ||/       |  ")
                    if nivdeb<=2:
                        print(" ||        0  ")
                    if nivdeb<=3:
                        print(" ||       /|\ ")
                    if nivdeb<=4:
                        print(" ||       /|  ")
                    if nivdeb<=5:
                        print(" ||           ")
                    if nivdeb<=6:
                        print(" ||           ")
                    if nivdeb<=7:
                        print(" ||           ")
                    if nivdeb<=8:
                        print("/||           ")
                    if nivdeb<=9:
                        print("==============\n")

                affichage = ""
                for x in solution:
                    if x in lettres_trouvees:
                        affichage += x + " "
                    else:
                        affichage += "_ "

                if "_" not in affichage:
                    print(">>> Gagné! <<<")
                    break

    elif niveau == inter:
            
            while nivint > 0:
                print("Nombre de vie(s) :",nivint)
                print("\nMot à deviner : ", affichage)
                proposition = input("Quelle lettre proposes-tu? : ")[0:1].lower()
                liste = liste + [proposition]
                print("lettre déja choisis : ",liste)

                if proposition in solution:
                    lettres_trouvees = lettres_trouvees + proposition
                    print("-> Bien vu!")
                else:
                    nivint = nivint - 1
                    print("-> Mauvaise réponse!\n")
                    if nivint==0:
                        print(" ==========Y= ")
                    if nivint<=1:
                        print(" ||/       |  ")
                    if nivint<=2:
                        print(" ||        0  ")
                    if nivint<=3:
                        print(" ||       /|\ ")
                    if nivint<=4:
                        print(" ||       /|  ")
                    if nivint<=5:
                        print("/||           ")
                    if nivint<=6:
                        print("==============\n")

                affichage = ""
                for x in solution:
                    if x in lettres_trouvees:
                        affichage += x + " "
                    else:
                        affichage += "_ "

                if "_" not in affichage:
                    print(">>> Gagné! <<<")
                    break

    elif niveau == exp:
            
            while nivexp > 0:
                print("Nombre de vie(s) :",nivexp)
                print("\nMot à deviner : ", affichage)
                proposition = input("Quelle lettre proposes-tu? : ")[0:1].lower()
                liste = liste + [proposition]
                print("lettre déja choisis : ",liste)

                if proposition in solution:
                    lettres_trouvees = lettres_trouvees + proposition
                    print("-> Bien vu!")
                else:
                    nivexp = nivexp - 1
                    print("-> Mauvaise réponse!\n")
                    if nivexp==0:
                        print(" ==========Y= ")
                    if nivexp<=1:
                        print(" ||/       |  ")
                    if nivexp<=1:
                        print(" ||        0  ")
                    if nivexp<=2:
                        print(" ||       /|\ ")
                    if nivexp<=2:
                        print(" ||       /|  ")
                    if nivexp<=3:
                        print("/||           ")
                    if nivexp<=3:
                        print("==============\n")

                affichage = ""
                for x in solution:
                    if x in lettres_trouvees:
                        affichage += x + " "
                    else:
                        affichage += "_ "

                if "_" not in affichage:
                    print(">>> Gagné! <<<")
                    break


    print("\n    * Fin de la partie *    ")
    break
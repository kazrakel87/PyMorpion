
def menu():
    print 
    print " __   __     ____     _______    _______    __     ____     __   __"  
    print "|  \_/  |   /    \   |       |  |       |  |  |   /    \   |  \ |  |" 
    print "|   _   |  |  /\  |  |      _|  |   ____|  |  |  |  /\  |  |   \|  |"
    print "|  | |  |  |  \/  |  |  |\  \   |  |       |  |  |  \/  |  |  |\   |"
    print "|__| |__|   \____/   |__| \__\  |__|       |__|   \____/   |__| \__|"
    print
    print
    print
    

def affichage_grille():
    print
    print "[0][1][2] ------------ [",grille[0],"][",grille[1],"][",grille[2],"]"
    print "[3][4][5] ------------ [",grille[3],"][",grille[4],"][",grille[5],"]"
    print "[6][7][8] ------------ [",grille[6],"][",grille[7],"][",grille[8],"]"
    print


def saisie_coup(joueur):
    global coup
    coup = input(joueur + " - Quel est ton prochain coup ? ")
    verification_coup(coup)        


def verification_coup(coup):
    global nombre_de_coups
    if (str(coup).isdigit()) and (coup >= 0 and coup <= 9) and (grille[coup] == "") :
        nombre_de_coups += 1
    else :
        saisie_coup(liste_joueurs[nombre_de_coups % 2])


def jouer():
    affichage_grille()
    saisie_coup(liste_joueurs[nombre_de_coups % 2])

    if (nombre_de_coups % 2 == 0) :
        grille[coup] = "x"
    else : 
        grille[coup] = "o"

    verification_grille(grille)


def verification_grille(grille):
    global fin_de_partie
    if (grille[0] == grille[1] and grille[1] == grille[2] and grille[1] <> "") :
        fin_de_partie = True
    elif (grille[3] == grille[4] and grille[4] == grille[5] and grille[4] <> "") :
        fin_de_partie = True
    elif (grille[6] == grille[7] and grille[7] == grille[8] and grille[7] <> "") :
        fin_de_partie = True
    elif (grille[0] == grille[3] and grille[3] == grille[6] and grille[3] <> "") :
        fin_de_partie = True
    elif (grille[1] == grille[4] and grille[4] == grille[7] and grille[4] <> "") :
        fin_de_partie = True
    elif (grille[2] == grille[5] and grille[5] == grille[8] and grille[5] <> "") :
        fin_de_partie = True
    elif (grille[0] == grille[4] and grille[4] == grille[8] and grille[4] <> "") :
        fin_de_partie = True
    elif (grille[2] == grille[4] and grille[4] == grille[6] and grille[4] <> "") :
        fin_de_partie = True

    if (fin_de_partie) : 
        print "**********************************************"
        print "**********************************************"
        affichage_grille()
        print "**********************************************"
        print "**********************************************"
        print "Fin de partie !"


###################################################################################
###################### MAIN 
###################################################################################
liste_joueurs = ["Joueur1", "Joueur2"] 
coup = ""
grille = ["", "", "", "", "", "", "", "", ""]
fin_de_partie = False
nombre_de_coups = 0

menu()
while (not fin_de_partie) :
    jouer()


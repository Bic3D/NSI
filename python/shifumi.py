import random

score_ordi = 0
score_player = 0

def end(who):
    if who == "player":
        input("\nVous avez gagné!")
        score_player += 1

    elif who == "nobody":
        input("\nEgalité.")
        
    else:
        input("\nVous avez perdu.")
        score_ordi += 1


def manche():
    choix_joueur = input("pierre, papier ou ciseaux?\n> ")
    
    choix_possibles = ["pierre", "feuille", "ciseaux"]
    choix_ordi = random.choice(choix_possibles)

    print("Le choix de l'ordi est "+choix_ordi)

    if choix_ordi == choix_joueur:
        end("nobody")

    # si l'ordi choisit la pierre
    elif choix_ordi == "pierre" and choix_joueur == "papier":
        end("player")
    elif choix_ordi == "pierre" and choix_joueur == "ciseaux":
        end("ordi")

    # si l'ordi choisit le papier
    elif choix_ordi == "papier" and choix_joueur == "ciseaux":
        end("player")
    elif choix_ordi == "papier" and choix_joueur == "pierre":
        end("ordi")
    
    # si l'ordi choisit les ciseaux
    elif choix_ordi == "ciseaux" and choix_joueur == "pierre":
        end("player")
    elif choix_ordi == "ciseaux" and choix_joueur == "papier":
        end("ordi")
    

while True:
    if score_ordi == 3:
        print("\nVous avez perdu la partie.")
        break
    elif score_player == 3:
        print("\nVous avez gagné la partie!")
        break

    print(str(score_player)+" à "+str(score_ordi)+",\nManche suivante!\n")
    manche()
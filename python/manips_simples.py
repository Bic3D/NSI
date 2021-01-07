def DEJA_VU():
    nom_prenom= input("entrez des trucs: ")
    nom = nom_prenom.split(" ")[0]
    nom = nom[0].upper()# + nom[1:]
    prenom = nom_prenom.split(" ")[1]
    prenom = prenom[0].upper()# + prenom[1:]
    print(nom,prenom)

def stocker_des_calories():
    valeurs = [i**2 - 2*i+3 for i in range(10)]
    print(valeurs)

def manipalutations_simples():
    liste = [45, 17, 89, 38, 10, 74]
    liste.sort()
    print(liste)
    liste.append(12)
    
    for i in range(len(liste)//2):
        liste[i],liste[-i-1] = liste[-i-1],liste[i]

    print(liste)
    
    for i in range(len(liste)):
        if liste[i] == 10:
            print("L'indice de l'élément 10 est "+str(i))

    liste.remove(38)
    print(liste)
    print(liste[1:3])
    print(liste[:2])
    print(liste[2:])
    print(liste[-1])

#manipalutations_simples()
#print("[10, 17, 38, 45, 74, 89]\n[12, 89, 74, 45, 38, 17, 10]\nL'indice de l'élément 10 est 6\n[12, 89, 74, 45, 17, 10]\n[89, 74]\n[12, 89]\n[74, 45, 17, 10]\n10")


def ex5():
    array = []
    chaine1 = "abc"
    chaine2 = "de"
    for i in chaine1:
        for j in chaine2:
            array.append(i+j)
    return array
    
print(ex5())



def ex4_1(n):
    array = []
    for i in range(1,n+1):
        array.append(1)
        array.append(i)
    return array
#print(ex4_1(10))

def ex4_2(n):
    array = []
    for i in range(1,n+1):
        for j in range(1,i+1):
            array.append(j)
    return array
#print(ex4_2(10))

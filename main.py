# Fonction primaire
# Nom du fichier à lire

def question1(nom):
    print(f"Je vais ouvrir le fichier {nom}")
    fichier = open(nom,'r', encoding='utf-8')
    cpt=1
    for ligne in fichier:
        ligne=ligne.rstrip("\n\r")
        print(f"ligne {cpt} : {ligne}")
        cpt+=1

    fichier.close()

def question2(nom):
    print(f"Explorateur du fichier {nom}")
    fichier = open(nom,'r', encoding='utf-8')

    fichier.readline()

    for ligne in fichier:
        ligne = ligne.rstrip("\n\r")
        liste = ligne.split(";")
        print(liste[2])

def question3(nom):
    print(f"Explorateur du fichier {nom}")
    fichier = open(nom, 'r', encoding='utf-8')

    cpt=1
    etudiants = {}

    for ligne in fichier:
        ligne=ligne.rstrip("\n\r")
        print(f"ligne {cpt} : {ligne}")
        cpt+=1

    for ligne in fichier:
        liste = ligne.split(";")
        dict = {}
        dict ["nom"] = liste[2]
        dict ["prenom"] = liste[3]
        dict ["numéro"] = liste[0]
        dict ["classe"] = liste[4]
        dict ["note"] = liste[5]

    if liste[1] not in etudiants:
        etudiants [liste[1]] = dict

    fichier.close()

    return etudiants




if __name__ == '__main__':
    question3("C:\\test\\test.txt")

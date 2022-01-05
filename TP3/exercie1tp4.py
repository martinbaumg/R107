debut = int(input("Entrez le début de la table : "))
table = int(input("Entrez la table de multiplication : "))
fin = int(input("Entrez la fin de la table : "))

while debut <= fin:
    print("{} x {} = {}".format(debut, table, debut * table))
    debut += 1

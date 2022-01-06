nomlist = []
for i in range(0,2):
    prenom = str(input("Prénom : "))
    nom = str(input("Nom : "))
    nomlist.append(" ".join([nom.upper(),prenom.capitalize()]))
nomlist = sorted(nomlist, key=str.lower)
for item in nomlist:
    temp = item.split()
    print(temp[1],temp[0])
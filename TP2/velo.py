débutloc = int(input("Donnez l'heure de début de la location (un entier) : "))
finloc = int(input("Donnez l'heure de fin de la location : "))


if 0 < débutloc < 7 and 17 < débutloc < 24 :
    x = 1

else 7 < débutloc < 17 :
    x = 2

if 0 < finloc < 7 and 17 < finloc < 24 :
    y = 1

else 7 < finloc < 17 :
    y = 2




print("Vous avez loué votre vélo \n{} heure(s) au tarif de horaire de 1.0 euro(s) \n{} heure(s) au tarif horaire de 2.0 euro(s) \nLe montant total à payer est de 16.0 euro(s).".format(débutloc, finloc))
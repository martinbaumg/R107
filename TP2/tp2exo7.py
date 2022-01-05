while True:
    try:
        start = int(input("Heure de début : "))
        end = int(input("Heure de fin : "))
    except ValueError:
        print("Entrez un nombre entier!\n")
        continue

    if start in range(25) and end in range(25):
        if start != end:
            if start < end:
                break
            else:
                print("Attention ! le début de la location est après la fin ...\n")
        else:
            print("Attention ! l’heure de fin est identique à l’heure de début.\n")
    else:
        print("Les heures doivent être comprises entre 0 et 24 !\n")
location = []
for i in range(start, end): location.append(i)

heuresPleine, heuresCreuses = 0, 0
for i in location:
    if i in range(7, 17):
        heuresPleine += 1
    else:
        heuresCreuses += 1

if heuresCreuses != 0: print(heuresCreuses, " heure(s) au tarif de 1€.")
if heuresPleine != 0: print(heuresPleine, " heure(s) au tarif de 2€.")
print(f"Le montant total à payer de {heuresCreuses + 2 * heuresPleine}€.")
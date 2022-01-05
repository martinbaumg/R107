nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
notes = []

for i in range(nombreEtudiants):
    note = float(input(f"Note étudiant {i + 1}: "))
    while 0 > note or note > 20:
            note = float(input(f"Note étudiant {i + 1}: "))

    notes.append(note)
    moyenne += note

moyenne = moyenne/nombreEtudiants
print(f"moyenne de la classe : {moyenne}")

print(f"Numéro de l'étudiant | note | écart à la moyenne")

for i in range(nombreEtudiants):

    print(f"{i} | {notes[i]} | {moyenne-notes[i]}")
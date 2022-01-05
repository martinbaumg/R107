nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
notes = []

for i in range(nombreEtudiants):
    while True:
        try:
            note = float(input(f"Note étudiant {i + 1}: "))
            if 0 <= note <= 20:
                notes.append(note)
                moyenne += note

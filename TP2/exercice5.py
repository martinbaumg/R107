x = int(input("entrez un nombre entier : "))

if x >= 0 and x%2 == 0 :
    print("Le nombre est positif et pair")
elif x >= 0 and x%2 != 0 :
    print("le nombre est positif et impair")
elif x < 0 and x%2 == 0 :
    print("Le nombre est négatif et pair")
elif x < 0 and x%2 != 0 :
    print("Le nombre est négatif et impair")
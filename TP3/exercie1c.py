a = 0
b = 0
c = 0

for i in range(10):
    n = float(input("donnez 10 veleurs : "))
    while n > 20 or n < 0:
        n = float(input("votre valeur ne rentre pas das l'intervalle, saisissez-en une autre : "))
    if n < 10 :
        a = a+1
    elif n > 15:
        b = b+1
    else :
        c = c+1
print("nombre de valeurs inférieur à 10 : {} \nnombre de valeurs supérieur à 15 : {}\nnombre de valeurs supérieur à 10 et inférieur strictement à 15 : {}".format(a, b, c))
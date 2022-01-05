import random

x = random.randint(0,100)
print(x)
n = int(input("Saisissez une valeur pour essayer de trouver la valeur : "))
print(n)
z = 0

while n != x :
    if n < x :
        print("La valeur saissie est trop petite")
        n = int(input("ressaisissez une valeur : "))
        z = z+1
    else :
        print("La valeur est trop grande")
        n = int(input("ressaisissez une valeur : "))
        z = z+1
print("bravo mais vous avez fait {} essais pour réussir".format(z))
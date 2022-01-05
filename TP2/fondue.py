BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400

nbConvives = int(input("Entrez le nombre de personne(s) conviés à la fondue : "))

nfromage = ((fromage*nbConvives)/BASE)
neau = ((eau*nbConvives)/BASE)
nail = ((ail*nbConvives)/BASE)
npain = ((pain*nbConvives)/BASE)

print("Pour faire une fondue fribourgeoise pour {} personnnes, il vous faut : \n- {} gr de fromage\n- {}dl d'eau\n- gousse(s) d'ail\n- {}gr de pain".format(nbConvives, nfromage, neau, nail, npain))

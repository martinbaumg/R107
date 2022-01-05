#import time

#n = int(input("donnez une valeur pour le compte à rebours: "))

#while n >= 0:
    #print(n)
  #  time.sleep(0.2)
 #   n = n-1
#print("voila")



import time

e = int(input("donnez une valeur pour le compte à rebours : "))
print(e)

for i in range(e):
    e = e - 1
    time.sleep(0.2)
    print(e)
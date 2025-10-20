zahl1 = int(input("Zahl 1: "))
zahl2 = int(input("Zahl 2: "))
if zahl2 < zahl1 and zahl1 > 5:
    temp = zahl1
    zahl1 = zahl2
    zahl2 = temp
else:
    if zahl1 == zahl2:
        zahl1 = 5
    zahl2 = 8
print("Ausgabe 1 =", zahl1)
print("Ausgabe 2 =", zahl2)



#Zahl 1: 6
#Zahl 2: 3
#Ausgabe 1 = 3
#Ausgabe 2 = 6

#Zahl 1: 7
#Zahl 2: 7
#Ausgabe 1 = 5
#Ausgabe 2 = 8
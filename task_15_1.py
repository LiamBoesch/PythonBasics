
#Kompilierfehler bei Zeile: 19
#Grund: else darf keine bedingungen enthalten
#Korrektur: Elseif

01  anzahl = 1
02  wert1 = 0
03  wert2 = 0
05  wert3 = 0
06  max_wert = 0
07
08  wert1 = float(input("Wert " + str(anzahl) + ": "))
09  anzahl += 1
10
11  wert2 = float(input("Wert " + str(anzahl) + ": "))
12  anzahl += 1
13
14  wert3 = float(input("Wert " + str(anzahl) + ": "))
15  anzahl += 1
16
17  if wert1 > wert2 and > wert3:
18      max_wert = wert1
19  else wert3 > wert2:
20          max_wert = wert3
21
22  print("Der grösste Wert ist:", max_wert)
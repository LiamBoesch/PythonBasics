#4.2 und 3.5 Ausgabe = typ 1 weil:schnitt = kleiner als 4 und 4.2 ist grösser als 4
#5.2 und 5.8 Ausgabe = typ4 weil schnitt ist grösser als 4 aber nicht 4 und nicht 5 und 5.2 und 5.8 sind grösser als 4
#3.3 und 3.8 Ausgabe = typ0 weil schnitt = kleiner als 4 und 3.3 und 3.8 = kleiner als 4

anzahl = 0
note1 = 0.0
note2 = 0.0
note1 = float(input("Note 1:"))
anzahl += 1
note2 = float(input("Note 2:"))
anzahl += 1
schnitt = (note1 + note2) / anzahl
if schnitt >= 4:
    print("*****")
    durchschnitt = int(schnitt * 2)
    durchschnitt = (durchschnitt + 1) // 2
    if durchschnitt == 4:
        print("Typ 2")
    else:
        if durchschnitt == 5:
            print("Typ 3")
        else:
            print("Typ 4")
else:
    print("-----")
    if note1 >= 4 or note2 >= 4:
        print("Typ 1")
    else:
        print("Typ 0")
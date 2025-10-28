geschlecht = input("Geschlecht (m/w): ")
gewicht = float(input("Gewicht in kg: "))

if geschlecht == "m":
    if gewicht <= 55:
        klasse = "Fliegengewicht"
    elif gewicht <= 66:
        klasse = "Leichtgewicht"
    elif gewicht <= 84:
        klasse = "Mittelgewicht"
    else:
        klasse = "Schwergewicht"

elif geschlecht == "w":
    if gewicht <= 48:
        klasse = "Fliegengewicht"
    elif gewicht <= 55:
        klasse = "Leichtgewicht"
    elif gewicht <= 63:
        klasse = "Mittelgewicht"
    else:
        klasse = "Schwergewicht"

else:
    klasse = "Ungültiges Geschlecht"

print("Gewichtsklasse:", klasse)
``
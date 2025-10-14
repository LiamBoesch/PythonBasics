groesse = float(input("Wie gross bist du in metern"))
gewicht = float(input("Wie schwer bist du in kg"))

groesseQ = (groesse * groesse)
BMI = (gewicht / groesseQ)
print(f"Dein BMI beträgt {BMI}")
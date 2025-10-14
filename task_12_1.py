Stunden = float(input("Stunden:"))
Minuten = float(input("Minuten:"))
Sekunden = float(input("Sekunden:"))

metrische_stunden = Stunden + (Minuten / 60) + (Sekunden / 3600)

print(f"Die umgerechnete Zeit im metrischen System ist {metrische_stunden:.2f} Stunden.")

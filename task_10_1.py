distanz = float(input("Welche distannz möchtest du auf deiner reise zurücklegen"))
Geschwindikeit = float(input("Wie schnell fährst du durchschnittlich in kmh"))
verbrauch = float(input("wie viele Liter verbraucht dein Auto auf 100km" ))
tatverbrauch = (distanz * verbrauch / 100)
fahrtzeit = (distanz / Geschwindikeit * 60)

print(f"Für diese reise beträgt dein Fahrzeit {fahrtzeit} minuten und dein verbrauch auf {distanz}KM ist {tatverbrauch} Liter")
schleife = 0
while schleife < 1:
    passwort = input("Gib ein sicheres Passwort ein")
    sicherheitstufepasswort = len(passwort)
    if sicherheitstufepasswort >= 8:
        print("perfekt! Dieses Passwort ist sicher")
        schleife += 1
    else:
        print("Das Passwort muss mindestens 8 zeichen haben versuche es erneut") 
        
        
        
schleife = 0
while schleife < 1:
    passwort = input("Gib ein sicheres Passwort ein")
    sicherheitsstufepasswort = len(passwort)
    if sicherheitsstufepasswort >= 8:
        print("perfekt! Dieses Passwort ist sicher")
        schleife += 1
    else:
        print("Das Passwort muss mindestens 8 zeichen haben versuche es erneut")

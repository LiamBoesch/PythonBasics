zahl1 = int(input("sag mir eine Zahl"))
unteregrenze = 10
oberegrenze = 20
if unteregrenze <= zahl1 <= oberegrenze :
    print(F"{zahl1} ist zwischen {unteregrenze} und {oberegrenze}") 
else:
    print(f"{zahl1} liegt nicht zwischen {unteregrenze} und {oberegrenze}")
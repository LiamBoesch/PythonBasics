zahl1 = int(input("sag mir eine Zahl"))
unteregrenze = 0
oberegrenze = 100
if unteregrenze <= zahl1 <= oberegrenze :
    print(F"{zahl1} ist zwischen {unteregrenze} und {oberegrenze}") 
elif zahl1 < unteregrenze:
    print(f"{zahl1} ist kleiner als {unteregrenze}")
elif zahl1 > oberegrenze:
    print(f"{zahl1} ist grösser als {oberegrenze}")
else:
    print(f"{zahl1} liegt nicht zwischen {unteregrenze} und {oberegrenze}")
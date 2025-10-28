monat = input("Gib einen Monat ein")
match monat:
    case "Januar":
           print("Winter") 
    case "Februar":
           print("Winter") 
    case "März":
           print("Frühling") 
    case "April":
           print("Frühling") 
    case "Mai":
           print("Frühling") 
    case "Juni":
           print("Sommer") 
    case "Juli":
           print("Sommer")           
    case "August":
           print("Sommer") 
    case "September":
           print("Herbst") 
    case "Oktober":
           print("Herbst") 
    case "November":
           print("Herbst") 
    case "Dezember":
           print("Winter") 
    case _: 
           print("Ungültiger Monat")                         
s
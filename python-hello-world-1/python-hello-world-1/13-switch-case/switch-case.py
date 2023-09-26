print("Wähle Sie bitte ein Produckt aus:")

while True:
    
    print("1 - Käse")
    print("2 - Butter")
    print("3 - Brot")
    print("4 - Fisch")
    
    nutzerEingabe = input("Produkte: ")
    
    match int(nutzerEingabe):
        case 1:
            print("Käse wurde ausgewählt.")
            break
        case 2:
            print("Butter wurde ausgewählt.")
            break
        case 3:
            print("Brot wurde ausgewählt.")
            break 
        case 4:
            print("Fisch wurde ausgewählt.")
            break
        case _:
            print("Falsche Eingabe")
            
    
    
    
"""
    if int(nutzerEingabe) == 1:
        print("Käse wurde ausgewählt.")
        break
    elif int(nutzerEingabe) == 2:
        print("Butter wurde ausgewählt.")
        break
    elif int(nutzerEingabe) == 3:
        print("Brot wurde ausgewählt.")
        break
    elif int(nutzerEingabe) == 4:
        print("Fisch wurde ausgewählt.")
        break
    elif 0 > int(nutzerEingabe) or int(nutzerEingabe) > 4:
        print("Falsche Eingabe")
"""
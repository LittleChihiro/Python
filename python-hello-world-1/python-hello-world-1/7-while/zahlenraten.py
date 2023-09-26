print("Zahlenraten")
print("Ich weiß eine Zahl - weißt Du sie auch?")

schaetzung = -1
zahl = 42

while schaetzung != zahl:
    eingabe = input("Deine Schätzung (ganze Zahl) (c fuer Abbruch): ")
    
    if eingabe == "c":
        break
        
    if eingabe.isdigit():
        schaetzung = int(eingabe)

        if schaetzung == zahl:
            print ("Glückwunsch, du hast gewonnen!")
        elif schaetzung > zahl:
            print("Deine Eingabe ist grosser als die Zahl")
        elif schaetzung < zahl:
            print("Deine Eingabe ist kleiner als die Zahl")
    else: 
        print("Fehler: du musst schon eine Zahl eingeben!")
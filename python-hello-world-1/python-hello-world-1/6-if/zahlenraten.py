print("Zahlenraten")
print("Ich weiß eine Zahl - weißt Du sie auch?")

zahl = 42

eingabe = input("Deine Schätzung (ganze Zahl): ")

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
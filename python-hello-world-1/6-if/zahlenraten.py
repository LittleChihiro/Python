print("Zahlenraten")
print("Ich weiß eine Zahl - weißt Du sie auch?")

zahl = 42

eingabe = int(input("Deine Schätzung (ganze Zahl): "))

if eingabe == zahl:
    print ("Glückwunsch, du hast gewonnen!")
elif eingabe > zahl:
    print("Deine Eingabe ist grosser als die Zahl")
elif eingabe < zahl:
    print("Deine Eingabe ist kleiner als die Zahl")
else: 
    print("Leider hast du nicht die Zahl erraten")
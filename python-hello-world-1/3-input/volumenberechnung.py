#Ueberschrift
print("Volumenberechnung eines Quaders")

print("Bitte gib die folgenden Seitenlängen ein:")

#Eingaben
eingabe_a = input("Länge von Seite a: ")
eingabe_b = input("Länge von Seite b: ")
eingabe_c = input("Länge von Seite c: ")

if eingabe_a.isdigit() and eingabe_b.isdigit() and \
eingabe_c.isdigit(): 
    
    #Variablen
    a = float(eingabe_a)
    b = float(eingabe_b)
    c = float(eingabe_c)

    #Volumen berechner
    volumen = a * b * c

    #Ausgabe der Seitenlaenge
    print("Seite a: {0}, Seite b: {1}, Seite c: {2}" .format(a, b, c))

    #Ausgabe des Ergebniss
    print("Ergebnis: {0}" . format(volumen))
    
else:
    print("Eine deiner Eingaben hat nicht nur Zahlen drinen ")


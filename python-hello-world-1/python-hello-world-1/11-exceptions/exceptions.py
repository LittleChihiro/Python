
print("Volumenberechnung eines Quaders")

print("Bitte gib die folgenden Seitenlängen ein:")

eingabe_fehlerfrei = False
while not eingabe_fehlerfrei:
    try:
        a = float(input("Länge von Seite a: "))
        b = float(input("Länge von Seite b: "))
        c = float(input("Länge von Seite c: "))
        eingabe_fehlerfrei = True
    except ValueError:
        print("Fehler! Eine Eingabe war nicht valide")
    finally: 
        print("Eingabe abgeschlossen")
        
        
volumen = a * b * c

print("Seite a: {0}, Seite b: {1}, Seite c: {2}" .format(a, b, c))

print("Ergebnis: {0}" . format(volumen))
        
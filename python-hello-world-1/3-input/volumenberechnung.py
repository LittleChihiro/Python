#Ueberschrift
print("Volumenberechnung eines Quaders")

print("Bitte gib die folgenden Seitenlängen ein:")
#Variablen
a = float(input("Länge von Seite a: "))
b = float(input("Länge von Seite b: "))
c = float(input("Länge von Seite c: "))

#Volumen berechner
volumen = a * b * c

#Ausgabe der Seitenlaenge
print("Seite a: {0}, Seite b: {1}, Seite c: {2}" .format(a, b, c))

#Ausgabe des Ergebniss
print("Ergebnis: {0}" . format(volumen))


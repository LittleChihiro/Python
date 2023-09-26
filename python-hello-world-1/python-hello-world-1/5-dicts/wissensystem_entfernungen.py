#entfernung in 10^6 km
entfernungen = {
    "Merkur": 58000,
    "Venus": 108,
    "Erde": 150,
    "Mars": 228,
    "Jupiter": 778,
    "Saturn": 1427,
    "Uranus": 2884,
    "Neptun": 4509
}

#Umrechnung von km in Zieleinheit
umrechnungen = {
    "km": 1,
    "m": 1000,
    "dm": 10000,
    "cm": 100000,
}

angefragte_planet = input("Bitte gib den Namen des Planet an: ")
angefragte_einheit = input("In welcher Einheit soll die Entfernung zur Sonne "+\
                           "angezeigt werden? ")

ergebnis = entfernungen[angefragte_planet] * 1000000 * \
    umrechnungen[angefragte_einheit]
    
print("Der Planet {0} hat eine Entfernung von {1} {2} zur Sonne." .format(
       angefragte_planet, ergebnis, angefragte_einheit 
    ))
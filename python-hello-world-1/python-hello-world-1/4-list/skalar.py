vektor1 = []
vektor2 = []

vektor1.append(float(input("Vektor1 Koordinate 1: ")))
vektor1.append(float(input("Vektor1 Koordinate 2: ")))
vektor1.append(float(input("Vektor1 Koordinate 3: ")))

vektor2.append(float(input("Vektor2 Koordinate 1: ")))
vektor2.append(float(input("Vektor2 Koordinate 2: ")))
vektor2.append(float(input("Vektor2 Koordinate 3: ")))

skalarprodukt = vektor1[0] * vektor2[0] + \
    vektor1[1] * vektor2[1] + \
    vektor1[2] * vektor2[2]
        
print("Das Skalarprodukt ist {0}" .format(skalarprodukt))

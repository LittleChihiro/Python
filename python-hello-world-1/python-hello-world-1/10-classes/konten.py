
class Konto(object):
    __kontostand = 0
    kontonummer = 1000
    inhaber = ""
    
    def __init__(self, kontonummer):
        self.kontonummer = kontonummer
        print("Konto {0} initiasiert".format(kontonummer))
    
    def einzahlen(self, betrag):
        if betrag > 0:
            self.__kontostand = self.__kontostand + betrag
            print("Der Betrag von {0} € wurde eingezahlt".format(
                self.__kontostand)
                  )
            print("Neuer Kontostand: " + str(self.__kontostand) + " €")
        else: 
            print("Der Betrag muss positiv und grosser 0 sein.")
            
            
    def abheben(self, betrag):
        if betrag > 0:
            self.__kontostand = self.__kontostand - betrag
            print("Der Betrag von {0} € wurde abgehoben".format(
                self.__kontostand)
                  )
            print("Neuer Kontostand: " + str(self.__kontostand) + " €")
        else: 
            print("Der Betrag muss positiv und grosser 0 sein.")
            
    def kontostand(self):
        return self.__kontostand
        

class JungesKonto(Konto):
    erzieungsberechtingte = []
    
    def abheben(self, betrag):
        if self.kontostand() - betrag >= 0:
            super().abheben(betrag)
        else: 
            print("Konto nicht gedeckt")

class Konto(object):
    kontostand = 0
    kontonummer = 1000
    inhaber = ""
    
    def einzahlen(self, betrag):
        if betrag > 0:
            self.kontostand = self.kontostand + betrag
            print("Der Betrag von {0} € wurde eingezahlt".format(
                self.kontostand)
                  )
            print("Neuer Kontostand: " + str(self.kontostand) + " €")
        else: 
            print("Der Betrag muss positiv und grosser 0 sein.")
            
            
    def abheben(self, betrag):
        if betrag > 0:
            self.kontostand = self.kontostand + betrag
            print("Der Betrag von {0} € wurde abgehoben".format(
                self.kontostand)
                  )
            print("Neuer Kontostand: " + str(self.kontostand) + " €")
        else: 
            print("Der Betrag muss positiv und grosser 0 sein.")
            
    def abheben(self, betrag):
        if betrag > 0:
            self.kontostand = self.kontostand - betrag
            print("Der Betrag von {0} € wurde abgehoben".format(
                self.kontostand)
                  )
            print("Neuer Kontostand: " + str(self.kontostand) + " €")
        else: 
            print("Der Betrag muss positiv und grosser 0 sein.")
            
            
            
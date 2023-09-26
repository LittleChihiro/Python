import programmutils
from konten import Konto, JungesKonto

programmutils.greeter()
a = Konto(123456)
b = JungesKonto(12345678)

a.einzahlen(100)
b.einzahlen(200)

summe = programmutils.sum(a.kontostand(), b.kontostand())
print(summe)
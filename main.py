# import datetime
from datetime import datetime

x = datetime.now()
rok = x.year
miesiac = x.month
dzien = x.day
print(f"{dzien}/{miesiac}/{rok}")

data = x.strftime("%d/%m/%Y, %H:%M:%S")

print(data)



# Zmienna
# nazwa = wartosc
# obliczenie = 100 * 100 / 20 + 7
# imie = "Anna"
#
# print(obliczenie)
# print(imie)
# print("imie")
#
# czesc = "jakieś powitanie"
# print(czesc)
# print("witam wszystkich")

nazwisko = "Kowalski"
# print(nazwisko)

# rok = 2025
# print(rok)
# rok = 2026
# print(rok)

# sneak case
kwota_do_zaplaty = 120

# camel case
kwotaDoZaplaty = 120

# STAŁA
# NAZWA_BAZY = "mysql_db"
# PORT = 3303

# bardziej zaawansowany sposób na stałe
# CTRL + / komentowanie wiele linijek na raz
class Config:
    port = 3303
    host = "localhost"
#
# print(Config.port)









# str (string)
# Typ prosty / prymitywny

# miasto = "Katowice"
# nazwisko = 'Kowalski'
#
# sprawdz_typ = type(nazwisko)
# fraza = "John's"
#
# # Konkatenacja
# jezyk = "Python"
# typ_jezyka = "backendowy"
#
# zdanie = jezyk + " to popularny język programowania"
# zdanie2 = "Mój ulubiony język to " + jezyk + ". Jest on " + typ_jezyka + "."
# # f string - Python 3.10
# zdanie3 = f"Mój ulubiony język to {jezyk}. Jest on {typ_jezyka}."
#
# print(zdanie2)
# print(zdanie3)


film = "haRRy pOtTer: Zakon Feniksa"

duza_litera = film.upper()
tytul = film.title()
zastap_znaki = tytul.replace("r","_")
zastap_fraze = film.replace("Zakon Feniksa", "Czara Ognia")

policz = film.count("R")
policz_bez_czulosci_na_litery = film.lower().count("r")



akapit = "To jest mój tekst"

pierwsza_litera = akapit[0]
ostatnia_litera = akapit[-1]
fragment = akapit[0:7]
rozpocznij_od = akapit[5::]

print(rozpocznij_od)




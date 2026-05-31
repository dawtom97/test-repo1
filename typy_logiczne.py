# # bool
# # Typ prosty / prymitywny
# from main import miesiac
#
# prawda = True
# falsz = False
#
# # Bool mogę uzyskać z wyniku metody
# a = "ABC"
# sprawdz1 = a.isnumeric()
# sprawdz2 = a.islower()
#
# # Bool mogę uzyskać z operatorów logicznych
#
# x = 7 > 4 # większe od
# y = 8 < 4 # mniejsze od
# z = 10 >= 10 # większe bądź równe
# h = 10 <= 12 # mniejsze bądź równe
# rowne = "abc" == "abcd" # porównanie
#
#
# a = 15
#
# # Blok kodu if
# # odpali się jeśli warunek spełniony
# # if a >= 10:
# #     print("zgadza się")
# #     print("kolejna operacja")
# #     print("jeszcze jedna")
# # else:
# #     print("liczba jest za mała")
#
# # typ_konta = "mod"
# #
# # if typ_konta == "admin":
# #     print("witaj w panelu admina")
# # elif typ_konta == "mod":
# #     print("witaj moderatorze")
# # elif typ_konta == "klient":
# #     print("witaj klient")
# # else:
# #     print("nie rozpoznano")
#
#
# # koszyk = 98.00
# # kod = "ABC"
# # kraj = "PL"
# #
# #
# # if koszyk > 150 or kod == "ABC2026":
# #     print("uzyskano rabat")
# # else:
# #     print("brak rabatu")
#
# login = "admin"
# dzien = "sobota"
# aktualizacja = True
#
# if login == "admin123" and (dzien == "sobota" or aktualizacja):
#     print("można przeprowadzić update")
#
# # skrótowy zapis
# # falszywe i prawdziwe
# # negacje
#
#
#
# # if koszyk >= 200 and kod == "ABC2026" and kraj == "PL":
# #     koszyk *= 0.9
# #     print(f"Uzyskałeś rabat!!. Do zapłaty {koszyk} zł")
# # else:
# #     print("Nie udało się uzyskać rabatu")
#
#
#
#
#
# # user_country = "Polska"
# # if user_country in ["Polska", "Niemcy", "Czechy"]:
# #     print("Dostawa możliwa")
# # else:
# #     print("Dostawa towaru niemożliwa")
#
#
# from datetime import datetime
#
# # user_role= "admin"
# # is_logged=True
#
# # jeśli zmienna is_logged ma wartość
# # którą mogę przekonwartować na True
# # if is_logged:
# #     print("jesteś zalogowany")
#
# # Do prawdy: -99...99, "..",[...], {...}, (...)
# # Do fałszu: 0,"", None,[],{},()
#
# # konwersja = bool(12)
# #
# # print(konwersja)
#
#
# # skrótowy zapis
# # falszywe i prawdziwe
#
#
# # negacje
#
#
# email = None
#
# # logowanie....
#
# # email = "jan@gmail.com"
# #
# # if email:
# #     inicjaly = email[0].upper()
# #     print(inicjaly)
#
#
# zalogowany = False
#
# wiadomosc = "Witaj w apce" if zalogowany else "Musisz się zalogować"
#
# # print(wiadomosc)
#
# # zmienne
# # typy danych (string i int/float)
# # instrukcje warunkowe: if..else
#
#
# user_role = "A"
# is_logged = True

# Instrukcja match

# match(user_role):
#     case "ADMIN" | "A": # or
#         print("witaj adminie")
#     case "MOD":
#         print("witaj w panelu moderatora")
#     case "USER":
#         print("Panel klienta")
#     case _:
#         print("Wystąpił błąd")
#
#
# from datetime import datetime
#
# month = datetime.now().month

# match(month):
#     case 1:
#         miesiac = "Styczeń"
#     case 5:
#         miesiac = "Maj"
#     case 12:
#         miesiac = "Grudzień"
#     case _:
#         miesiac = "Brak"
#
# print(miesiac)

# TRY...EXCEPT

# print("aplikacja działa 1")
#
# print("aplikacja działa 2")
#
# try:
#     print("try 1")
#     print(zmienna)
#     print("try 2")
# except:
#     print("złapałem błąd!")
# finally:
#     print("Operacja zakończona")
#
# print("aplikacja działa 3")


# try:
#     print(zmienna)
# except Exception as e:
#     print("Skontaktuj się z administratorem")
#     print(e)

x = input("Podaj liczbę: ")

# ktoś może: dzielić przez 0, brak liczby, nic nie podać
try:
    dzialanie = 100 / float(x)
    if float(x) == 7:
        raise NameError("Wiadomość błędu")
    print(dzialanie)
except ZeroDivisionError as e:
    print("Nie możesz dzielić przez 0!")
    print(e)
except ValueError as e:
    print("Musisz podać liczbę!")
    print(e)
except NameError as e:
    print("Mój własny błąd! Nie można podac liczby 7")
    print(e)
except Exception as e:
    print("Wystąpił błąd")
    print(e)

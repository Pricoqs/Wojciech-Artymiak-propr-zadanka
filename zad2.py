"""
Stwórz prosty program do kalkulacji cen biletów na różne środki transportu (autobus, pociąg, samolot). Na
początku kod zawiera powtarzające się fragmenty obliczeń dla każdego środka transportu. Twoim
zadaniem jest usunięcie zbędnych powtórzeń, tak aby kod był bardziej zwięzły i łatwiejszy do utrzymania.
"""

typ = input(
    "Wpisz nazwe srodka transportu z jakiego chcesz przeliczyc ceny (autobus/pociąg/samolot)"
)
cena = float(input("Podaj cene srodka transportu"))

if typ == "autobus":
    cena = cena * 1.5
elif typ == "pociąg":
    cena = cena * 3
elif typ == "samolot":
    cena = cena * 10
else:
    print(f"ERROR: brak typu srodka transportu {typ}")

print(f"Przeliczona cena wynosi: {cena}")

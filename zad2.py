"""
Stwórz prosty program do kalkulacji cen biletów na różne środki transportu (autobus, pociąg, samolot). Na
początku kod zawiera powtarzające się fragmenty obliczeń dla każdego środka transportu. Twoim
zadaniem jest usunięcie zbędnych powtórzeń, tak aby kod był bardziej zwięzły i łatwiejszy do utrzymania.
"""

from enum import Enum


class NazwaSrodkaTransportu(Enum):
    autobus = 0
    pociag = 1
    samolot = 2


typyPojazdow = {
    NazwaSrodkaTransportu.autobus: 1.5,
    NazwaSrodkaTransportu.pociag: 3,
    NazwaSrodkaTransportu.samolot: 10,
}


def przeliczanieCenBiletow(
    nazwaSrodkaTransportu: NazwaSrodkaTransportu, iloscKilometrow: float
) -> float:
    return iloscKilometrow * typyPojazdow[nazwaSrodkaTransportu]


nazwa = input(
    "Wpisz nazwe srodka transportu na podstawie jakiego jakiego chcesz przeliczyc ceny biletow (autobus/pociąg/samolot): "
)
nazwaSrodkaTransportu = NazwaSrodkaTransportu[nazwa]

iloscKilometrow = float(
    input(
        "Ile kilometrow przemierzysz przemieszczajac sie podanym srodkiem transportu: "
    )
)

print(
    f"Przeliczona cena wynosi: {przeliczanieCenBiletow(nazwaSrodkaTransportu, iloscKilometrow)}"
)

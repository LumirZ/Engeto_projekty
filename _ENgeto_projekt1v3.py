"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lumír Zeman
email: lumir.zeman@seznam.cz
discord: rulik.luzem
"""

# zadání základních proměnných pro přístup k analýze textu
username = input("Zadejte své přihlašovací jméno: ")
password = input("Zadejte heslo: ")
uzivatele = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
         '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
         '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
         ]
oddělovač = "----------------------------------------"

# kontrola oprávněného uživatele pro přístup k analýze textu
if uzivatele.get(username) == password:
    print(oddělovač)
    print("Welcome to the app,", username)
    print("We have 3 texts to be analyzed.")
    print(oddělovač)
else:
    print("unregistered user, terminating the program..")
    exit()

# výběr textu k analýze a základní statistika analýzy vybraného textu včetně nové statistiky
#slov kombinujících čísla a písmena
version = input("Enter a number btw. 1 and 3 to select: ")
if not version.isnumeric() or int(version) not in range(1, 4):
    print("Terminating the program..")
    exit()
else:
    bezinter = TEXTS[int(version) - 1].replace(",", "").replace(".", "").replace("-", "")
    print("There are", len(bezinter.split()), "words in the selected text.")
    print("There are", sum(1 for slovo in bezinter.split() if slovo.istitle() and slovo.isalpha()),
          "titlecase words.")
    print("There are", sum(1 for slovo in bezinter.split() if slovo.isupper() and slovo.isalpha()),
          "uppercase words.")
    print("There are", sum(1 for slovo in bezinter.split() if slovo.islower()), "lowercase words.")
    print("There are", sum(1 for slovo in bezinter.split() if slovo.isnumeric()), "numeric strings.")
    print("There are", len(bezinter.split()) - sum(1 for slovo in bezinter.split() if slovo.isalpha())
          - sum(1 for slovo in bezinter.split() if slovo.isnumeric()),
          "combination of alphanumeric strings.")
    cisla = []
    for slovo in bezinter.split():
        if slovo.isnumeric():
            cisla.append(int(slovo))
    print("The sum of all the numbers", sum(cisla))

# detailní statistika textu pro sloupcový graf
# 1_příprava hodnot
pocet_slov = []
for slovo in bezinter.split():
    delka_slova = len(slovo)
    pocet_slov.append(delka_slova)

pocet_unique = dict()
for cislo in pocet_slov:
    if cislo not in pocet_unique:
        pocet_unique[cislo] = 1
    else:
        pocet_unique[cislo] += 1

sorted_pocet = dict(sorted(pocet_unique.items()))

# detailní statistika textu pro sloupcový graf
# 2_tisk hlavičky a hodnot do grafu s dynamickou šíří sloupců
hodnoty_grafu = list(sorted_pocet.values())
hodnoty_grafu.sort()
print(oddělovač)
if hodnoty_grafu[-1] % 2 == 0:
    print("LEN|" + (" " * (abs((hodnoty_grafu[-1] + 1) - 10) // 2)) + "OCCURENCES"
          + (" " * ((abs((hodnoty_grafu[-1] + 1) - 10) // 2) + 1)) + "|NR.")
else:
    print("LEN|" + (" " * (abs((hodnoty_grafu[-1] + 1) - 10) // 2)) + "OCCURENCES"
          + (" " * (abs((hodnoty_grafu[-1] + 1) - 10) // 2)) + "|NR.")
print(oddělovač)
for cislo in sorted_pocet:
    if cislo < 10:
        print("  " + str(cislo) + "|" + "*" * sorted_pocet.get(cislo) + " " * ((hodnoty_grafu[-1] + 1)
              - sorted_pocet.get(cislo)) + "|" + str(sorted_pocet.get(cislo)))
    else:
        print(" " + str(cislo) + "|" + "*" * sorted_pocet.get(cislo) + " " * ((hodnoty_grafu[-1] + 1)
              - sorted_pocet.get(cislo)) + "|" + str(sorted_pocet.get(cislo)))

"""
Dynamická šíře sloupců, se mi zdá vhodnější pro zachování vzhledu tištěného výstupu a
vypadá lépe pro všechny 3 varianty textu, i případný update textů. Samozřejmě,
pouze za podmínky, že nejdelší slovo nebude menší než 10 písmen. 
"""

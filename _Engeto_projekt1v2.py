"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lumír Zeman
email: lumir.zeman@seznam.cz
discord: rulik.luzem
"""
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
if uzivatele.get(username) == password:
    print("----------------------------------------")
    print("Welcome to the app,", username)
    print("We have 3 texts to be analyzed.")
    print("----------------------------------------")
else:
    print("unregistered user, terminating the program..")
    exit()
version = int(input("Enter a number btw. 1 and 3 to select: "))
if version not in range(1, 4):
    print("Terminating the program..")
    exit()
else:
    print("There are", len(TEXTS[version - 1].split()), "words in the selected text.")
    print("There are", sum(1 for slovo in TEXTS[version - 1].split() if slovo.istitle()), "titlecase words.")
    print("There are", sum(1 for slovo in TEXTS[version - 1].split() if slovo.isupper()), "uppercase words.")
    print("There are", sum(1 for slovo in TEXTS[version - 1].split() if slovo.islower()), "lowercase words.")
    print("There are", sum(1 for slovo in TEXTS[version - 1].split() if slovo.isnumeric()), "numeric strings.")
    cisla = []
    for slovo in TEXTS[version - 1].split():
        if slovo.isnumeric():
            cisla.append(int(slovo))
    print("The sum of all the numbers", sum(cisla))
print("----------------------------------------")
print("LEN|    OCCURENCES    |NR.")
print("----------------------------------------")
bezinter = TEXTS[version - 1].replace(",", "").replace(".", "").replace("-", "")
slovo_1 = "1"
slovo_1_sum = sum(1 for slovo in bezinter.split() if len(slovo) == 1)
print(f"{slovo_1:>3}|{str(slovo_1_sum * '*'):<18}|{str(slovo_1_sum)}")
slovo_2 = "2"
slovo_2_sum = sum(1 for slovo in bezinter.split() if len(slovo) == 2)
print(f"{slovo_2:>3}|{str(slovo_2_sum * '*'):<18}|{str(slovo_2_sum)}")
slovo_3 = "3"
slovo_3_sum = sum(1 for slovo in bezinter.split() if len(slovo) == 3)
print(f"{slovo_3:>3}|{str(slovo_3_sum * '*'):<18}|{str(slovo_3_sum)}")
slovo_4 = "4"
slovo_4_sum = sum(1 for slovo in bezinter.split() if len(slovo) == 4)
print(f"{slovo_4:>3}|{str(slovo_4_sum * '*'):<18}|{str(slovo_4_sum)}")
slovo_5 = "5"
slovo_5_sum = sum(1 for slovo in bezinter.split() if len(slovo) == 5)
print(f"{slovo_5:>3}|{str(slovo_5_sum * '*'):<18}|{str(slovo_5_sum)}")
slovo_6 = "6"
slovo_6_sum = sum(1 for slovo in bezinter.split() if len(slovo) == 6)
print(f"{slovo_6:>3}|{str(slovo_6_sum * '*'):<18}|{str(slovo_6_sum)}")
slovo_7 = "7"
slovo_7_sum = sum(1 for slovo in bezinter.split() if len(slovo) == 7)
print(f"{slovo_7:>3}|{str(slovo_7_sum * '*'):<18}|{str(slovo_7_sum)}")
slovo_8 = "8"
slovo_8_sum = sum(1 for slovo in bezinter.split() if len(slovo) == 8)
print(f"{slovo_8:>3}|{str(slovo_8_sum * '*'):<18}|{str(slovo_8_sum)}")
slovo_9 = "9"
slovo_9_sum = sum(1 for slovo in bezinter.split() if len(slovo) == 9)
print(f"{slovo_9:>3}|{str(slovo_9_sum * '*'):<18}|{str(slovo_9_sum)}")
slovo_10 = "10"
slovo_10_sum = sum(1 for slovo in bezinter.split() if len(slovo) == 10)
print(f"{slovo_10:>3}|{str(slovo_10_sum * '*'):<18}|{str(slovo_10_sum)}")
slovo_11 = "11"
slovo_11_sum = sum(1 for slovo in bezinter.split() if len(slovo) == 11)
slovo_11_mez = (18 - slovo_11_sum) * " "
print(" " + slovo_11 + "|" + str(slovo_11_sum * "*" + slovo_11_mez) + "|" + str(slovo_11_sum))
# poslední dva řádky ponechány k výukovým účelům pro příští generace,
# neboť formátování bylo vysvětleno až výrazně později po zadání projektu.

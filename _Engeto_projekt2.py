"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Lumír Zeman
email: lumir.zeman@seznam.cz
discord: rulik.luzem
"""

# Importuje potřebný modul
import random


# grafický prvek
separator = "----------------------------------------"


# Vrací list jednotlivých číslic daného čísla
def getdigits(number):
    return [int(i) for i in str(number)]


# Vrací hodnotu True, pokud číslo neobsahuje duplicity
# jinak vrací False
def noduplicities(number):
    num_li = getdigits(number)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False


# Generuje 4místné číslo bez duplicitních čísel
def generatenum():
    while True:
        number = random.randint(1000, 9999)
        if noduplicities(number):
            return number


# Vrací úspěšnost odhadu,
# správné číslo i pozice - bulls
# správné číslo, ale ne pozice - cows
def numofbullscows(number, guess):
    bull_cow = [0, 0]
    num_li = getdigits(number)
    guess_li = getdigits(guess)

    for i, j in zip(num_li, guess_li):

        # existence společné číslice
        if j in num_li:

            # přesný zásah - bulls
            if j == i:
                bull_cow[0] += 1

            # správné číslo, ale ne pozice - cows
            else:
                bull_cow[1] += 1

    return bull_cow


# Oslovení a úvod
print("Hi there!")
print(separator)
print("I've generated a random 4 digit number for you."
      "Let's play a bulls and cows game.")
print(separator)


# Generování čísla a omezení pokusů na uhádnutí čísla
number = generatenum()

limit = input("Do you want to limit number of your tries by yourself? (y/n) ")
if limit != "y" and limit != "Y":
    print("All right, you have 30 attempts.")
    tries = 30
else:
    tries = int(input('Enter number of tries: '))

num_of_tries = int()
total = num_of_tries + tries


# Hra probíhá do doby uhádnutí čísla nebo vypršení počtu pokusů
while tries > 0:
    guess = input("Enter a number: ")
    print(separator)
    if not str(guess).isnumeric():
        print("Number should not have letters or symbols, only digits. Try again.")
        continue
    if not noduplicities(guess):
        print("Number should not have repeated digits. Try again.")
        continue
    if int(guess) < 1000 or int(guess) > 9999:
        print("Enter 4 digit number only, without zero at the beginning. Try again.")
        continue

    bull_cow = numofbullscows(number, guess)

    if bull_cow[0] > 1:
        bull = "bulls"
    else:
        bull = "bull"
    if bull_cow[1] > 1:
        cow = "cows"
    else:
        cow = "cow"

    print(f"{bull_cow[0]} {bull}, {bull_cow[1]} {cow}")
    tries -= 1
    num_of_tries += 1

    if bull_cow[0] == 4:
        print(f"Correct, you've guessed the right number in {num_of_tries} of {total} guesses!")
        break
else:
    print(f"Sorry, you ran out of tries. Number was {number}")

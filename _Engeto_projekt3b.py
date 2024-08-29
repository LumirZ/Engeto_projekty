import requests
import bs4


def vstupni_hodnoty(url, vystupni_soubor):
    """
    1. Definuj webový odkaz na konkrétní stránku výsledků voleb dané obce.
    2. Definuj název výstupního souboru ve formátu .csv.
    """
    url = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"
    vystupni_soubor = "vystup_volby.csv"
    return url, vystupni_soubor

def posli_pozadavek_get(url: str) -> str:
    """
    Vrať odpověd serveru na požadavek typu GET.
    """
    response = requests.get(url)
    return response.text

def parsovana_odpoved_main(odpoved: str) -> bs4.BeautifulSoup:
    """
    Získej rozdělenou odpověď na požadavek typu GET.
    """
    soup = bs4.BeautifulSoup(odpoved, features="html.parser")
    table_top = soup.find_all(class_ = "table")
    records = []
    for result in table_top:
        číslo = result.find_all("td", {"class": "cislo"}).text
        obec = result.find_all("td", {"class": "overflow_name"}).text
        records.append((číslo, obec))
    return records


if __name__ == "__main__":
    url: str =  \
        "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"
    odpoved = parsovana_odpoved_main(posli_pozadavek_get(url))
    print(odpoved)

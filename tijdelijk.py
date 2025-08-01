from helper import decoreer

def print_aanbieding():
    prijzen = {
        "aarbei" : 3,
        "vanille" : 4,
        "chocolade" : 5
    }

    aanbieding = prijzen["aarbei"] * 0.8

    reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"

    reclame_tekst2 = reclame_tekst[:63]

    reclame_tekst3 = reclame_tekst2.upper()

    reclame_tekst4 = reclame_tekst3.split()

    for el in reclame_tekst4:
        if len(el) > 4:
            print(el.upper())
        else:
            print(el.lower())

decoreer("Aanbieding")
print_aanbieding()
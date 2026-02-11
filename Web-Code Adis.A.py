# Adis.A
# Web-Code

# Für ein Buchprojekt wird ein Web-Code benötigt.
# Mit diesem Web-Code können Artikel direkt online abgefragt werden.
# Der Code soll aus acht Zeichen bestehen.
# Vorkommen dürfen Ziffern und Kleinbuchstaben.
# Um Verwechslungen zu vermeiden,
# kommen die Ziffer Eins (1) und der Kleinbuchstabe "ell" (l) nicht vor.
# Ebenso kommt die Null (0) nicht vor.
# Dass das große "Oh" (Systemadministration) nicht vorkommen kann, ist klar,
# denn die Vorgabe erlaubt nur Kleinbuchstaben.
#
# Schreibe ein Programm, das fünf zufällige Web-Codes erzeugt.

import random
import string


def generate_web_codes(count=5):
    allowed_chars = 'abcdefghijkmnopqrstuvwxyz23456789'

    print("Fünf zufällige Web-Codes:")
    print("=" * 25)

    for i in range(count):
        code = ''.join(random.choice(allowed_chars) for _ in range(8))
        print(f"{i + 1}. {code}")

generate_web_codes()
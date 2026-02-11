# Adis

# Passwort-Qualität

# Schreibe eine Funktion, die die Qualität von Passwörtern nach
# einem einfachen Punktesystem bewertet.
# Es gelten dabei die folgenden
# Regeln:
# – Passwort mit 7 oder weniger Zeichen: immer 0 Punkte,
# - egal, welche Kriterien noch erfüllt sind.
# – Ab 8 Zeichen: 1 Punkt
# – Enthält sowohl Groß- als auch Kleinbuchstaben: +1 Punkt
# – Enthält MEHR als sechs unterschiedliche Zeichen: +1 Punkt
# – Enthält zumindest eine Ziffer: +1 Punkt
# – Enthält zumindest ein Sonderzeichen: +1 Punkt
# Beispiele:
# – 'abc': 0 Punkte
# – 'abcdefghij': 2 Punkte
# – 'ab1122$$!!': 3 Punkte
# – 'Abcd1234$!': 5 Punkte

def passwort_qualitaet(passwort):
    # Regel 1: Passwort mit 7 oder weniger Zeichen = 0 Punkte
    if len(passwort) <= 7:
        return 0

    punkte = 0

    # Regel 2: Ab 8 Zeichen = 1 Punkt
    punkte += 1

    # Regel 3: Enthält sowohl Groß- als auch Kleinbuchstaben
    hat_grossbuchstabe = False
    hat_kleinbuchstabe = False

    for zeichen in passwort:
        if zeichen.isupper():
            hat_grossbuchstabe = True
        elif zeichen.islower():
            hat_kleinbuchstabe = True

    if hat_grossbuchstabe and hat_kleinbuchstabe:
        punkte += 1

    # Regel 4: Enthält MEHR als sechs unterschiedliche Zeichen
    unterschiedliche_zeichen = set(passwort)
    if len(unterschiedliche_zeichen) > 6:
        punkte += 1

    # Regel 5: Enthält zumindest eine Ziffer
    hat_ziffer = any(zeichen.isdigit() for zeichen in passwort)
    if hat_ziffer:
        punkte += 1

    # Regel 6: Enthält zumindest ein Sonderzeichen
    hat_sonderzeichen = any(not zeichen.isalnum() for zeichen in passwort)
    if hat_sonderzeichen:
        punkte += 1

    return punkte
# Testfälle
testfaelle = [
    'abc',           # 0 Punkte
    'abcdefghij',    # 2 Punkte
    'ab1122$$!!',    # 3 Punkte
    'Abcd1234$!',    # 5 Punkte
]

for pw in testfaelle:
    print(f"'{pw}': {passwort_qualitaet(pw)} Punkte")
























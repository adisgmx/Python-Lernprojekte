# Adis

# Kostenberechnung

"""
Erstelle eine Funktion zur Kostenberechnung.
Dieser wird Preis, Anzahl und Währung als Argumente übergeben
und sie soll daraus die Kosten berechnen und zurückgeben.
Standardmäßig soll die Anzahl 100 betragen
und die Währung Euro sein.

Teste die Funktion:
print(berechne_kosten(2)) # 200 €
print(berechne_kosten(2, 2)) # 4 €
print(berechne_kosten(2, 2, '$')) # 4 $
print(berechne_kosten(2, waehrung='$')) # 200 $
"""

def kosten_berechnung(preis, anzahl=100, waehrung='€'):
    kosten = preis * anzahl
    ergebnis = waehrung
    return f'{kosten} {waehrung}'

print(kosten_berechnung(2))                                  # 200 €
print(kosten_berechnung(2, 2))                  # 4 €
print(kosten_berechnung(2, 2, '€'))   # 4 €
print(kosten_berechnung(2, waehrung='€'))              # 200 €
























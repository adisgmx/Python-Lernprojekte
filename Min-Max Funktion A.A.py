# Adis

# Min-Max-Funktion

# Die in Python vordefinierten Funktionen min() und max() ermitteln
# das kleinste bzw. größte Element einer Liste von Zahlen.
# Programmiere die Funktion min_max(),
# die die beiden entsprechenden Elemente als Tupel zurückgibt,
# ohne min(), max() oder sort()/sorted() zu benutzen.

def min_max(zahlen):
    if not zahlen:
        return None
    minimum = zahlen[0]
    maximum = zahlen[0]

    for zahl in zahlen:
        if zahl < minimum:
            minimum = zahl
        if zahl > maximum:
            maximum = zahl

    return (minimum, maximum)
print(min_max([3, 1, 4, 1, 5, 9, 2]))
print(min_max([-5, 0, 10, -2]))
print(min_max([42]))
print(min_max([]))













# Adis

liste1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
liste2 = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9]
def ist_doppelt(liste):
    for i in range (len(liste)):
        for j in range (i+1, len(liste)):
            if liste[i] == liste[j]:
                return True
    return False

print(ist_doppelt(liste1))
print(ist_doppelt(liste2))









# Funktion berechneKennzahlen
def berechneKennzahlen ():
    # Besetze Variable
    umschlaghäufigkeit = 0.0
    wareneinsatz = 0.0
    dlagerbestand = 0.0
    anfangsbestand = 0.0
    endbestand = 0.0
    einkäufe = 0.0
    dlagerdauer = 0.0

    # Eingabe mit Typkonvertierung
    anfangsbestand = float (input( " Anfangsbestand: " ))
    endbestand = float(input( " Endsbestand: "))
    einkäufe = float (input( " Einkäufe: "))

    # Verarbeitung
    wareneinsatz = anfangsbestand + einkäufe - endbestand
    dlagerbestand = ( anfangsbestand + endbestand ) / 2
    umschlaghäufigkeit = wareneinsatz / dlagerbestand
    dlagerdauer = 360 / umschlaghäufigkeit

    #Ausgabe
    print( " Umschlaghäufigkeit: " , umschlaghäufigkeit)
    print( " Lagerbestand: " , dlagerbestand)
    print( ' Wareneisatz:' , wareneinsatz)
    print(' Lagerdauer' , dlagerdauer)

#Aufruf  der Funktion
berechneKennzahlen()
    
    

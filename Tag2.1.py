# Datentyp, Operatoren, Literale

def zeigeDatentypen_Operatoren():

    # Ganze Zahl
    einwohner = 430917

    #Gleitkomma-Zahlen ( Rundungsfehler )
    preis = 12.45
    entfernung = 1.38E15
    abstand = 1.5e-6


    print( " Einwohner: " ,einwohner, "\nEntfernung: " , entfernung,"\n",
           " Abstand: " , abstand)

    #nichtnumerische Variable
    paragraph = '§'
    Gruss = "Hallo GFN"

    status = True
    zustand = False

    print("Gruss", Gruss, "Zustand",zustand)

    # arithmetische Operatoren
    x = 9
    y = 4
    erg = x/y
    print( " Gleitkomma-Division: ", erg)

    x = 9
    y = 4
    i_quotient = x //y
    print(" Ganzzahl-Division:", i_quotient)

    # Exponentiation
    x = 2
    y = 4
    ergebnis = x**y
    print ("Exponentiation: ", ergebnis)

    # Vergleichsoperatoren erzeugt als Ergebnis True oder False
    verg1 = 5 > 7
    print( "Verg1:" , verg1)

    verg2 = 5 == 5
    print( "Verg2: " , verg2)


    a1 = 7
    a2 = 9
    if a1==a2:
        print("Gleichheit")
    else:
        print("Ungleichheit")
            




    

    


def showTime():
    sec = int( input( " Anzahl Sekunden:"))

    # Berechnung der Stunden
    hour = sec // 3600
    sec = sec % 3600

    #Minuten
    minute = sec // 60
    sec = sec % 60

    print( "Stunden:" , hour, "\n", "Minuten: " , minute,"\n",
           "Sekunden:" ,sec )
    
    



zeigeDatentypen_Operatoren()
#showTime()












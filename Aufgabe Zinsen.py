# Zinsberechnung mit geschalteter Entscheidung

def berechneZinsen_2():

    #Variable
    anlagebetrag = 0.0
    zinsen = 0.0


    # Eingabe
    anlagebetrag = float( input( "Anlagebetrag:"))


    #Verarbeitungsschritt


    if anlagebetrag <= 5000:
        zinsen = anlagebetrag * 2.0 / 100
    elif anlagebetrag <= 10000:
        zinsen = anlagebetrag * 2.25 / 100
    elif anlagebetrag <= 50000:
        zinsen = anlagebetrag * 2.5 / 100
    else:
        zinsen = anlagebetrag * 2.75 / 100


    # Ausgabe
    print( "Anlagebetrag:" , anlagebetrag,
           "Zinsen: " , zinsen)


berechneZinsen_2()
berechneZinsen_2()

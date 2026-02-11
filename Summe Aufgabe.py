# Schreibtisch-Test S. 12
def test():
    a = 1
    Summe = 0
    while a < 5:
        Summe = Summe +a
        if a > 3:
            Summe = Summe - 1
        else:
            pass
        a = a + 1
    print ( "Summe: " , Summe )


test()

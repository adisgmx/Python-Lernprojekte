# Schleifenarten

# kopfgesteuerte Schleife
def ausgabe_zahlen():
    i = 0

    while i <= 10:
        print (i)
        i = i + 1

# Fussgesteuerte Schleife ( work-around )
def sag_was():

    # unendliche kopfgesteuerte Schleife
    while True:
        text = input(" Eingabe ")

        if len(text) == 0:
            break
        else:
            print( " Eingabe: " , text )

# Zählschleife
def ausgabe_sterne():
    
    for index in  range ( 8,-1,-2 ):
        print("*" , index ,  end =" ")
        

# Aufruf
#ausgabe_zahlen()
#sag_was()
ausgabe_sterne()

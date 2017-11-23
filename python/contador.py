def contador_a():
    palabra=raw_input ("Dime una palabra")
    suma=0
    for cont in range (0,len(palabra),1):
        if palabra[cont]=="a"or palabra[cont]=="e"or palabra[cont]=="o" or palabra[cont]=="i" or palabra[cont]=="u":
             suma=suma+1
    print "En la palabra" ,palabra," hay ",len(palabra)," letras, de las cuales ", suma, " son vocales y  ", len(palabra)-suma, "son consonantes"
contador_a()

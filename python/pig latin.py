def pig_latin():
    texto=raw_input("ecribe un texto to chulo")
    for cont in range(0,len(texto),1):
        if texto[cont]== "A" or texto[cont]=="a" or texto[cont]=="E" or texto[cont]=="e" or texto[cont]=="O" or texto[cont]=="o" or texto[cont]== "I" or texto[cont]== "i":
            print "u",
        else:
            print texto[cont],
pig_latin()

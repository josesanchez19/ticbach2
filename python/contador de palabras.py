def contador_aes():
    palabra=raw_input ("Dime una palabra")
    suma=0
    for cont in range (0,len(palabra),1):
        if palabra[cont]=="o":
             suma=suma+1
    print ("En la palabra"),palabra,("hay"),suma,("letra")
contador_aes()

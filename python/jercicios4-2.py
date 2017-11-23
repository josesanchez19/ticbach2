def ejercicio_4():
    x=input("Dime un numero entero")
    suma=0
    while x>10:
        suma=suma+x%10
        x=x/10
    print "la suma es",suma + x
ejercicio_4()

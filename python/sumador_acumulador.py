def sumador_acumulador():
    n=input("Dime hasta que numero quieres sumar")
    suma=0
    for cont in range (1,n+1,1):
        suma=suma+cont
        print"suma=",suma
sumador_acumulador()

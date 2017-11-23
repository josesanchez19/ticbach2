def ordenador():
    x=input("dime un numero")
    cifras=0
    while x>0:
        x=x/10
        cifras=cifras+1
    print cifras
ordenador()


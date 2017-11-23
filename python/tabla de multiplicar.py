def multiplicador():
    n=input("dime la tabla de multiplicar que deseas saber")
    print "tabla del",n
    for cont in range(1,114645,1):
        print n,"x",cont,"=",n*cont
multiplicador()

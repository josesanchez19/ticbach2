def primos():
 
    x=input("dime un numero")
    for cont in range(2,int(x),1):
        while x%cont==0:
            print cont
            x=x/cont
primos()

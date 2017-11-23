def menu_operacion():
    seguir="SI"
    num1=input("dime un numero")
    num2=input("dime otro numero")
    while (seguir=="SI"):
        print "que deseas hacer con los numeros:"
        print "1 sumarlos"
        print "2 restalos"
        print "3 multiplicar"
        print "4 dividirlos"
        respuesta=input()
        if(respuesta==1):
            suma=num1+num2
            print"la suma es",suma
        if (respuesta==2):
            resta=num1-num2
            print "la resta es ",resta
        if (respuesta==3):
            multiplicacion=num1*num2
            print "la multiplicacion es ", multiplicacion
        if (respuesta==4):
            resto=num1%num2
            division=(num1/num2)
            print("la division es"),division
menu_operacion()



            
        
            
            

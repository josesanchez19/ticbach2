def ejercio_2():
    largest=0
    num1=float(input("entre first number:"))
    num2=float(input("entre secand number:"))
    num3=float(input("entre third number:"))
    if(num1>=num2)and(num1>=num3):
        largest=num1
    else:
        if(num2>=num1) and (num2>=num3):
            largest=num2
        else:
            largest=num3
            print ("largest number between"),num1,num2,("and"),num3,("laetgest")
ejercio_2()

/*Este programa sirve paea leer por teclado 10 mumeros y devolver el mayor*/
#include<iostream>

int main(){
    //Definicion de variable
    int cont;
    int numero;
    int mayor;
    int salir;
    //Bucle de tipo for cont=cont+1 es lo mismo cont++
    // for (cont<=10;cont>=0;cont--)}
    std::cout<<"dime un numero entero:";
    std::cin>>numero;
    mayor=numero;
    for (cont=1;cont<=10;cont++){
        std::cout<<"dime un numero entero:";
        std::cin>>numero;
        if (numero>mayor){
           mayor=numero;
        }
    }
    std::cout<<"El mayor es:"<<mayor;
    std::cout<<"Toca cualquier tecla para salir";
    std::cin>>salir;
    return 0;
    
    
    
    
    
    
    
    
    
    
}

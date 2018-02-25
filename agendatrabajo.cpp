#include<iostream>
using namespace std;

int main(){
   struct contacto{
       string nombre;
       string numero;
       string calle;
       
   };
   int cont;
int borrar;
   contacto amigo[10];
   int salir;
string auxiliar1;


  for(cont=0;cont<10;cont++){
       cout<<"Contacto "<<cont<<endl;
       cout<<"nombre: ";
       cin>>amigo[cont].nombre;
       cout<<"telefono fijo : ";
       cin>>amigo[cont].numero;
       cout<<"calle : ";
       cin>>amigo[cont].calle;
   }
   for(cont=0;cont<10;cont++){
       cout<<"Contacto:"<<cont<<endl;
       cout<<amigo[cont].nombre;
       cout<<amigo[cont].numero;
       cout<<amigo[cont].calle<<endl;
   }
   cin>>salir;
    return 0;  
}



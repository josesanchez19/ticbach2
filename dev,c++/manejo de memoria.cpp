//Programas sobre manejo de memoria
#include<stdio.h>
int main(){
    char palabra1[5];
    char palabra2[5];
    int salir;
    printf("Dime algo: ");
    scanf("%s",palabra1);
    printf("\nDime algo mas: ");
    scanf("%s",palabra2);
    printf("direccion palabra1 = %x",palabra1);
    printf("palabra1 = %c\n",*(palabra1+3));
    printf ("direccion palabra2= %x",palabra2);
    printf("palabra2 = %c  ",*(palabra2+3));
    scanf("%i",&salir);
}

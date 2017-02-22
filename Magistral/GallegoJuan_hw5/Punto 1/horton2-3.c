
#include <stdio.h>
#include <stdlib.h>
#define pr1 3.50f
#define pr2 5.50f

int main(void)
{
  float precio = 0.0;                                       
  int tip = 0;                       
  int cant = 0;                   


   printf("\ningrese el tipo y la cantidad del producto que desea.");
   scanf("%d %d", &tip, &cant);
   if(tip==1)
     { precio = pr1* cant;
       printf("el precio a pagar es %.2f .\n", precio);
     };
   if(tip==2)
     {  precio = pr2* cant;
        printf("el precio a pagar es %.2f .\n", precio);
     }
   else {printf("ese producto no existe lok.\n");};
   
   return 0;
}

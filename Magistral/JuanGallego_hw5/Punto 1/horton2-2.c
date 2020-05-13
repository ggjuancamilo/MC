
#include <stdio.h>
#define ftXyr 3.0f
#define inXyr 36.0f

int main(void)
{
  float m1 = 0.0;                     
  float m2 = 0.0;                      
  float ft = 0.0;                       
  float in = 0.0;                       


   printf("\ningrese el ancho del cuarto, primero los pies seguidos de las pulgadas.");
   scanf("%f %f", &ft, &in);
   m1= ft/ftXyr + in/inXyr;
   printf("\ningrese el largo del cuarto, primero los pies seguidos de las pulgadas.");
   scanf("%f %f", &ft, &in);
   m2= ft/ftXyr + in/inXyr;   


   printf("el area del cuarto es %.2f yardas cuadradas.\n", m1*m2);
   return 0;
}


#include <stdio.h>


int main(void)
{
  int m1 = 0.0;                     
  int m2 = 0.0;                      
  float sa = 0.0;                       
  float ho = 0.0;                       


   printf("\ningrese el salario y las horas trabajadas respectivamente.");
   scanf("%f %f", &sa, &ho);
   m1= (int)(sa/ho);
   m2= (int)((sa/ho-m1) *100);   


   printf("your average hourly pay rate is  %d dollar and %d cents.\n", m1,m2);
   return 0;
}






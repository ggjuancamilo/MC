#include <stdio.h>
#define inXft 12
#define ftXyr 3

int main(void)
{
  int ft = 0;
  int in = 0;
  int yr = 0;
  
  
  printf("ingrese una distancia en pulgadas: ");
  scanf("%d", &in);

  ft = in/inXft;  
  yr = ft/ftXyr; 
  ft %= ftXyr;        
  in %= inXft;     

  printf("\nLa distancia ingresada es equivalente %d yardas %d pies y %d pulgadas.\n",
                                                    yr, ft, in);
  return 0;
}

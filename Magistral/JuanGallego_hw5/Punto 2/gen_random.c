#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{

  int n=atoi(argv[2]);
  int m=atoi(argv[1]);
  int i=0;
  int j=0;
  double r; 
  FILE *fp;
  fp = fopen ( argv[3], "w" );     
  
  for (i;i<(n);i++)
   {
    for (j;j<(m);j++)
     {
      r = drand48();
      fprintf(fp, "%f \t", r);

     }
    fprintf(fp,"\n");
    j=0;
   }
      
  

  return 0;	


}


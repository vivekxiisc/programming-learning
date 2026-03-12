#include<stdio.h>
int main()
{
    int r,c;
    printf("enter no of rows");
    scanf("%d",&r);
     printf("enter no of columns");
    scanf("%d",&c);
    
    
    for(int i=1;i<=r;i++)
    {
      
        for(int j=1;j<=r-i;j++ )
        {
          
          printf(" ");
          
          }
          for(int k=1;k<=c;k++)
          {
            printf("%c",k+64);
        
        
            
          }
        printf("\n");
        c++;
    
    
        }
        return 0;
}


//   A
//  AB
// ABC
//ABCD
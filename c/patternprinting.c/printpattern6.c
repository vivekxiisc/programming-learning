#include<stdio.h>
int main()
{
    int r,c;
    printf("enter no of rows");
    scanf("%d",&r);
    printf("enter the no of things in one row");
    scanf("%d",&c);
    for(int i=1;i<=r;i++)
    {
        int d=65;
        for(int j=1;j<=c;j++ )
        {
          
            printf("%c",d);
            d++;
            
        }
        printf("\n");
        c++;
    }
        return 0;
}
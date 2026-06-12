#include<stdio.h>
int main()
{
int n;
printf("enter the marks");
scanf("%d",&n);
if(n>80)
printf("A grade\n");
else if(n>60)
printf("B grade\n");
else if(n>40)
printf("C grade\n");
else
printf(" FAIL");
    return 0;
}
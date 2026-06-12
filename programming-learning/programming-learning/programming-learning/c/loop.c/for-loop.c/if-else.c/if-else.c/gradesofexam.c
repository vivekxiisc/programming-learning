#include<stdio.h>
int main()
{
int n;
printf("enter the marks");
scanf("%d",&n);
if(n>80)
printf("A grade\n");
if(n>60)
printf("B grade\n");
if(n>40)
printf("C grade\n");
else
printf(" FAIL");
    return 0;
}



//here if marks is greater than last condition output comes to be all grades
//we must use else-if condition here............
#include<stdio.h>
int main()
{
int cp, sp;
printf("enter cost price");
scanf("%d",&cp);
printf("enter selling price");
scanf("%d",&sp);
if(sp>cp)
printf("profit  =  %d",sp-cp);
else
printf("loss  =  %d",cp-sp);

    return 0;
}

//here no profit no loss is not showing for that we must use nested else-if,
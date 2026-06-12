#include<stdio.h>
int main()
{
    for(int i=1;i<=100;i++){
    if(i%2==0)
    printf("%d  ",i);
    if(i%60==0)
    break;
    }
    return 0;
}
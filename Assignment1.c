#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
void prime(int);
void main()
{
    int k,q,i=0;
    char s[50];
    int a[10],*t;
    int A[1000];
    printf("\n Enter the values for K and Q");
    scanf("%d%d",&k,&q);
    printf("\nEnter the queries in the form of \n ! l r x OR ? l r");
    t=prime(k);
    while(i<q)
    {
        printf("Enter the %d query",i);
        i++;
        scanf("%s",s);
        sscanf(s,"%d %d %d %d",&a[0],&a[1],&a[2],&a[3]);
        if(a[0]=='!')
        {
            for(int j=a[1];j<=a[2]+1;j++)
            {
                A[j]=a[3];
                printf("%d",a[j])
            }
        }
        int c=0;
        if(a[0]=='?')
        {
           int s=0;
           for(i=0;i<=a[2];i++)
           {
               if(b[i]==a[1])
               {
                   c++;
               }
           }
           printf("no of common prime factors is %d",c);
        }


    }
}
void prime(int n)
{
    int b[20],i=0;
    for(i=2;n>1;i++)
    {
        while(n%i==0)
        {
            b[i-2]=i;
            n=n/i;
        }
    }
    return b;

}

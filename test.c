#include<stdio.h>
void main()
{
    int n,i,j,a[10][10],a1[10][10];
    double e=0.0; 
    printf("Enter the index : ");
    scanf("%d",&n);
    printf("No. of nodes : %d",n);
    printf("\nEnter the elements :\n");
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        scanf("%d",&a[i][j]);
    }
    printf("\n");
    for(i=0;i<n;i++)
    {
      for(j=0;j<n;j++)
      printf("%d",a[i][j]);
      printf("\n");
    }
    e=(n*(n-1))/2;
    printf("edge = %f",e);
    for(i=0;i<n;i++)
    {
      for(j=0;j<n;j++)
      if(i==j)
      {
        a1[i][j]=0;
      }
      else
      {
        a1[i][j]=a[i][j];
      }
      
    }
}
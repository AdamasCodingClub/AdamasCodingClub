#include<stdio.h>
int main()
{
	int nodes,i,j,f,l,w,edges=0,a[200][200];
	printf("Enter the number of nodes: ");
	scanf("%d",&nodes);
	edges = ((nodes*(nodes -1))/2 )* 0.4;
	printf("\nNumber of edge is: %d\n",edges);
	for(i=0;i<=nodes;i++)
	{
		for(j=0;j<=nodes;j++)
		{
			a[i][j]=9999;
		}
	}
	for(i=1;i<=edges;i++)
	{
		printf("\nEnter the first and last vertices of the edge:\n");
		scanf("%d%d",&f,&l);
		printf("\nEnter the weightage:\n");
		scanf("%d",&w);
		a[f][l]=a[l][f]=w;
	}
	printf("\n\nThe adjacency matrix of the graph is:\n\n\n");
	for(i=0;i<nodes;i++)
	{
		printf("\t%d",i);
	}
	for(i=0;i<nodes;i++)
	{
		printf("\n\n\n%d",i);
		for(j=0;j<nodes;j++)
		{
			if(i==j)
			{
				printf("\t0");
			}
			else
			{
				printf("\t%d",a[i][j]);
			}
		}
	}
}

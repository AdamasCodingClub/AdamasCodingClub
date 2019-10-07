#include<stdio.h>
void display(int** edges,int node,int sv,int* visited)
{
	printf("%d",sv);
	visited[sv]=1;
    for(int i=0;i<node;i++)
    {
    	if(i==sv)
    	continue;
		if(visited[i])
		continue;
		if(edges[sv][i]==1)
    	print(edges,node,i,visited);
	}
}
void main()
{
	printf(" Enter no. of nodes/vertices ");
	scanf("%d",node);
	printf(" \n The no. of edges are %d",node*(node-1)/2);
	
	int **edges=new int*[node];
	for(i=0;i<node;i++)
	
		edges[i]=new int[node];
		
    for(i=0;i<node;i++)
    edge[i][i]=0;
    
for(i=0;i<node;i++)
{
edges[first_v][second_v]=1;
edges[second_v][first_v]=1;

} 

int* visited=new int[node];  
for(i=0;i<node;i++)

	visited[i]=0;
	

display(edges,node,0,visited);

}

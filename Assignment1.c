#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define SIZE 99999
void main(){
    char s[SIZE];
    int a[SIZE],b[SIZE],c[SIZE];
    char* part1,*part2,*part3,*part4;
    int i1,i2,i=2,j,k,c1=0;
    int p=0,n;
    printf("\nEnter any integer value of K:\n");
    scanf("%d",&k);
    for(i=2;k>1;i++){
        while(k%i==0){
            b[i-2]=i;
            k=k/i;
            printf("%d ",b[i-2]);
        }
    }
    printf("\nEnter the queries values like: ' ! l r x ' or  ' ? l r ':\n");
    fflush(stdin); //Buffer clear
    printf("\nEnter the queries:= ");
    gets(s);
    part1=strtok(s," ");
    // IF the input string is ! l r x
    if(*part1=='!'){
        part2=strtok(NULL," ");
        part3=strtok(NULL," ");
        part4=strtok(NULL," ");
        int p1=*part2;
        int p2=*part3;
        int p3=*part4;
        p1=p1-48,p2=p2-48,p3=p3-48;
        printf("\nThe value is assigned to position\n");
        for(p=p1;p<=p2;p++){
            c[p]=p3;
            printf("array[%d]=%d\n",p,c[p]);
        }
        printf("\nThe string look likes=");
        for(n=0;n<=p2;n++){
            printf("%d ",c[n]);
        }
    }
    //IF the input string is ? l r
    if(*part1=='?'){
        part2=strtok(NULL," ");
        part3=strtok(NULL," ");
        int l1=*part2;
        int r=*part3;
        l1=l1-48;r=r-48;
        for(i1=0;i1<=r;i1++){
            for(i2=0;i2<=r;i2++){
                if(b[i2]==l1){
                    c1++;
                }
            }
            l1++;
        }
        printf("\nThe number of common prime factors= %d ",c1);
    }
}

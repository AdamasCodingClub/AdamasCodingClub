import math
Input=input("Enter the values of K And Q = ")
Input=Input.split(" ")
for j in range(len(Input)):
    Input[j]=int(Input[j])
A=[0]*106

pr=[]
def prime(n):
    while n % 2 == 0: 
        if pr==[]:
            pr.append(2)
        else:
            pass
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2): 
            while n % i== 0: 
                if pr==[]:
                    pr.append(i)
                elif pr[-1]== i:
                    pass
                else:
                    pr.append(i)
                n = n / i 
    if n > 2: 
        pr.append(n)
    return pr
pr=prime(Input[0])
op=[]
print("Enter the questions = ")
for i in range(Input[1]):
    q=input()
    q=q.split(" ")
    if(q[0]=='!'):
        for i in range(int(q[1]),int(q[2])+1):
            A[i]=int(q[3])
    elif (q[0]=="?"):
        o=0;
        for i in pr:
            for j in range(int(q[1]), int(q[-1])+1 ):
                if  (A[j]%i==0) :
                    if(A[j] != 0 ):
                        o+=1
                        break
        op.append(o)
print(*op,sep='\n')
            

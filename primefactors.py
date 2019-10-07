import math
def primeFactors(n):
    t=[]
    if n%2==0:
        t.append(2)
    while n % 2 == 0: 
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i==0:
            t.append(i)
        while n % i== 0: 
            n = n / i 
    if n > 2: 
        t.append(int(n))
    return t
k,q=map(int,input().split())
p=primeFactors(k)
x=[0]*100000

while q>0:
    q-=1 
    a=list(input().split())
    l=int(a[1])
    r=int(a[2])
    if a[0]=='!':
        k=int(a[3])
        for i in range (l,r+1):
            if x[i]==0:
                x[i]=k 
    else:
        ans=0
        for i in p:
            for j in range(l,r+1):
                if x[j]==0:
                    continue
                if x[j]%i==0:
                    ans+=1 
                    break
        print(ans)

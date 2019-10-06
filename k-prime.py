def fun3(lis1,a,st):
        for i in lis1:
                if a%i==0:
                        st.add(i)
def fun2(n):
        if n<2:
                return False
        if n==2:
                return True
        i=2
        while i*i<=n:
                if n%i==0:
                        return False
                i+=1
        return True
def fun(k):
        if k==2:
                return [2]
        if k==3:
                return [3]
        i=int(k**.5)
        i=1
        li=[]
        while i*i<=k:
                if k%i==0:
                        if fun2(i):
                                li.append(i)
                        if fun2(k//i):
                                li.append(k//i)
                i+=1
        return list(set(li))
print("Enter the values of K And Q = ")
k,q=map(int,input().split())

lis1=fun(k)
#print(lis1)
lis=[0]*100001
for _ in range(q):
        print("Enter the queries = ")
        s=list(map(str,input().split()))
        if s[0]=='!':
                vv=int(s[3])
                for i in range(int(s[1]),int(s[2])+1):
                               lis[i]=vv
        else:
                st={0}
                for i in range(int(s[1]),int(s[2])+1):
                        if lis[i]!=0:
                                fun3(lis1,lis[i],st)
                print(len(st)-1)
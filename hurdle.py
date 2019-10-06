import math

a=[]
r=int(input("Enter the no of elements for the array:"))

for i in range(r):
	n=int(input("Enter the element:"))
	a.append(n)
print(a)

k=int(input("Enter the positive integer number"))
while k % 2==0:
	print(2)
	k=k/2
for j in range(3,int(math.sqrt(k))+1,2):
	while k % j==0:
		print("Prime Factors:")
		for l in a:
			if j==l:
				print(j)
		k=k/j
if k>2:
	for l in a:
		if k==l:
			print(int(k))








			
		
	

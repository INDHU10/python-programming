p,q=map(int,input().split())
k=list(map(int,input().split()))
c=0
for i in range(0,len(k)):
	if(k[i]==q):
		c=c+1
print(c)		
		

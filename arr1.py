hh=input()
hh=hh.split()
gg=int(hh[0])
dd=int(hh[1])
for i in range(gg,dd+1):
  su=0
  tt=i
  while(tt>0):
    yy=tt%10
    su+=yy**3
    tt=tt//10
  if(i==su):
    print(i,end=' ')
    

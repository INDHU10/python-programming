hh=input()
hh=hh.split()
pp=int(hh[0])
jj=int(hh[1])
for l in range(pp+1,jj+1):
  if l>1:
    for i in range(2,l):
      if(l%i==0):
        break;
    else:
      print(l,end=' ')

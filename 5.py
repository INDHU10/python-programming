xx=input()
xx=xx.split()
yy=xx[0]
zz=xx[1]
ww=xx[2]
if(yy>zz and yy>ww):
  print(yy)
elif(zz>ww):
  print(zz)
else:
  print(ww)

m=input()
q=0
k=0
for i in range(len(m)):
  if(m[i].isalpha()):
    q=q+1
  elif(m[i].isdigit()):
    k=k+1
  else:
    g=0
if q>=0 and k>=0:
  print("yes")
else:
  print("no")

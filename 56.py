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
if q>=1 and k>=1:
  print("Yes")
else:
  print("No")

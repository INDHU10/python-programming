m=input()
count=0
for i in range(len(m)):
  if(m[i].isdigit() or m[i].isalpha() or m[i]==' '):
    continue
  else:
    count=count+1
print(count)    
    

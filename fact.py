b=int(input())
fact=1
if(b==1):
  print(b)
elif(b<0):
  print("can't do factorial for negative")
else:
  for i in range(1,b+1):
    fact=fact*i
  print(fact)  

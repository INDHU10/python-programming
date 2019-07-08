b=int(input())
fact=1
if(num==1):
  print(num)
elif(num<0):
  print("can't do factorial for negative")
else:
  for i in range(1,num+1):
    fact=fact*i
  print(fact)  

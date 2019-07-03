yy=int(input())
if(yy%4==0 or yy%400==0 and yy%100!=0):
  print("yes")
else:
  print("no")

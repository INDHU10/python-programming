ff=int(input())
if ff>1:
  for i in range(2,ff):
    if(ff%i==0):
      print("no")
      break;
  else:
    print("yes")
else:
  print("no")

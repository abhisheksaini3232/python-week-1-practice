x=int(input("Enter the number to find the square root"))
halfX=int(x/2)
for i in range(halfX):
  if(i*i==x):
    print(i)
    break
  elif(i*i>x):
    print(i-1)
    break

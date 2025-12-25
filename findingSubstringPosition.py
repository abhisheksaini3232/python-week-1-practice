full=input("Enter the string: ").lower()
half=input("Enter the substring: ").lower()

lengthFull=len(full)
lengthHalf=len(half)

for i in range(lengthFull):
  
    if (full[i:i+lengthHalf]==half[:]):
      (print("The starting position of the substring is ",i))
      a=1
      break

    else: a=-1   
      
  
i=-1   
if(i==a): print("No match")
  
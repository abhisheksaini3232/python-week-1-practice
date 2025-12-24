stringInput=input("Enter a string to reverse: ")


# reversedString= stringInput[::-1]
# print("Reversed string is:",reversedString)

"""With using for loop"""
len=int(len(stringInput)/2)
length=len(stringInput)
for i in range(len):
  stringInput[i][length-i-1]=stringInput[length-i-1][i]

print("Reversed string is:",stringInput)



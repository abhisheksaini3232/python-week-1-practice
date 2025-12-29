# Project 1 — Student Marks → Grade Calculator
# Concepts Used:
# Variables, conditions, functions
# Features
# Input marks for multiple subjects
# Calculate percentage
# Assign grade
# Handle invalid input

def gradecalculate(marksList):
  total=sum(marksList)
  Percentage=(total*100)/300
  print(f"You have got {Percentage}% in exams")
  if(Percentage>90):
    grade="A"
  elif(Percentage>80 and Percentage<91):
    grade="B"  
  elif(Percentage>70 and Percentage<81):
    grade="C"  
  elif(Percentage>60 and Percentage<71):
    grade="D"
  elif(Percentage>39 and Percentage<61):
    grade="E"
  elif(Percentage<40):
    grade="F"

  print("You have got",grade,"grade in exam")


marksList=[]
while True:
  try:
      marks=int(input("Enter the marks of Mathematics:"))
      marksList.append(marks)  
      marks=int(input("Enter the marks of Science:")) 
      marksList.append(marks)  
      marks=int(input("Enter the marks of English: ")) 
      marksList.append(marks)  
      gradecalculate(marksList)
      break
  except ValueError:print("Enter a valid input")    


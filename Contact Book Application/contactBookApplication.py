# Project 3 — Contact Book Application
# Concepts Used:
#  Dictionaries, lists, functions
# Features
# Add contact
# Search contact
# Delete contact
# Display all contacts

contactDict={}

def addContact():
  name=input("Enter the name: ")
  while True:
    try:
      # number=input("Enter the contact number(separate with ','' if multiple): ").split(",")
      numbers=list(map(int,input("Enter the contact number(separate with ','' if multiple): ").split(",")))
      for i in range (len(numbers)):
        length=len(str(numbers[i]))
        if(length==10):
          continue
        
    except ValueError: print("The contact number length is less than 10")      
      
        
  contactDict["name"]=numbers
  print(f"The contact for {name} added with number {numbers}")
  print(contactDict)

addContact()

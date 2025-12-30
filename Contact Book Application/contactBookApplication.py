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
  name=input("Enter the name: ").capitalize()
  while True:
    try:
      numbers=list(map(int,input("Enter the contact number(separate with ','' if multiple): ").split(",")))
      break
        
    except ValueError: print("Invalid input")      
      
        
  contactDict[name]=numbers
  print(f"The contact for {name} added with number {numbers}")
  print(contactDict)

def searchContact():
  findContact=input("Enter the name of contact you want to find: ").capitalize()
  contact=contactDict.get(findContact)
  print(f"The contact number for {findContact} is {contact}")

def deleteContact():
  contact=input("Enter the name to delete that contact: ").capitalize()
  contactDict.pop(contact, 'Not found')  
  print(f"The contact for {contact} got deleted")

def displayContact():
  print(contactDict)

def deleteAllContact():
  contactDict.clear()
  print("All contacts got deleted")

while True:
 try:
  option=int(input("1. Add contact \n2.Search contact \n3.Delete contact \n4.Display All \n5.Delete All \n6.Exit\n"))
  
  if(option==1):
    addContact()
  elif(option==2):
    searchContact()
  elif(option==3):
    deleteContact()
  elif(option==4):
    displayContact()
  elif(option==5):
    deleteAllContact()
  elif(option==6):
    break
 except:
   print("Enter a valid  input") 
 
  


    

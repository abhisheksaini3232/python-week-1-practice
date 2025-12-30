# Project 3 — Contact Book Application
# Concepts Used:
#  Dictionaries, lists, functions
# Features
# Add contact
# Search contact
# Delete contact
# Display all contacts

class ContactBook:
  

  def __init__(self):
    self.contactDict={}

  def addContact(self):
    
    name=input("Enter the name: ").capitalize()
    while True:
      try:
        numbers=list(map(int,input("Enter the contact number(separate with ','' if multiple): ").split(",")))
        break
          
      except ValueError: print("Invalid input")      
        
          
    self.contactDict[name]=numbers
    print(f"The contact for {name} added with number {numbers}")
    print(self.contactDict)

  def searchContact(self):
    findContact=input("Enter the name of contact you want to find: ").capitalize()
    contact=self.contactDict.get(findContact)
    print(f"The contact number for {findContact} is {contact}")

  def deleteContact(self):
    contact=input("Enter the name to delete that contact: ").capitalize()
    self.contactDict.pop(contact, 'Not found')  
    print(f"The contact for {contact} got deleted")

  def displayContact(self):
    print(self.contactDict)

  def deleteAllContact(self):
    self.contactDict.clear()
    print("All contacts got deleted")



#Main function starts
contact=ContactBook()


while True:
 try:
  option=int(input("1. Add contact \n2.Search contact \n3.Delete contact \n4.Display All \n5.Delete All \n6.Exit\n"))
  
  if(option==1):
    contact.addContact()
  elif(option==2):
    contact.searchContact()
  elif(option==3):
    contact.deleteContact()
  elif(option==4):
    contact.displayContact()
  elif(option==5):
    contact.deleteAllContact()
  elif(option==6):
    break
 except:
   print("Enter a valid  input") 
 
  


    

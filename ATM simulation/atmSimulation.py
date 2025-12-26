# Project 2 — ATM Simulation (Console-Based)
# Concepts Used:
#  Loops, conditions, functions
# Features
# Check balance
# Deposit money
# Withdraw money
# Exit system

balance=0
def depositMoney():
      amount=int(input("Enter the amount you want to add: "))
      balance+=amount
      print("The balance has been updated to ",balance)

def withdrawMoney():
      amount=int(input("Enter the amount you want to add: "))
      if(amount<balance):
        balance=balance-amount
        print("The balance has been updated to ",balance)
      
while True:
 try:
    option=int(input("Enter the option\n1.Check balance 2.Deposit money 3.Withdraw money 4.Exit system"))
    if(option==1):
       print("Your balance is ",balance)
    elif(option==2):
       depositMoney()
    elif(option==3):
       withdrawMoney()
    elif(option=4):
       break       
 except valueError:
   print("Please enter appropriate value")



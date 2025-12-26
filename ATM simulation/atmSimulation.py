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
      global balance
      amount=int(input("Enter the amount you want to add: "))
      balance=amount+balance
      print("The balance has been updated to ",balance)

def withdrawMoney():
      global balance
      amount=int(input("Enter the amount you want to add: "))
      if(amount<balance):
        balance=balance-amount
        print("The balance has been updated to ",balance)
      else:
         print("Low Balance")  
      
while True:
    option=int(input("Enter the option\n1.Check balance 2.Deposit money 3.Withdraw money 4.Exit system\n:"))
    if(option==1):
       print("Your balance is ",balance)
    elif(option==2):
       depositMoney()
    elif(option==3):
       withdrawMoney()
    elif(option==4):
       break       
    else:
     print("Please enter appropriate value")



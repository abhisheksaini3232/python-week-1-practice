# Project 5 — Expense Tracker (File-Based)
# Concepts Used:
#  File handling, loops, functions
# Features
# Add daily expense
# Save to file
# Read expense history
# Show total monthly expense


class DailyExpenseTracker:
  def __init__(self):
    self.Expense={}
    

  def addExpense(self):
    name=input("Enter the name of the expense: ").capitalize()
    amount=int(input("Enter the amount of expense: "))
    self.Expense[name]=amount        
    print(f"The expense of {amount} for {name} has been added")

  def totalExpense(self):
    total=sum(self.Expense.values())
    print(f"The total expense is {total}")  
  
  def saveToFile(self):
    f=open("expenseTrackerFile.txt", "a")
    f.write(str(self.Expense))
    print("The data has been saved to the file")

  def readFile(self):
    f=open("expenseTrackerFile.txt", "r")
    fileText=f.read()
    print("printing the file text now")
    print(fileText)


monday=DailyExpenseTracker()

Options=input("1.Add Expense\n 2.Save in File\n 3. Read Expense\n 4. Show total Exense\n 5.Exit")



#  Do we need to setup another function to calculate the total if we have multiple dictionaries in the file. And Do we need the save the Expense Dictionary before to calculate the total

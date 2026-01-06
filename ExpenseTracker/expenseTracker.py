# Project 5 — Expense Tracker (File-Based)
# Concepts Used:
#  File handling, loops, functions
# Features
# Add daily expense
# Save to file
# Read expense history
# Show total monthly expense

import ast


class DailyExpenseTracker:
    def __init__(self):
        self.Expense = {}
        self.file_name = "expenseTrackerFile.txt"
        self._load_from_file()  

    def addExpense(self):
        name = input("Enter the expense: ").capitalize()
        amount = int(input("Enter the amount of expense: "))
        if name in self.Expense:
            self.Expense[name] += amount
        else:
            self.Expense[name] = amount
        print(f"The expense of {amount} for {name} added")

    def totalExpense(self):
        total = sum(self.Expense.values())
        print(f"The total expense is {total}")

    def saveToFile(self):
        with open(self.file_name, "w") as f:
            f.write(str(self.Expense))
        print("The data has been saved to the file")

    def readFile(self):
        try:
            with open(self.file_name, "r") as f:
                fileText = f.read()
            if fileText: print(fileText)
            else: print("Empty File")
        except FileNotFoundError:
            print("No file found or No expense")

    def _load_from_file(self):
        try:
            with open(self.file_name, "r") as f:
                content = f.read().strip()
                if content:
                    self.Expense = ast.literal_eval(content)
        except FileNotFoundError:
            self.Expense = {}


def main():
    monday = DailyExpenseTracker()

    while True:
        print("\n1. Add Expense")
        print("2. Save in File")
        print("3. Read Expense")
        print("4. Show Total Expense")
        print("5. Exit")

        option = input("Enter your option (1-5): ")

        if option == "1":
            monday.addExpense()
        elif option == "2":
            monday.saveToFile()
        elif option == "3":
            monday.readFile()
        elif option == "4":
            monday.totalExpense()
        elif option == "5":
            print("Exiting")
            break
        else:
            print("Please choose between 1 to 5.")


if __name__ == "__main__":
    main()



#  Do we need to setup another function to calculate the total if we have multiple dictionaries in the file. And Do we need the save the Expense Dictionary before to calculate the total

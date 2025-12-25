userInput=input("Enter a string to count vowels : ")

if(userInput=="" ):
    print("Please enter a valid string")

else:
    vowels='AEIOUaeiou'
    count=0
    for i in userInput:
        if i in vowels:
            count+=1
    print(f"Total Vowels in the string is : {count}")
def get_number(prompt, min_val=0, max_val=100):
    while True:
        try:
            num = int(input(prompt))
            if min_val <= num <= max_val:
                return num
            print(f"Enter number between {min_val} and {max_val}!")
        except ValueError:
            print("Enter valid number!")


x = get_number("Enter number (0-100): ")
count = 1
while True:
    guess = get_number("Guess the number: ")

    if guess == x:
        print(f"Congratulations! You guessed in {count} tries!")
        break
    elif guess > x:
        print("Too high!")
    else:
        print("Too low!")

    count += 1
    if count==7:
        print('Your chances are exhausted')
        break

print("Thanks for playing!")

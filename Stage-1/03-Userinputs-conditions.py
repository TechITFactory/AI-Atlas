#03 : number guessing game
# input() int() if/elif/else, compare operators, logical operator, nested conditions

#python3 03-Userinputs-conditions.py

import random # extra py tools by default, random lets us pick random numbers

print("+" * 40)
print("     NUMBER GUESSING GAME")
print("=" * 40)
print()

#input() always returs string
#int() converts string to integer
#float() converts string to float
#str() converts integer to string
#bool() converts string to boolean

name = input("Enter your Name:")
print(f"Hey {name}, Lets Play! \n")

# if /elif /else

print("choose difficulty")
print(" 1 - Easy (1 to 10, 7 guesses)")
print(" 2 - Medium (1 to 50, 5 guesses)")
print(" 3 - Hard (1 to 100, 3 guesses)")
print()

choice = input("ENter Your Choice (1/2/3): ")

if choice == "1":
    high = 10
    max_guesses = 7
    label = "Easy"
elif choice == "2":
    high = 50
    max_guesses = 5
    label = "Medium"    
elif choice == "3":
    high = 100
    max_guesses = 3
    label = "Hard"
else:
    print("Invalid Choice. Defaulting to Medium")    
    high = 50
    max_guesses = 5
    label = "Medium"

print(f"\n[{label}] Guess a number between 1 and {high}. You have {max_guesses} Guesses")

# random.randint(a, b)
secret = random.randint(1, high)
guesses_left = max_guesses
last_guess = None

#Comparision Operator
# ==, >, <, >=, =<, !=

#guess 1

guess = int(input(f"Guess {max_guesses - guesses_left + 1 }/{max_guesses}:"))
guesses_left = guesses_left - 1

if guess == secret:
    print(f"Correct! You got it in 1 guess, Impressive, {name}!")
elif guess < secret:
    print(f"Too Low! {guesses_left}")
else:
    print(f"Too High! {guesses_left}")
    
#guess 2

guess = int(input(f"Guess {max_guesses - guesses_left + 1 }/{max_guesses}:"))
guesses_left = guesses_left - 1

if guess == secret:
    print(f"Correct! You got it in 2 guess, Impressive, {name}!")
elif guess < secret:
    print(f"Too Low! {guesses_left} guesses left")
    if secret - guess <=3:
        print("Hint: You are close")
else:
    print(f"Too High! {guesses_left} guesses left")
    if guess - secret <=3:
        print("Hint: You are close")
    
#guess 3 

if guess != secret and guesses_left > 0:
    guess = int(input(f"Guess {max_guesses - guesses_left + 1 }/{max_guesses}:"))
    guesses_left -= 1
    if guess == secret:
        print(f"Correct! You got it in 3 guess, Impressive, {name}!")
    elif guess < secret:
        print(f"Too Low! {guesses_left} guesses left")
        if secret - guess <=2:
            print("Hint: You are close")
    else:
        print(f"Too High! {guesses_left} guesses left")
        if guess - secret <=2:
            print("Hint: You are close")

# guess 4

if guess != secret and guesses_left > 0:
    guess = int(input(f"Guess {max_guesses - guesses_left + 1 }/{max_guesses}:"))
    guesses_left -= 1
    if guess == secret:
        print(f"Correct! You got it in 4 guess, Impressive, {name}!")
    elif guess < secret:
        print(f"Too Low! {guesses_left} guesses left")
        if secret - guess <=2:
            print("Hint: You are close")
    else:
        print(f"Too High! {guesses_left} guesses left")
        if guess - secret <=2:
            print("Hint: You are close")


# guess 5

if guess != secret and guesses_left > 0:
    guess = int(input(f"Guess {max_guesses - guesses_left + 1 }/{max_guesses}:"))
    guesses_left -= 1
    if guess == secret:
        print(f"Correct! You got it in 5 guess, Impressive, {name}!")
    elif guess < secret:
        print(f"Too Low! {guesses_left} guesses left")
        if secret - guess <=2:
            print("Hint: You are close")
    else:
        print(f"Too High! {guesses_left} guesses left")
        if guess - secret <=2:
            print("Hint: You are close")

# guess 6

if guess != secret and guesses_left > 0:
    guess = int(input(f"Guess {max_guesses - guesses_left + 1 }/{max_guesses}:"))
    guesses_left -= 1
    if guess == secret:
        print(f"Correct! You got it in 6 guess, Impressive, {name}!")
    elif guess < secret:
        print(f"Too Low! {guesses_left} guesses left")
        if secret - guess <=2:
            print("Hint: You are close")
    else:
        print(f"Too High! {guesses_left} guesses left")
        if guess - secret <=2:
            print("Hint: You are close")

#guess 7 FInal Guess

if guess != secret and guesses_left > 0:
    guess = int(input(f"Guess {max_guesses - guesses_left + 1 }/{max_guesses}:"))
    guesses_left -= 1

    if  guess == secret:
        print(f"Correct! You got it in 7 guess, Impressive, {name}!")
    else:
        diff = abs(secret - guess)
        print(f"GAME OVER! The secret number was {secret}")
        if diff <= 2:
            print("Hint: You are close")
        elif diff <= 5:
            print("Hint: You are getting warmer")
        else:
            print("Hint: You are getting colder")

print()
if guess == secret:
    remaining_pct = (guesses_left / max_guesses) * 100
    print(f"You guessed the number in {max_guesses - guesses_left} guesses!")
    print(f"You guessed the number in {remaining_pct:.2f}% of your allowed guesses!")
else:
    print(f"GAME OVER! The secret number was {secret}")
    remaining_pct = (guesses_left / max_guesses) * 100
    print(f"You guessed the number in {max_guesses - guesses_left} guesses!")
    print(f"You guessed the number in {remaining_pct:.2f}% of your allowed guesses!")

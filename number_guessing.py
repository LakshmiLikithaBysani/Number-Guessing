import random

number = random.randint(1, 10)

print("🎯 Number Guessing Game")
print("I have selected a number between 1 and 10.")

guess = int(input("Enter your guess: "))

if guess == number:
    print("🎉 Congratulations! You guessed it correctly.")
else:
    print("❌ Wrong guess!")
    print("The correct number was:", number)
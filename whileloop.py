import random
"""Separate each digit of a number and print it on the new line"""
num = int(input("Enter a number: "))
while num > 0:
    digit = num % 10
    print(digit)
    num //= 10

""" Accept a number and print its reverse"""
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print(f"Reverse is: {reverse}")
"""Accept a number and check if it is a pallindromic number (If
number and its reverse are equal?"""
if reverse == num:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")


"""Create a random number guessing game with python."""

number_to_guess = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")

guess = None
while guess != number_to_guess:
    guess = int(input("Enter your guess (between 1 and 100): "))
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
print(f"Congratulations! You've guessed the number {number_to_guess}.")


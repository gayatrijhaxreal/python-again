"""- Accept an integer and Print hello world n times """
n = int(input("Enter a number: "))
for i in range(n):
    print("Hello World")

"""Print natural number up to n"""
for i in range(1, n + 1):
    print(i)
"""- Reverse for loop. Print n to 1 """
for i in range(n, 0, -1):
    print(i)
"""Take a number as input and print its table"""
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

    """ Sum up to n terms """
sum = 0
for i in range(1, n + 1):
    sum += i
print(f"Sum of first {n} natural numbers is: {sum}")

"""- Factorial of a number"""
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Factorial of {n} is: {factorial}")

"""- Print the sum of all even & odd numbers in a range separately"""
even_sum = 0
odd_sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(f"Sum of even numbers up to {n} is: {even_sum}")
print(f"Sum of odd numbers up to {n} is: {odd_sum}")

"""Print all the factors of a number"""
print(f"Factors of {n} are: ", end="")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")

"""Accept a number and check if it a perfect number or not.

 A number whose sum of factors is equal to the number itself


 Ex - 6 = 1, 2, 3 = 6"""

factor_sum = 0
for i in range(1, n):
    if n % i == 0:
        factor_sum += i
if factor_sum == n:
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")  

"""Check wether the number is prime or not """
is_prime = True
if n < 2:
    is_prime = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")

"""- Reverse a string without using in build functions."""


string = input("Enter a string: ")
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
print(f"Reversed string is: {reversed_string}")

"""Check string is Pallindrome or not """

if string == reversed_string:
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")

""" Count all letters, digits, and special symbols from a given
string

 Given: str1 = "P@#yn26at^&i5ve"

 Expected Outcome:

 Total counts of chars, digits, and symbols

 Chars = 8

 Digits = 3

 Symbol = 4"""

str1 = "P@#yn26at^&i5ve"
chars = 0
digits = 0
symbols = 0
for char in str1:
    if char.isalpha():
        chars += 1
    elif char.isdigit():
        digits += 1
    else:
        symbols += 1
print(f"Chars = {chars}")
print(f"Digits = {digits}")
print(f"Symbols = {symbols}")

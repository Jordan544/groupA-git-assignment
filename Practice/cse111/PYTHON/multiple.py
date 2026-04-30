# #addition
# def addition_function():
#     num1 = float(input('Enter first number: '))
#     num2 = float(input('Enter second number: '))
#     result = num1 + num2
#     print(f'Addition of {num1} and {num2} is {result:.2f}')

# #Division
# def division_function():
#     num1 = float(input('Enter first number: '))
#     num2 = float(input('Enter second number: '))
#     result = num1 / num2
#     print(f'Division of {num1} and {num2} is {result:.2f}')

# #Subtraction
# def subtraction_function():
#     num1 = float(input('Enter first number: '))
#     num2 = float(input('Enter second number: '))
#     result = num1 - num2
#     print(f'Subtraction of {num1} and {num2} is {result:.2f}')

# #Multiplication
# def multiplication_function():
#     num1 = float(input('Enter first number: '))
#     num2 = float(input('Enter second number: '))
#     result = num1 * num2
#     print(f'Multiplication of {num1} and {num2} is {result:.2f}')

# #Modulo
# def modulo_function():
#     num1 = float(input('Enter first number: '))
#     num2 = float(input('Enter second number: '))
#     result = num1 % num2
#     print(f'Modulus of {num1} and {num2} is {result:.2f}')


# user_entry = str(input('Enter mathematical operation (+ * - / %): '))

# if user_entry == '+':
#     addition_function()
# elif user_entry == '/':
#     division_function()
# elif user_entry == '*':
#     multiplication_function()
# elif user_entry == '-':
#     subtraction_function()
# elif user_entry == '%':
#     modulo_function()
# else:
#     print('Invalid Syntax')

import random
from time import sleep
while True:
    math = random.randint(1, 5)
    print(math)
    print()

    user_guess = int(input("Guess a Number between 1 and 5: "))
    if user_guess == math:
        for i in range(3, 0, -1):
            print(i, flush=True)
            sleep(0.5)

        print(f"Correct!! You have guessed the number: {math}")
        print()
        play_again = str(input("Play Again?: ")).lower
        print()
        if play_again == "no":
            print("Thanks for playing")
            break

    else:
        for i in range(3, 0, -1):
            print(i, flush=True)
            sleep(0.5)

        print("Wrong Guess!! Please try again")




import os
# Imports the os module used to clear the CMD screen


def addition (number1, number2):
    answer_addition = (number1 + number2)
    return answer_addition
# This is the function that performs the Addition


def subtraction (number1, number2):
    answer_subtraction = (number1 - number2)
    return answer_subtraction
# This is the function that performs the Subtractions


def multiplication (number1, number2):
    answer_multiplication = (number1 * number2)
    return answer_multiplication
# This is the function that performs the Multiplications


def division (number1, number2):
    if number2 == 0: # Lines 24-26 prevents the calculator from crashing when deviding by 0
        print('\nCannot Divide By Zero.')
        return None
    else:
        answer_division = (number1 / number2)
        return answer_division
# This is the function that performs the Divisions


running = True
while running:
# Keeps the calculator running as long as the sentinel variable remains True
    

    print('=====================\n  PYTHON CALCULATOR\n=====================\n\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Clear\n6. Exit\n\n')
    # This displays the Menu for the Calculator


    menu_option = int(input('Choose An Option:'))

    if menu_option == 1: # Performs the addition calculation and displays the result
        number1 = float(input('Enter first number: '))
        number2 = float(input('Enter second number: '))
        answer_addition = addition(number1, number2)
        print(f'\nThe Answer Is: {answer_addition}\n')

    elif menu_option == 2: # Performs the subtraction calculation and displays the result
        number1 = float(input('Enter first number: '))
        number2 = float(input('Enter second number: '))
        answer_subtraction = subtraction(number1, number2)
        print(f'\nThe Answer Is: {answer_subtraction}\n')

    elif menu_option == 3: # Performs the multiplication calculation and displays the result
        number1 = float(input('Enter first number: '))
        number2 = float(input('Enter second number: '))
        answer_multiplication = multiplication(number1, number2)
        print(f'\nThe Answer Is: {answer_multiplication}\n')

    elif menu_option == 4: # Performs the division calculation and displays the result
        number1 = float(input('Enter first number: '))
        number2 = float(input('Enter second number: '))
        answer_division = division(number1, number2)
        if answer_division != None: # Checks if it is deviding by 0
            print(f'\nThe Answer Is: {answer_division}\n')

    elif menu_option == 5:
        os.system('cls')
    # Clears the CMD screen

    elif menu_option == 6:
        running = False
    # Exits the calculator by changing the sentinel variable to False
    
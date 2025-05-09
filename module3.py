import os
import random

tasks = []
scores = []

def pause():
    input("\nPress any key to continue...")

def title1():
    print("======================================== ")
    print("            Simple Calculator            ")
    print("======================================== ")
   
def title2():
    print("======================================== ")
    print("          Temperature Converter          ")
    print("======================================== ")

def title3():
    print("======================================== ")
    print("               To-Do List                ")
    print("======================================== ")

def title4():
    print("======================================== ")
    print("          Number Guessing Game           ")
    print("======================================== ")
    
def title5():
    print("======================================== ")
    print("       Student Grade Calculator          ")
    print("======================================== ")
    
def add():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        title1()
        print("                   ADD                   ")
        firstNumber = input("\nEnter first number: ")
        if firstNumber.isdigit():
            break
        else:
            print ("\nInvalid input. Please try again.")
            pause()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        title()
        print("                   ADD                   ")
        print("\nEnter first number:", firstNumber)
        secondNumber = input("\nEnter second number: ")
        if secondNumber.isdigit():
            break
        else:
            print ("\nInvalid input. Please try again.")
            pause()
    sum = int(firstNumber) + int(secondNumber)
    print ("\nResult:", sum)
    pause()
           
def subtract():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        title1()
        print("                 SUBTRACT                ")
        firstNumber = input("\nEnter first number: ")
        if firstNumber.isdigit():
            break
        else:
            print ("\nInvalid input. Please try again.")
            pause()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        title1()
        print("                 SUBTRACT                ")
        print("\nEnter first number:", firstNumber)
        secondNumber = input("\nEnter second number: ")
        if secondNumber.isdigit():
            break
        else:
            print ("\nInvalid input. Please try again.")
            pause()
    difference = int(firstNumber) - int(secondNumber)
    print ("\nResult:", difference)
    pause()
   
def multiply():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        title1()
        print("                 MULTIPLY                ")
        firstNumber = input("\nEnter first number: ")
        if firstNumber.isdigit():
            break
        else:
            print ("\nInvalid input. Please try again.")
            pause()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        title1()
        print("                 MULTIPLY                ")
        print("\nEnter first number:", firstNumber)
        secondNumber = input("\nEnter second number: ")
        if secondNumber.isdigit():
            break
        else:
            print ("\nInvalid input. Please try again.")
            pause()
    product = int(firstNumber) * int(secondNumber)
    print ("\nResult:", product)
    pause()
   
def divide():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        title1()
        print("                  DIVIDE                 ")
        firstNumber = input("\nEnter first number: ")
        if firstNumber.isdigit():
            break
        else:
            print ("\nInvalid input. Please try again.")
            pause()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        title1()
        print("                  DIVIDE                 ")
        print("\nEnter first number:", firstNumber)
        secondNumber = input("\nEnter second number: ")
        if secondNumber.isdigit():
            break
        else:
            print ("\nInvalid input. Please try again.")
            pause()
    quotient = int(firstNumber) / int(secondNumber)
    print ("\nResult:", quotient)
    pause()
   
def part1():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        title1()
        print("                  Menu                   ")
        print("[1] Add")
        print("[2] Subtract")
        print("[3] Multiply")
        print("[4] Divide")
        print("[5] Exit")
       
        choice = input("\nEnter your choice (1-5): ")
        if choice == "1":
            add()
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                title1()
                print("                   ADD                   ")
                choice = input("\nWould you like to add again (Y/N)? ")
                if choice == "Y":
                    add()
                elif choice == "N":
                    part1()
                else:  
                    print ("Invalid input. Please try again.")
                    pause()
        if choice == "2":      
            subtract()
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                title1()
                print("                 SUBTRACT                ")
                choice = input("\nWould you like to subtract again (Y/N)? ")
                if choice == "Y":
                    subtract()
                elif choice == "N":
                    part1()
                else:  
                    print ("Invalid input. Please try again.")
                    pause()
        if choice == "3":      
            multiply()
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                title1()
                print("                 MULTIPLY                ")
                choice = input("\nWould you like to multiply again (Y/N)? ")
                if choice == "Y":
                    subtract()
                elif choice == "N":
                    part1()
                else:  
                    print ("Invalid input. Please try again.")
                    pause()            
        if choice == "4":      
            divide()
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                title1()
                print("                  DIVIDE                 ")
                choice = input("\nWould you like to divide again (Y/N)? ")
                if choice == "Y":
                    subtract()
                elif choice == "N":
                    part1()
                else:  
                    print ("Invalid input. Please try again.")
                    pause()            
        elif choice == "5":
            print ("\nThank you for using this program!")
            pause()
            break
        else:
            print ("\nInvalid input. Please try again.")
            pause()


def celciusToFahrenheit():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        title2()
        print("      CONVERT CELSIUS TO FAHRENHEIT      ")
        temperature = input("\nEnter temperature in celsius: ")
        if temperature.isdigit():
            intTemperature = int(temperature)
            f1_float = intTemperature * 9
            f2_float = f1_float / 5
            fahrenheit_float = f2_float + 32
            print ("\nConverted:",fahrenheit_float,"°C")
            pause()
            break
        else:
            print ("\nInvalid input. Please try again.")
            pause()


def fahrenheitToCelcius():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        title2()
        print("      CONVERT FAHRENHEIT TO CELCIUS      ")
        temperature = input("\nEnter temperature in fahrenheit: ")
        if temperature.isdigit():
            intTemperature = int(temperature)
            c1_float = intTemperature - 32
            c2_float = c1_float * 5
            celcius_float = c2_float / 9
            print ("\nConverted:",celcius_float,"°F")
            pause()
            break
        else:
            print ("\nInvalid input. Please try again.")
            pause()
   
def part2():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        title2()
        print("                  Menu                   ")
        print("[1] Convert Celsius to Fahrenheit")
        print("[2] Convert Fahrenheit to Celsius")
        print("[3] Exit")
       
        choice = input("\nEnter your choice (1-3): ")
        if choice == "1":
            celciusToFahrenheit()
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                title2()
                print("      CONVERT CELSIUS TO FAHRENHEIT      ")
                choice = input("\nWould you like to convert again (Y/N)? ")
                if choice == "Y":
                    celciusToFahrenheit()
                elif choice == "N":
                    part2()
                else:  
                    print ("Invalid input. Please try again.")
                    pause()
        elif choice == "2":
            fahrenheitToCelcius()
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                title2()
                print("      CONVERT FAHRENHEIT TO CELSIUS      ")
                choice = input("\nWould you like to convert again (Y/N)? ")
                if choice == "Y":
                    fahrenheitToCelcius()
                elif choice == "N":
                    part2()
                else:  
                    print ("Invalid input. Please try again.")
                    pause()
        elif choice == "3":
                    print ("\nThank you for using this program!")
                    pause()
                    break
        else:
            print ("\nInvalid input. Please try again.")
            pause()

def add_task(tasks):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        title3()
        view_tasks(tasks)
        print("\n               ADD TASK                  ")
        task = input("\nEnter the task to add: ")
        if task:
            if task in tasks:
                print("\nTask already exists.")
                pause()
            else:
                tasks.append(task)
                print("\nTask added.")
                pause()
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    title3()
                    print("\n               ADD TASK                  ")
                    choice = input("\nWould you like to add another task (Y/N)? ")
                    if choice == "Y":
                        break
                    elif choice == "N":
                        part3()
                    else:  
                        print ("\nInvalid input. Please try again.")
                        pause()
                        continue
        else:
            print("\nInvalid input. Please try again.")
            pause()
            
def remove_task(tasks):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        title3()
        view_tasks(tasks)
        print("\n             REMOVE TASK                 ")
        choice = input("\nEnter the task to remove: ")
        if 1 <= int(choice) <= len(tasks):
                removedTask = tasks.pop(int(choice) - 1)
                print(f"\nTask '{removedTask}' removed.")
                pause()
        else:
            print("\nInvalid input. Please try again.")
            pause()
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            title3()
            print("\n             REMOVE TASK                 ")
            choice = input("\nWould you like to remove another task (Y/N)? ")
            if choice == "Y":
                break
            elif choice == "N":
                return
            else:  
                print ("\nInvalid input. Please try again.")
                pause()
            
def view_tasks(tasks):
    os.system('cls' if os.name == 'nt' else 'clear')
    title3()
    print("\n              VIEW TASKS                  ")
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        pause()
    else:
        print("\nNo tasks available.")
        pause()
    
def part3():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        title3()
        print("                  Menu                   ")
        print("[1] Add Task")
        print("[2] Remove Task")
        print("[3] View Tasks")
        print("[4] Exit")
       
        choice = input("\nEnter your choice (1-4): ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            title3()
            view_tasks(tasks)
        elif choice == "4":
            print("\nThank you for using this program!")
            pause()
            mainMenu()
        else:
            print("\nInvalid input. Please try again.")
            pause()
            
def playNumberGuessingGame():
    number = random.randint(1, 100)
    attempts = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        title4()
        print("\n       PLAY NUMBER GUESSING GAME            ")
        guessInput = input("\nGuess the number (1-100): ")
        if not guessInput.isdigit():
            print("\nInvalid input. Please try again.")
            pause()
            continue
        guessInt = int(guessInput)
        attempts += 1
        if guessInt < 1 or guessInt > 100:
            print("\nInvalid input. Please try again.")
            pause()
            continue
        if guessInt < number:
            print("\nToo low!")
            pause()
            continue
        elif guessInt > number:
            print("\nToo high!")
            pause()
            continue
        else:
            print(f"\nCongratulations! You guessed the number {number} in {attempts} attempts.")
            pause()
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            title4()
            print("\n       PLAY NUMBER GUESSING GAME            ")
            choice = input("\nWould you like to play again (Y/N)? ")
            if choice == "Y":
                break
            elif choice == "N":
                return
            else:  
                print ("\nInvalid input. Please try again.")
                pause()
            
def part4():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        title4()
        print("                  Menu                   ")
        print("[1] Play Number Guessing Game")
        print("[2] Exit")
        
        choice = input("\nEnter your choice (1-2): ")
        if choice == "1":
            playNumberGuessingGame()
        elif choice == "2":
            print("\nThank you for using this program!")
            pause()
            mainMenu()
        else:
            print ("\nInvalid input. Please try again.")
            pause()
    
def addScore(scores):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        title5()
        print("                  ADD SCORE              ")
        subject = input("\nEnter the subject: ")
        if subject:
            break
        else:
            print("\nInvalid input. Please try again.")
            pause()
            continue
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        title5()
        print("                  ADD SCORE              ")
        print("\nEnter the subject:",subject)
        scoreInput = input("\nEnter the score (0-100): ")
        if scoreInput.replace('.', '', 1).isdigit():
            score = float(scoreInput)
            if 0 <= score <= 100:
                scores.append(score)
                print("\nScore added.")
                pause()
                break
            else:
                print("\nInvalid input. Please try again.")
                pause()
        else:
            print("\nInvalid input. Please try again.")
            pause()
            continue
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        title5()
        print("\n                ADD SCORE                   ")          
        choice = input("\nWould you like to add a score again (Y/N)? ")
        if choice == "Y":
            addScore(scores)
        elif choice == "N":
            part5()
        else:  
            print ("\nInvalid input. Please try again.")
            pause()
        
def calculateAverage(scores):
    os.system('cls' if os.name == 'nt' else 'clear')
    title5()
    print("           CALCULATE AVERAGE             ")
    if scores:
        average = sum(scores) / len(scores)
        print(f"\nAverage Grade: {average:.2f}")
        pause()
    else:
        print("\nNo scores available to calculate average.")
        pause()
    
def part5():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        title5()
        print("                  Menu                   ")
        print("[1] Add Score")
        print("[2] Calculate Average")
        print("[3] Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        if choice == "1":
            addScore(scores)
        elif choice == "2":
            calculateAverage(scores)
        elif choice == "3":
            print("\nThank you for using this program!")
            pause()
            break
        else:
            print ("\nInvalid input. Please try again.")
            pause()
    
def mainMenu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("======================================== ")
        print("                MAIN MENU                ")
        print("======================================== ")
        print("[1] Simple Calculator")
        print("[2] Temperature Converter")
        print("[3] To-do List")
        print("[4] Number Guessing Game")
        print("[5] Student Grade Calculator")
        print("[6] Exit")

        choice = input("\nEnter your choice (1-6): ")
        if choice == "1":
            part1()
        elif choice == "2":
            part2()
        elif choice == "3":
            part3()
        elif choice == "4":
            part4()
        elif choice == "5":
            part5()
        elif choice == "6":
            break
        else:
            print ("Invalid input. Please try again.")
            pause()

mainMenu()

import os 

def checkAgain():
    while True:
        choice = input("Do you want to check another year? (y/n) ").upper()
        if choice == "Y":
            os.system('cls')
            userInput()
            break
        elif choice == "N": 
            os.system('cls')
            exit()
            break
        else: 
            os.system('cls')
            print("Wrong input, try again.")
            continue

def checkYear(x):
    if (x % 4 == 0):
        if (x % 100 == 0):
            if (x % 400 == 0):
                os.system('cls')
                print("The year " + str(x) + " is a leap year.")
                checkAgain()
            else:
                os.system('cls')
                print("The year " + str(x) + " is not a leap year.")
                checkAgain()
        else:
            os.system('cls')
            print("The year " + str(x) + " is a leap year.")
            checkAgain()
    else:
        os.system('cls')
        print("The year " + str(x) + " is not a leap year.")
        checkAgain()

def userInput():
    while True:
        year = input("What year do you want to check if leap? ")
        result = year.isdigit()
        if result:
            checkYear(int(year))
            break
        else:
            print("Wrong input, try again.")
            continue

os.system('cls')
userInput()
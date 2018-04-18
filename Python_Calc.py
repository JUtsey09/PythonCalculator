import pyperclip
import math
def calc():
    print("Welcome to the Utsey Python Calculator v1.0!\n")
    print("Please select an operation:\n")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root\n")
    def numbers():
        global num1 
        num1 = int(input("\nEnter first number: "))
        global num2
        num2 = int(input("Enter second number: "))
    def calc2():
        user_input = input("\nPress Enter to perform another calculation or type 'q' and press Enter to quit.\n\n\n")
        if user_input == 'q':
            print('Goodbye!')
        else:
            calc()
    selection = input("Select an option: (1,2,3,4,5): ")
    if selection == '1':
        print("\nYou chose Addition!")
        numbers()
        total = num1 + num2
        pyperclip.copy(str(total))
        print("\nSolution:",num1,"+",num2,"=",total)
        calc2()
    elif selection == '2':
        print("\nYou chose Subtraction!")
        numbers()
        total = num1 - num2
        pyperclip.copy(str(total))
        print("\nSolution:",num1,"-",num2,"=",total)
        calc2()
    elif selection == '3':
        print("\nYou chose Multiplication!")
        numbers()
        total = num1 * num2
        pyperclip.copy(str(total))
        print("\nSolution:",num1,"*",num2,"=",total)
        calc2()
    elif selection == '4':
        print("\nYou chose Division!")
        numbers()
        total = num1 / num2
        pyperclip.copy(str(total))
        print("\nSolution:",num1,"/",num2,"=",total)
        calc2()
    elif selection == '5':
        print("\nYou chose Square Root!")
        num3 = int(input("\nEnter number: "))
        total = math.sqrt(num3)
        pyperclip.copy(str(total))
        print("\nSolution: The square root of", num3, "is:",total)
        calc2()
    else:
        print("\nInvalid selection! Please enter a valid operation.\n")
        input("Press any key to continue...\n\n\n")
        calc()
calc()

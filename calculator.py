# Creating a simple calculator application.
# User is asked to enter two numbers and the operation (e.g. +, -, x, etc.) that they’d like to perform on the numbers. 
# Display the answer to the equation. Every equation entered by the user should be written to a text file. 
# Using defensive programming to write this program in a manner that is robust and handles unexpected events and user inpnumber.

print("Welcome to first simple calculator application")
# While loops function to give the user a choice and repeat if answer is invalid.
while True: 
    # Asking the user to choose.
    user_choice = (input("Enter 1 to calculate a new equation, 2 to read all equations from a text file: "))
    if user_choice == "1":
        while True:
            # Create try function to test for errors.
            try:
                # Asking the user for two number and an operator.
                number_one = float(input("Please enter your first number: "))  
                number_two = float(input("Please enter your second number: "))             
                equation_sign = input("Choose the operator you want to use (+ , -, *, /): ")
            # Create except to handle the errors.
            except ValueError:
                print("Error, enter a valid number: ")
                # Continue statement to repeat the inputs if user answer is invalid.
                continue
            # Calculations based on the operator chosen by the user.
            try:   
                if equation_sign == "+":
                    answer = number_one + number_two
                elif equation_sign == "-":
                    answer = number_one - number_two
                elif equation_sign == "*":
                    answer = number_one * number_two
                elif equation_sign == "/":
                    answer = number_one / number_two
                else:
                    print("Error, enter corect operator (+ , -, *, /): ")
                    continue
            # Handle errors for any number divedid be 0.   
            except ZeroDivisionError:
                print("Error, can not devide a number by 0: ")
                continue
            # Open a txt file and add all the equations in the file.
            file = open("calculator.txt", "a")
            result = (f"{number_one} {equation_sign} {number_two} = {answer}\n")
            print(result)                   # Print the the entire equation.
            file.write(result,)             # Write the entire equation into the txt file.
            file.close()                    # Close the file with the equation saved.

            # Check with user if the program needs to stop or to repeat the process. 
            user = input("Do you want to start from beginning press Y / N ").lower()
            if user == "Y".lower():
                continue
            else:
                print("Thank you for your time! ")
                break
        break 

    # Read equations from txt file.
    elif user_choice == "2":
        while True:
            try:
                user = input("Please enter name of new txt file: ") # Asking user to give a name for the file.
                user = open("calculator.txt", "r")                  # User input equal to the file created in equation block.
                for x in user:                                      # Used for loop to print equation from the txt file.
                    print(x)
            # Handle errors.
            except FileNotFoundError:
                print("File not found try again, no previous equation made! ")
                continue
                # Check with user if the program needs to stop or to repeat the process. 
            user = input("Do you want to start from beginning press Y / N ").lower()
            if user == "Y".lower():
                continue
            else:
                print("Thank you for your time! ")
                break
        break

    # In case of invalid choice at the beginning following error will print and repeat the program.       
    else:
        print("Invalid choice! ")
            


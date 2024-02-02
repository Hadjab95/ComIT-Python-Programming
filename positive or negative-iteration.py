#An Algorithm to keep asking the user for a number by keyboard and say if the number is positive or negative

while True:
    try:
        Number = float(input("Enter a number: "))
        if Number > 0:
            print(Number, "is positive.")
        elif Number < 0:
            print(Number, "is negative.")
        else:
            print("The number is zero")
    except ValueError:
        print("Invalid input. Please enter a valid number")
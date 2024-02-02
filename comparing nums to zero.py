#An algorithm that read a number and say if it greater equal or less than zero

while True:
    try:
        num = int(input("Enter a number: "))
        if num > 0:
            print(num, "is greater than 0")
        elif num < 0:
            print(num, "is less than 0")
        else:
            print("The number is 0")
    except ValueError:
        print("Invalid input, Please enter a valid number")

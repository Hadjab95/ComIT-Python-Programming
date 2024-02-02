#This will compare two real numbers and print the largest of them
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    print("The first number is the largest")
elif num2 > num1:
    print("The second number is the largest")
else:
    print("The two numbers are equals")

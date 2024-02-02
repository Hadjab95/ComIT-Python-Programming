#An Algorith to read a number by keyboard and say if it positive or negative

Number = float(input("Enter a number: "))
if Number > 0:
    print(Number, "is positive.")
elif Number < 0:
    print(Number, "is negative.")
else:
    print("The number is 0")

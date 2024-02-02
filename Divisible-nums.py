#This algorithm will determine if an "N" number is divibles by another "M"

N = int(input("Enter a number: "))
M = int(input("Enter another numer: "))
result = N / M
if result%2 == 0:
    print("These numbers are divisible") 
else:
    print("These numbers are not divible")

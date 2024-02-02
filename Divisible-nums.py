#This algorithm will determine if an "N" number is divibles by another "M"

#N = int(input("Enter a number: "))
#M = int(input("Enter another number: "))
#result = N / M
#if result%2 == 0:
    #print("These numbers are divisible") 
#else:
    #print("These numbers are not divisible")

#Same Algorithm using a function

def divisible_numbers(n, m):
    print(f"Enter a number: {n}")
    print(f"Enter another number: {m}")
    return n%m == 0
n = 6
m = 4
result = divisible_numbers(n, m)
print(f" {n} is divisible by {m}: {result}")


    
#This algorithm will determine if an "N" number is divibles by another "M" using a Function


def divisible_numbers(n, m):
    return n%m == 0
    
n = 25
m = 5
result = divisible_numbers(n, m)
print(f" {n} is divisible by {m}: {result}")

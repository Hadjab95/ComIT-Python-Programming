#This Algorithm will determine the largest of 3 numbers

def largest_of_three (a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


largest = largest_of_three(10, 20, 15)
print("The largest number is: ", largest)
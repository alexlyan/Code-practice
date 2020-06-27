# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

# For example:

#  persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
#                        # and 4 has only one digit.

def persistence(n):
    per_count = 0
    n = str(n)

    while len(n) != 1:
        z = 1   
        for y in n:
            z *= int(y)
        n = str(z)
        per_count += 1
    return per_count

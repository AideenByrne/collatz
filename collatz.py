# The number we will perform collatz conjecture on
n = 20

# Keep looping until we reach 1
# Note: this assumes the Collatz conjecture is true

while n != 1:
# print current value of n
    print (n)

    if n % 2 == 0:
    n = n /2
    else:
    n = (3 *n) + 1

print (n)

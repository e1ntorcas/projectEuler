# Source of problem https://projecteuler.net/problem=3

def prime(n):
    # is number prime or not?
    if n <= 1:
        return False
    # all divisors
    for i in range(2, int(n ** 0.5) + 2):
        if n % i == 0:
            return False
    # if no divisors, than it's prime
    return True


# the number to we want largest prime factor of
number = 600851475143

for i in range(1, number):
#while j * number
    # Lets just find a large factor
    if number % i == 0:
        j = int(number / i)
        #print(i)
        # Is it Prime?
        if prime(j):
            print('This is our number: ', j)
            break

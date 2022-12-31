def prime(n):
    # is number prime or not?
    if n <= 1:
        return False
    # all divisors
    for i in range(2,int(n ** 0.5) +1):
        if n % i == 0:
            return False
    # if no divisors, than it's prime
    return True

numbers = list()
for i in range(1, 2000000):
    if prime(i):
        numbers.append(i)

print(sum(numbers))
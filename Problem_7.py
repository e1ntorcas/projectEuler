def prime(n):
    # is number prime or not?
    if n <= 1:
        return False
    # all divisors
    for i in range(2,n):
        if n % i == 0:
            return False
    # if no divisors, than it's prime
    return True

start = 2
count = 0
number = 0
while True:
    print(start, count)
    if count == 10001:
        print("That's it", number)
        break
    elif prime(start):
        count += 1
        number = start
        start += 1
        continue
    else:
        start += 1
        continue

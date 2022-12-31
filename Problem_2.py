# Source of problem: https://projecteuler.net/problem=2
# Even Fibonacci numbers

# for i in range(1, 4000000):
j = 1
i = 0
numbers = list()
while j < 4000000:
    k = i + j
    i = j
    j = k
    if j % 2 == 0:
        numbers.append(j)
    else:
        continue

print(numbers)
print(sum(numbers))

first, second = 0, 1
fibonacci = [first, second]
total = list()
while fibonacci[-1] < 4000000:
    a = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(a)
    if a % 2 == 0:
        total.append(a)

print(total)
print(sum(total))
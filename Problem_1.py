# Source of problem: https://projecteuler.net/problem=1
numbers = list()
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        numbers.append(i)
    else:
        pass
print(numbers)
print('Сумма всех: ', sum(numbers))
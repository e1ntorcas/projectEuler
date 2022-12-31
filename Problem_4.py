# Source of problem: https://projecteuler.net/problem=4
# Largest palindrome product

def polindrome(n):
    a = str(n)
    if a == a[::-1]:
        return True
    else:
        return False
numbers = list()
for i in range(1, 1000):
    # print(i)
    for j in range(1, 1000):
        k = i * j
        # print(k)
        if polindrome(k):
            numbers.append(k)
print(max(numbers))
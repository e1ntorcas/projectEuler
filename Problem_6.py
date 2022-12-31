# Sum square difference
# Source of problem https://projecteuler.net/problem=6

sum2 = list()
for i in range(1, 101):
    sum2.append(i)
a = sum(sum2)
dec1 = pow(a, 2)
sum1 = list()
for j in range(1, 101):
    sum1.append(pow(j, 2))
dec2 = sum(sum1)
print(dec1 - dec2)

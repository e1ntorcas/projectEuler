# Source of problem https://projecteuler.net/problem=9

for i in range(3,1000):
    for j in range(i+1, 1000):
        c_Pow = pow(i, 2) + pow(j, 2)
        c = pow(c_Pow, 0.5)
        if i + j + c == 1000:
            print('a:', i, 'b', j, 'c', c)
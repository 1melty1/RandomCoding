from math import sqrt

def sim_sqrt(num, twh=2, istheresqrt=False):
    i = twh
    while i**2 <= num/2:
        if num % (i**2) == 0:
            print('steps: ', i, '√', x/i**2)
            sim_sqrt(num/i**2, i, True)
        i += 1
    if isinstance(x/i**2, float) and not istheresqrt:
        print('Cannot further simplify')

x = int(input("simplify what? "))
sim_sqrt(x)

# 8/1/2021 by myself

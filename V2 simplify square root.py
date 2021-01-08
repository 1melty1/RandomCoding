from math import sqrt

def sim_sqrt(num, twh=2):
    i = twh # avoid starting from the i value tried before
    if sqrt(num) % 1 == 0:
        print('The answer is:', sqrt(num))
        exit()
    while i**2 <= num/2:
        if num % (i**2) == 0 and num != 0:
            print('steps: ', i, '√', num/i**2)
            sim_sqrt(num/i**2, i) # return the simplist sqrt number, i refer to line 4
        i += 1
    print('Cannot further simplify')


x = int(input("simplify what? "))
sim_sqrt(x)

# 8/1/2021 by myself
from math import sqrt

def sim_sqrt(num, twh=2):
    i = twh                                            # avoid starting from the i value tried before because if i^2 is possible to devide from i√(num/i^2) it would be divided earlier
    if sqrt(num) % 1 == 0:
        print('The answer is:', sqrt(num))             # see if it's a perfect square
        exit()
    while i**2 <= num/2:                               # reduce the number of loop i^2 cannot be greater than half of num e.g. 3^2 < 10
        if num % (i**2) == 0 and num != 0:             # condition of the number in square root can be divide by perfect square i
            print('steps: ', i, '√', num/i**2)
            sim_sqrt(num/i**2, i)                      # return the simplified sqrt number, i is the x in i√(num/i^2) (extracting the prefect square in square root)
        i += 1
    print('Cannot further simplify')                   # if it's not enter into recursion (cannot divide by perfect square) then it can't be simplified


x = int(input("simplify what? "))
sim_sqrt(x)

# 8/1/2021 by myself

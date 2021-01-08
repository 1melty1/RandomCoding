from math import sqrt

def sim_sqrt(num_in_sqrt, coef=1):
    i = int(sqrt(num_in_sqrt))
    while (i/2 < num_in_sqrt):
        if (num_in_sqrt % i**2 == 0):
                if coef == i*coef:
                    print('Cannot further simplify')
                    exit()
                coef = i*coef
                print('=', coef, '√', num_in_sqrt / i**2)
                sim_sqrt(num_in_sqrt/coef**2, coef)                
        else:
            i -= 1
x = int(input("simplify what? "))
sim_sqrt(x)

# 8/1/2021 by myself
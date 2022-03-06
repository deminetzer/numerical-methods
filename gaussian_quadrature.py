import numpy as np
import matplotlib.pyplot as plt
from math import ceil

'''
    Integral calculation using the Gaussian quadrature method
    input : polynomial, polynomial degree, interval, number of points
    output : result of the integral
'''


def change_interval(low, up):
    """
    CHANGE OF INTERVAL OF INTEGRATION TO [-1,1]
    params: Original interval
    returns: Polynomial that represents the change of the variable of the original polynomial
    """
    a2 = (up-low)/2
    a1 = (up+low)/2
    p_a1a2 = np.poly1d([a2, a1], variable='Xd')
    return p_a1a2


# Get polynomial
degree = int(input("enter degree of polynomial : "))
coefficients = []
for i in range(degree+1):
    print("                       ", degree-i)
    coefficients.append(float(input("enter coefficient for x  : ")))
p1 = np.poly1d(coefficients)
print('\n\033[1m' + "polynomial is :" + '\033[0m')
print(p1)


# Get interval
low = int(input("\n\nenter lower limit : "))
up = int(input("enter upper limit : "))
print('\033[1m' + "interval is :" + '\n\033[0m' + f'[{low},{up}]\n\n')


# Get number of points - n
n = int(input("enter number of points : "))
if n < 1:
    raise ValueError("number of points has to be bigger than 0")
min_points = ceil((degree+1)/2)
if n < min_points:
    print('\033[91m' + "\nPay attention ! An exact result will probably not be obtained.\n"
          f'For an accurate result, select at least {min_points} points' + '\033[0m', "\n")


##################################################
# Make sure the interval is [-1,1]
if up != 1 or low != -1:
    temp = p1
    x = np.arange(low, up + 1)
    y = temp(x)
    plt.plot(x, y)
    plt.axhline(color="black")
    plt.fill_between(x, y, where=[(x>low-1) and (x<up+1) for x in x])
    print('\033[1m' + f'\n\nchanging the interval from [{low},{up}] to [-1,1]' + '\033[0m')
    p1 = np.polyval(p1, change_interval(low, up))
    dXd = (up-low)/2
    p1 = p1*dXd
    p1 = np.poly1d(p1, variable='Xd')
    print('\033[1m' + "new polynomial :" + '\n\033[0m')
    print(p1)
    print('\n\033[1m' + "new interval :" + '\n\033[0m' + "[-1,1] ")


# Graphs printing
xd = np.arange(-1, 2)
yd = p1(xd)
plt.plot(xd, yd)
plt.axhline(color="black")
plt.fill_between(xd, yd, where=[(xd > -2) and (xd < 2) for xd in xd])
plt.show()


##################################################
# Get weights and nodes
x, w = np.polynomial.legendre.leggauss(n)
print('\n\033[1m' + "\n\nweights : " + '\033[0m', w)
print('\033[1m' + "nodes : " + '\033[0m', x, "\n\n")


##################################################
# Placing data in the Gaussian Quadratures formula
result = 0
print('\n\033[1m' + "Interim results : \n" + '\033[0m')
for i in range(n):
    current = w[i]*p1(x[i])
    result += current
    print(f'w({i})*f(x({i})) = {current}')
print('\n\033[1m' + "final result : " + '\033[0m', result)






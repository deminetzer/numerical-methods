from math import pow
import numpy as np

'''
    Program to approximate the integral of f(x) from a to b by Simpson's rule.
'''


def simps(f,a,b,N=50):
    '''

    Simpson's rule approximates the integral.

    Parameters
    ----------
    f : function of a single variable
    a , b : float
        Interval of integration [a,b]
    N : (even) integer
        Number of subintervals of [a,b]

    Returns
    -------
    float
        Approximation of the integral of f(x) from a to b using
        Simpson's rule with N subintervals of equal length.
    '''
    print(f'N = {N}')
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = []
    for i in x:
        y.append(f(i))
    for i in range(len(y)):
        print(f'i = {i} , x = {x[i]} , f(x) = {y[i]}')
    print('\n')
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S


print("\n*** SIMPSON METHOD ***\n")

# Get polynomial
degree = int(input("enter degree of polynomial : "))
coefficients = []
for i in range(degree+1):
    print("                       ", degree-i)
    coefficients.append(float(input("enter coefficient for x  : ")))
f = np.poly1d(coefficients)
print('\n\033[1m' + "polynomial is :" + '\033[0m')
print(f)

# Get interval
a = float(input("\nenter interval [a,b] : \na : "))
b = float(input("b : "))
if a > b:
    raise ValueError("a > b - Invalid interval")


print(f'FINAL RESULT : {simps(f, a, b)}\n')


derivative_f = np.polyder(np.polyder(np.polyder(np.polyder(f))))
h = (b-a)/50
error = (1/180)*(pow(h, 50))*(b-a)*derivative_f(1)
error = float(error)
print(f'ESTIMATED ERROR : {error}\n')
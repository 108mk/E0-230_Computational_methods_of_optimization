import numpy as np

import CMO_A2

# function and its derivatives
def f_2(x):
    return  2/( (1+2*x**2)**(3/2) )
def f_1(x):
    return 2*x/( (1+2*x**2)**(1/2) )
def f(x):
    return ( 1 + 2*x**2 )**(1/2)

# parameters for back tracking
beta = 0.9
c = 0.1

# initial step-size alpha
alpha = 1
tol = 1e-4

# backtracking to find suitable step-size alpha
k =1 # counter

# initial point
x = 1
while abs(f_1(x)) > tol:
    d = -( ( f_2(x) )**(-1) )*(f_1(x))
    
    alpha = 1
    while f(x + alpha*d) > f(x) + c*alpha*f_1(x)*d:
        alpha = beta*alpha
    
    x = x + alpha*d
    k = k+1

# final outputs
print('x_final:', round(x, 9))
print('x_final:', x)
print('num_iteration(k):', k)
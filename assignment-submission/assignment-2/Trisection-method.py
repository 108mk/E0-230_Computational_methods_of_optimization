import numpy as np
import CMO_A2

# variables
x = -1
y = 1

# tolerance
tol = 1e-4

# maximum oteration
max_iter = 100

# finding minima iteratively
for i in range(max_iter):

    r = (y+2*x)/3
    s = (2*y+x)/3

    f_r = CMO_A2.oracle1(21044, r)
    f_s = CMO_A2.oracle1(21044, s)

    if f_r <= f_s:
        x = x
        y = s
    else:
        x = r
        y = y

    if (y-x) < tol:
        break      


# Output results
print( 'num_iteration:', i )
print( 'alpha_star:', round((x+y)/2, 9) )

g_alpha_star = CMO_A2.oracle1( 21044, (x+y)/2 ) 
print('g_alpha_star:', round(g_alpha_star, 9) )

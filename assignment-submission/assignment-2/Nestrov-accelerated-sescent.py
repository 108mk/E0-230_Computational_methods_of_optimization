import numpy as np
from numpy import linalg as LA 

import CMO_A2

########################## GRADIENT DESCENT ##################################

# initial point
x_0 = [0.0, 0.0, 0.0, 0.0, 0.0]

# iterative gradient descent

def gradient_descent(x_0, alpha, tol, max_iter):
    
    x = x_0

    for i in range(max_iter):

        fx, grad_fx = CMO_A2.oracle3(21044, x)
        x = x - (alpha*grad_fx)

        if LA.norm(grad_fx) < tol:
            break

    #print results
    print('num_iteration:', i)
    print('x_star:', x)
    print('f_x_star:', round(fx, 9))
    print()

    return None

# call function: it prints num_iteration, x and fx. It returns None.
gradient_descent(x_0, alpha=0.00004, tol=1e-4, max_iter=1000)


########################## ACC. GRADIENT DESCENT ##################################

def acc_grad_descent(x_0, theta=0.142, alpha=0.00004, tol=1e-4, max_iter=1000):
    
    # variables and its initial value
    x_cur = x_0
    x_prev = x_0
    
    y = (1+theta)*x_cur


    for i in range(max_iter):

        fy, grad_fy = CMO_A2.oracle3(21044, y)
        if LA.norm(grad_fy) < tol:
            break
        
        x_cur = y - (alpha*grad_fy)

        y = x_cur + ( theta*(x_cur - x_prev) )

        x_prev = x_cur

        

    #print results
    print('num_iteration:', i)
    print('x_star:', x_cur)

    fx_cur, grad_fx_cur = CMO_A2.oracle3(21044, x_cur)
    print('f_x_star:', round(fx_cur, 9))    

    return None

# call function: it prints num_iteration, x and fx. It returns None.

x_0 = np.array([0.0, 0.0, 0.0, 0.0, 0.0])

acc_grad_descent(x_0, theta=0.142, alpha=0.00004, tol=1e-4, max_iter=1000)
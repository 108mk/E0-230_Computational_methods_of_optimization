import numpy as np
import CMO_A2

#define canonical co-ordiante axis
E = np.identity(5)

# MAtrix to store conjugate vectors in the matrix-row
U = np.zeros((5,5))

# initialize conjugate gradient u_0
U[0] = E[0]
S = np.zeros(5)

# call oracle for Q-matrix

Q = CMO_A2.oracle4(21044)

#################### Part-I ##########################################

# loop to calculate conjugate vectors

for i in range(1, 5):
    S = np.zeros(5)
    for j in range(i):
        Num = ( ( np.transpose(E[i]).dot(Q) ).dot(U[j]) )
        Den = ( ( np.transpose(U[j]).dot(Q) ).dot(U[j]) )
        S = S + ( Num/Den ) * U[j]

    U[i] = E[i] - S

print('u_0:', U[0])
print('u_1:', U[1])
print('u_2:', U[2])
print('u_3:', U[3])
print('u_4:', U[4])
print()



#################### Part-II ##########################################

# quadratic form/function
Q = CMO_A2.oracle4(21044)
b = [2.0, 1.0, 0.0, 4.0, 4.0]   # My SR Number upto one significant digit

# starting point
x = [0.0, 0.0, 0.0, 0.0, 0.0]  

# while loop iterator 
k = 1 
max_iter = 5  # k_max = n = 5 as per eigenvectors of matrix Q

# iteration searching the minima
while k <= max_iter:
    
    # helper variable to calculate step size alpha
    num = b - Q.dot(x)  # numerator to calculate alpha step size 
    den = Q.dot(U[k-1]) # denominator to calculate alpha step size

    # step size for progress
    alpha = np.transpose(U[k-1]).dot(num) / np.transpose(U[k-1]).dot(den)
    
    # iterative update for x
    x = x + alpha*U[k-1]
    k = k + 1

    
fx = (1/2)*np.transpose(x).dot(Q.dot(x)) - np.transpose(b).dot(x)

print('x_star:', x)
print('fx_star:', round(fx, 9))
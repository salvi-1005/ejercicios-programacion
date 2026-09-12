import numpy as np

A = np.array([[3,0,0],[0,(5/4),(3/4)],[0,(3/4),(5/4)]])
b = np.array([[3,2,2]]).T
x = np.array([[1,1,1]]).T

difs = []
be = np.sqrt(17) * 1/6 * 10**(-4)
while len(difs) < 1000_000:
    error = np.random.rand(3, 1)
    error_norm = np.linalg.norm(error)
    if error_norm >= 1 or error_norm == 0:
        continue
    
    error = error * be
    b_tilde = b + error
    x_tilde = np.linalg.solve(A,b_tilde)
    difs.append(np.linalg.norm(x_tilde - x))

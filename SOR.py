import numpy as np

#Takes an nxn matrix and an 1xn vector
#and solves for x by interating num_it times.

def go(A, b, w, tol_type, tol, verbose):
    
    shape = np.shape(A)
    m = shape[0]
    n = shape[1]
    
    if m != n:
        print("This solver only works for square matrices")
        print("This matrix is %dx%d." % (m, n))
        exit(1)
    
    if m != np.shape(b)[0]:
        print("b must be the same dimensions as A.")
        print("b appears to be %d elements long" % np.shape(b)[0])
        exit(1)
    
    x = np.zeros(np.shape(b))
    prev_x = np.zeros(np.shape(b))
    diff = np.zeros(np.shape(b))

    if tol_type == 'a':
        numpy_solution = np.linalg.solve(A, b);

    num_iterations = 0
    error = tol + 1.0
    max_iterations = 200
    while error > tol and num_iterations < max_iterations:
        num_iterations += 1
        for i in range(0, m):
            prev_x[i] = x[i]
            sum = b[i]
            old_x = x[i][0]
            for j in range(0, m):
                if i != j:
                    sum = sum - A[i][j]*x[j][0]
            sum = sum / A[i][i]
            x[i][0] = sum
            x[i][0] = x[i][0] * w + (1.0 - w)*old_x
        if tol_type == 'a':
            diff = np.subtract(x, numpy_solution)
            error = np.linalg.norm(diff) / np.linalg.norm(x)
        if tol_type == 'r':
            diff = np.subtract(x, prev_x)
            error = np.linalg.norm(diff) / np.linalg.norm(x)

    if verbose == 'TRUE':
        if tol_type == 'a':
            print("Using SOR to converge to an absolute error of %.8f required %d iterations." % (tol, num_iterations))
        if tol_type == 'r':
            print("Using SOR to converge to an absolute error of %.8f required %d iterations." % (tol, num_iterations))

        print("The solution is:")
        print(x)

    return num_iterations



    return
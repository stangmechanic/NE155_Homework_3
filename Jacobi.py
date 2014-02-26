import numpy as np

#Takes an nxn matrix and an 1xn vector
#and solves for x by iterating until the
#given tolerance (tol) is met. tol_type
#is a single character to indicate absolute
#or relative convergence ('a' or 'r').
#Prints the solution and required iterations
#to meet the tolerance.

def go(A, b, tol_type, tol):
    
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


    if tol_type == 'a':
        numpy_solution = np.linalg.solve(A, b);

    old_x = np.zeros(np.shape(b))
    new_x = np.zeros(np.shape(b))
    prev_x = np.zeros(np.shape(b))
#We'll hold the difference (x(i) - x) here.
    diff = np.zeros(np.shape(b))

    error = tol + 1;

    num_iterations = 0
    while error > tol:
        num_iterations += 1
        for i in range(0, m):
            prev_x[i] = new_x[i]
            sum = b[i]
            for j in range(0, m):
                if i != j:
                    sum = sum - A[i][j]*old_x[j][0]
            sum = sum / A[i][i]
            new_x[i][0] = sum
        old_x = new_x
        if tol_type == 'a':
            diff = np.subtract(new_x, numpy_solution)
            error = np.linalg.norm(diff) / np.linalg.norm(new_x)
        if tol_type == 'r':
            diff = np.subtract(new_x, prev_x)
            error = np.linalg.norm(diff) / np.linalg.norm(new_x)

    if tol_type == 'a':
        print("Using Jacobi to converge to an absolute error of %.8f required %d iterations." % (tol, num_iterations))
    if tol_type == 'r':
        print("Using Jacobi to converge to a relative error of %.8f required %d iterations." % (tol, num_iterations))

    print("The solution is:")
    print(new_x)

    return
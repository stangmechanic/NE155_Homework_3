import numpy as np
from matplotlib import pyplot as plt

import Jacobi
import GaussSeidel
import SOR

def go():

    n = 5
    w = 1.1

    #An nxn matrix of zeros
    A = np.zeros ( (n, n) )
    
    #Row indexed first, columns second
    A[0][0] =  4
    A[0][1] = -1
    
    j = 1
    #remember that the values returned by range never include the last value, e.g., they're
    #for iterating over arrays.
    for row in range (1, n-1):
        A[row][j-1] = -1
        A[row][j]   =  4
        A[row][j+1]   = -1
        j += 1
    
    A[n-1][n-2] = -1
    A[n-1][n-1] =  4
    
    b = np.zeros( (1, n))
    for i in range (0, n):
        b[0][i] = 100
    b = np.transpose(b)

    Jacobi.go(A, b, 'a', 0.000001)
    GaussSeidel.go(A, b, 'a', 0.000001)
    SOR.go(A, b, w, 'a', 0.000001, 'TRUE')

    Jacobi.go(A, b, 'r', 0.000001)
    Jacobi.go(A, b, 'r', 0.00000001)

    GaussSeidel.go(A, b, 'r', 0.000001)
    GaussSeidel.go(A, b, 'r', 0.00000001)

    SOR.go(A, b, w, 'r', 0.000001, 'TRUE')
    SOR.go(A, b, w, 'r', 0.00000001, 'TRUE')

    iterations_required = 0
    min_iterations = 200;

    omega_array = np.array(0)
    iterations_array = np.array(0)
    omega = 0.0
    omega_delta = 0.001
    omega += omega_delta
    while omega < 2.0:
        iterations_required = SOR.go(A, b, omega, 'a', 0.000000001, 'FALSE')
        if iterations_required <= 9:
            print("Omega: %f only required %d iterations." % (omega, iterations_required))

        omega_array = np.append(omega_array, omega)
        iterations_array = np.append(iterations_array, iterations_required)
        omega += omega_delta

    print(omega_array)
    print(iterations_array)

    #Plot information
    x_min = 0
    x_max = 2.0
    y_min = 0
    y_max = 200


    plt.axis([x_min, x_max, y_min, y_max])
    plt.xlabel('omega', fontsize=12, color='black')
    plt.ylabel('Required iterations', fontsize=12, color='black')

    plt.plot(omega_array, iterations_array, 'bo', label='iterations required')
             #    plt.plot(np.arange(0, n), solution, 'ro', label='explicit inversion')
             #    plt.plot(np.arange(0, n), numpy_solution, 'bo', label='numpy.linalg.solve')
             #    plt.legend(('explicit inversion', 'numpy.linalg.solve'), loc='lower center')
    plt.show()

    return
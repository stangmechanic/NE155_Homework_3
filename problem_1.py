import numpy as np
from matplotlib import pyplot as plt

def problem_1():
    
    n = 100
   
    #An nxn matrix of zeros
    A = np.zeros ( (n, n) )
    
    #Row indexed first, columns second
    A[0][0] =  2
    A[0][1] = -1
    
    j = 1
    #remember that the values returned by range never include the last value, e.g., they're
    #for iterating over arrays.
    for row in range (1, n-1):
        A[row][j-1] = -1
        A[row][j]   =  2
        A[row][j+1]   = -1
        j += 1
    
    A[n-1][n-2] = -1
    A[n-1][n-1] =  2
    
    #Returns a one row, n column array.
    b = np.zeros( (1, n))
    
    b[0][0] = 1
    
    #I don't like this, but range returns from (a to b-1), which is effectively n-2.
    for j in range (1, n - 1):
        b[0][j] = j + 1
    
    b[0][n-1] = n-1
    #Transpose that array so it becomes one column, n rows.
    b = np.transpose(b)

    condition_number = np.linalg.cond(A)
    print("The condition number of A is: %f " % condition_number)

    inverse_A = np.linalg.inv(A)
    solution = np.dot(inverse_A, b)
    
    print("The solution by inverting A, and multiplying by b is: ")
    print(solution)
    print("")

    numpy_solution = np.linalg.solve(A, b);
    
    # Verifying that the two solutions are the same, they are.
    if np.allclose(solution, numpy_solution) == True:
        print("These solutions are the same")
    else:
        print("Something went wrong...")
        exit(1)
    
    #Plot information
    x_min = 0
    x_max = n
    y_min = 0
    y_max = np.amax(solution) * 1.05
    y_min = np.amin(solution) * 1.05
    
    plt.axis([x_min, x_max, y_min, y_max])
    plt.xlabel('nth solution', fontsize=12, color='black')
    plt.ylabel('Solution value', fontsize=12, color='black')
    
    plt.plot(np.arange(0, n), solution, 'ro', label='explicit inversion')
    plt.plot(np.arange(0, n), numpy_solution, 'bo', label='numpy.linalg.solve')
    plt.legend(('explicit inversion', 'numpy.linalg.solve'), loc='lower center')
    plt.show()
    return 0


This folder should contain nine files:

README.txt
solutions.txt
main.py
problem_1.py
problem_2.pdf
problem_3.py 
SOR.py
GaussSeidel.py
Jacobi.py

The solution set is run by the command:
python main.py

and should produce the same information as is contained
in solutions.txt. Expected run time is less than five minutes. 

General notes:

Algorithms for Jacobi iteration, GaussSeidel and Successive Over Relaxation
are adapted from:

Chapra, Steven and Raymond Canale. “Numerical Methods for Engineers”. 4th ed.
New York, McGraw-Hill Higher Education, 2002. 

The code is not optimized for performance, and is intended to be somewhat
readable for debugging purposes. Three solvers are provided, Jacobi, GS, and 
SOR. See the python files description of arguments and outputs. Scripts require
the SciPy stack (www.scipy.org - thanks smart people!)

The python scripts were tested against the following configurations:
Ubuntu 13.10 with python 2.7.5+
Mac OS X 10.9.2 with python 2.7.6
Windows 7 Professional, Service Pack 1, python 2.7 (with SciPy stack from Anaconda)

The output to standard out is: 
1.b. The condition number of the matrix A (4133.642927)
1.c. The solution by inversion and multiplication:
1.e. The plot of my solution versus numpy.linalg.solve.  One of the solutions
is obscured because they are (hopefully as they should be) identical solutions.
The program should pause here until you close the plot window. Behavior might
differ on your system.

2. Handwritten solutions are provided in the problem_2.pdf. 

3.a. The required iterations and solution for each of the three solution techniques.

3.b. The required iterations and solution for given stoping criteria for each
of the tolerances. Successive over-relaxation with an appropriately chosen omega was the
fastest to converge. In each case the absolute convergence took fewer iterations than
relative convergence (I thought this was a bit odd, but probably accurate). Also, I'm 
surprised at how quickly we can converge to 10^-8 after we've made it to 10^-6. e.g., 
SOR required 8 iterations to converge to a tolerance of 10^-6, but only 10 to get to
10^-8.  Not sure if all solutions will converge this quickly after they bgin to converge,
or it's just the small number of equations, or the type of system.

3.c. I chose the easiest/lamest way I could think of to determine the optimal value for
SOR: I counted the required number of iterations to converge while stepping through 
the omega values from 0.001 to 1.999 in intervals of 0.001. The omegas which required the fewest
iterations are then printed to standard out, and a plot of 
iterations to convergence is produced. I limit the number of iterative attempts to
200. The best omegas range from 1.052 to 1.084. It's interesting
that not all omegas in this range yield the fewest number of iterations required. For example
an omega of 1.07 required ten iterations, but 1.069 only required nine iterations. This 
approach is not helpful if you need to solve the equation only once, but if we need 
to solve the equation several times, this could be helpful. Also, we know the best relaxation
values are probably near one, so we could narrow the search range to 0.8 to 1.2 or so. 

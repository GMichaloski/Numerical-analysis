import numpy as np
import math



def update_vector(matrix,vector):
    print(matrix)    
    temp_matrix = matrix
    for line in range(vector.size):
        sum_line = 0
        for column in range(vector.size):

            sum_line += temp_matrix[line,column] 
        vector[line] = sum_line

    return vector
    
# NOTE: This algorithm is not 100% reliable, as it may converge to the wrong number

# INPUT: Once you have a linear system, you'll have to follow 3 steps before using the method
#      1 - Isolate each one of the components
#      2 - Put all of these equations into a matrix, respecting the order
#      3 - Finally, use the matrix into the function 🤠
def jacobi(matrix,iteration_times):
    values_array = np.zeros(math.isqrt(matrix.size))
    for i in range(iteration_times):
        values_array = update_vector(matrix,values_array) 
        print("\n")
    return values_array


jacobi(np.matrix([[0.7,-0.2 ,-0.1],[-0.2,-1.6,-0.2],[-0.2,-0.3,0.6]]),5)
# jacobi(np.matrix([[0.7,-0.2 ,-0.1],[-0.2,-1.6,-0.2],[-0.2,-0.3,0.6]]),2)
# print(jacobi(np.matrix([[0.7,-0.2 ,-0.1],[-0.2,-1.6,-0.2],[-0.2,-0.3,0.6]]),3))
# print(jacobi(np.matrix([[0.7,-0.2 ,-0.1],[-0.2,-1.6,-0.2],[-0.2,-0.3,0.6]]),4))





# print(by_line_mult(np.matrix([[1,1,1],[2,2,2],[3,1,3]]),np.array([1,2,3])))

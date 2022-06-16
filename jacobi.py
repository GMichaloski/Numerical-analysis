import numpy as np
import math

def update_vector(matrix,vector):
    answer_vector = np.zeros(vector.size)
    for column in range(vector.size):
        for line in range(vector.size):
            if (column == line):
                answer_vector[column] += matrix[line,column]
            else:
                answer_vector[column] += matrix[line,column] * vector[line]
    return answer_vector
    
# NOTE: This algorithm is not 100% reliable, as it may converge to the wrong number

# INPUT: Once you have a linear system, you'll have to follow 3 steps before using the method
#      1 - Isolate each one of the components
#      2 - Put all of these equations into a matrix, according to the following standard: [[a1,a2,a3,...],[b1,b2,b3,...],[c1,c2,c3,...],...]
#      3 - Finally, use the matrix into the function 🤠
def jacobi(matrix,iteration_times):
    values_array = np.zeros(math.isqrt(matrix.size))
    for i in range(iteration_times):
        values_array = update_vector(matrix,values_array) 
    return values_array

print(jacobi(np.matrix([[0.7,-0.2 ,-0.2],[-0.2,-1.6,-0.3],[-0.1,-0.2,0.6]]),1))
print(jacobi(np.matrix([[0.7,-0.2 ,-0.2],[-0.2,-1.6,-0.3],[-0.1,-0.2,0.6]]),2))
print(jacobi(np.matrix([[0.7,-0.2 ,-0.2],[-0.2,-1.6,-0.3],[-0.1,-0.2,0.6]]),3))
print(jacobi(np.matrix([[0.7,-0.2 ,-0.2],[-0.2,-1.6,-0.3],[-0.1,-0.2,0.6]]),10))







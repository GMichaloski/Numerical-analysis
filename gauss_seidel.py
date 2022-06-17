import numpy as np
import math

# def update_vector(matrix,vector):
#     answer_vector = vector
#     for line in range(vector.size):
#         for column in range(vector.size):
#             debugMatrix = matrix[line,column]
#             debugVetorR = answer_vector[column] 
#             debugVetorV = answer_vector[line]
#             if (line != column):
#                 answer_vector[column] += matrix[line,column] * answer_vector[line]
#             else:
#                 answer_vector[column] += matrix[line,column]
#     return answer_vector

def update_vector(matrix,vector):
    answer_vector = vector
    for column in range(vector.size):
        for line in range(vector.size):
            debugMatrix = matrix[line,column]
            debugVetorR = answer_vector[column] 
            debugVetorV = answer_vector[line]
            if (column != line):
                answer_vector[column] += matrix[line,column] * answer_vector[line]
            else:
                answer_vector[column] += matrix[line,column]
    return answer_vector
    
# NOTE: This algorithm is not 100% reliable, as it may converge to the wrong number

# INPUT: Once you have a linear system, you'll have to follow 3 steps before using the method
#      1 - Isolate each one of the components
#      2 - Put all of these equations into a matrix, according to the following standard: [[a1,a2,a3,...],[b1,b2,b3,...],[c1,c2,c3,...],...]
#      3 - Finally, use the matrix into the function 🤠
def gauss_seidel(matrix,iteration_times):
    values_array = np.zeros(math.isqrt(matrix.size))
    for i in range(iteration_times):
        values_array = update_vector(matrix,values_array) 
    return values_array

print(gauss_seidel(np.matrix([[0.7,-0.2 ,-0.2],[-0.2,-1.6,-0.3],[-0.1,-0.2,0.6]]),1))
print(gauss_seidel(np.matrix([[0.7,-0.2 ,-0.2],[-0.2,-1.6,-0.3],[-0.1,-0.2,0.6]]),2))
print(gauss_seidel(np.matrix([[0.7,-0.2 ,-0.2],[-0.2,-1.6,-0.3],[-0.1,-0.2,0.6]]),3))
print(gauss_seidel(np.matrix([[0.7,-0.2 ,-0.2],[-0.2,-1.6,-0.3],[-0.1,-0.2,0.6]]),10))







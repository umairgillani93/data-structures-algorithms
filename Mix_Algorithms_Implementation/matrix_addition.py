import random 
import numpy as np 

def add_matrices(matrix1, matrix2):
    """returns the sum of two matrices"""
    
    result_matrix = [[0 for r in range(len(matrix1))] for c in range(len(matrix1[0]))] # result matrix shape
    
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
            
    return result_matrix
            


rows, cols = (3, 3)
mat1 = [[random.randint(0,10) for r  in range(rows)] for c in range(cols)]
mat2 = [[random.randint(0, 20) for r in range(rows)] for c in range(cols)]
print(mat1)
print(mat2)
add_matrices(mat1, mat2)

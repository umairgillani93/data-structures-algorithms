import numpy as np

def matrix_multiplication(mat1, mat2):
    "returns the product of two matrices"

    result = np.zeros((mat1.shape[0], mat2.shape[1]))

    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result



if __name__ == '__main__':
    matrix1 = np.random.rand(3,2)
    matrix2 = np.random.rand(2,3)
    print(np.matmul(matrix1, matrix2))
    print('\n')
    print(matrix_multiplication(matrix1, matrix2))

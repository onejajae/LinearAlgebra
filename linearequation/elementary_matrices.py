from matrix import *
from vector import Vector


def get_permutation_matrix(matrix_size, pivot_index, target_index):
    identity = IdentityMatrix(matrix_size)
    identity[pivot_index][pivot_index] = 0
    identity[pivot_index][target_index] = 1
    identity[target_index][target_index] = 0
    identity[target_index][pivot_index] = 1
    return identity


def get_scaling_elementary_matrix(matrix_size, pivot_index, coef_val):
    identity = IdentityMatrix(matrix_size)
    identity[pivot_index][pivot_index] = 1/coef_val
    return identity


def get_replacement_elementary_matrix(matrix_size, pivot_index, target_index, coef_val):
    identity = IdentityMatrix(matrix_size)
    if coef_val == 0:
        return identity
    else:
        identity[target_index][pivot_index] = -coef_val
        return identity


def row_operations(matrix):
    for i in range(len(matrix)-1):
        if matrix[i][i] == 0:
            for row_index in range(i, len(matrix)):
                if matrix[row_index][i] != 0:
                    print("r%d <- r%d" % (i, row_index))
                    matrix[i], matrix[row_index] = matrix[row_index], matrix[i]     #interchange
                    break
        print("r%d <- %f * r%d" % (i, 1 / matrix[i][i], i))
        matrix[i] = matrix[i] / matrix[i][i]    #scaling

        for row_index in range(i+1, len(matrix)):
            print("r%d <- r%d - (%d)r%d" % (row_index, row_index, matrix[row_index][i], i))
            matrix[row_index] = matrix[row_index] - (matrix[row_index][i] * matrix[i])   #replacement
    else:
        print("r%d <- %f * r%d" % (i + 1, 1 / matrix[i + 1][i + 1], i + 1))
        matrix[i+1] = matrix[i+1] / matrix[i+1][i+1]    #scaling

    return matrix


def get_forward_elementary_matrices_list(matrix):
    matrix_size = len(matrix)
    identity = IdentityMatrix(matrix_size)
    permutation_matrices_list = []
    forward_elementary_matrices_list = []
    for pivot_index in range(len(matrix)-1):
        if matrix[pivot_index][pivot_index] == 0:
            for target_index in range(1, len(matrix)):
                if matrix[target_index][pivot_index] != 0:
                    permutation_matrix = get_permutation_matrix(matrix_size, pivot_index, target_index)
                    permutation_matrices_list.append(permutation_matrix)
                    matrix = permutation_matrix * matrix
                    break
        scaling_elementary_matrix = get_scaling_elementary_matrix(matrix_size, pivot_index,
                                                                  matrix[pivot_index][pivot_index])
        identity[pivot_index][pivot_index] = matrix[pivot_index][pivot_index]
        forward_elementary_matrices_list.append(scaling_elementary_matrix)
        matrix = scaling_elementary_matrix * matrix

        for target_index in range(pivot_index+1, len(matrix)):
            replacement_matrix = get_replacement_elementary_matrix(matrix_size, pivot_index, target_index,
                                                                   matrix[target_index][pivot_index])
            identity[target_index][pivot_index] = matrix[target_index][pivot_index]
            forward_elementary_matrices_list.append(replacement_matrix)
            matrix = replacement_matrix * matrix

    else:
        scaling_elementary_matrix = get_scaling_elementary_matrix(matrix_size, pivot_index + 1,
                                                                  matrix[pivot_index+1][pivot_index+1])
        identity[pivot_index + 1][pivot_index + 1] = matrix[pivot_index + 1][pivot_index + 1]
        forward_elementary_matrices_list.append(scaling_elementary_matrix)
        matrix = scaling_elementary_matrix * matrix

    return identity, matrix


if __name__ == "__main__":
    a = Vector([2,6,2])
    b = Vector([-3,-8,0])
    c = Vector([4,9,2])
    m1 = Matrix([a,b,c])

    d = Vector([0.5,0,0])
    e = Vector([0,1,0])
    f = Vector([0,0,1])
    m2 = Matrix([d,e,f])

    print(get_forward_elementary_matrices_list(m1)[0])
    print(get_forward_elementary_matrices_list(m1)[1])

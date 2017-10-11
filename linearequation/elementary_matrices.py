from matrix import Matrix
from vector import Vector


def row_operations(matrix):
    for i in range(len(matrix)-1):
        if matrix[i][i] == 0:
            for row_index in range(i, len(matrix)):
                if matrix[row_index][i] != 0:
                    matrix[i], matrix[row_index] = matrix[row_index], row_index[i]  #interchange
                    print("r%d <- r%d"%(i, row_index))
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


if __name__ == "__main__":
    a=[2,3,-1,5,1]
    b=[1,-1,1,2,5]
    c=[3,2,-3,-2,8]
    d=[1,2,3,4,0]
    e=[4,5,6,7,8]
    _a = Vector(a)
    _b = Vector(b)
    _c = Vector(c)
    _d = Vector(d)
    _e = Vector(e)
    _m = Matrix([_a,_b,_c,_d,_e])
    for i in row_operations(_m):
        print(i)
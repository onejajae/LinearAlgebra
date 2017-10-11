from matrix import Matrix
from vector import Vector


def augmenting(matrix, uv):
    if len(matrix) != len(uv):
        return
    else:
        for i in range(len(matrix)):
            matrix[i].append(uv[i])
    return matrix


def forward_elimination(matrix):
    for i in range(1,len(matrix)):
        if matrix[i-1][i-1] == 0:
            for row_index in range(i,i+len(matrix[i:])):
                if matrix[row_index][i-1] != 0:
                    matrix[i-1], matrix[row_index] = matrix[row_index], matrix[i-1]
                    break
        matrix[i-1] = scaling(matrix[i-1], i-1)
        for row_index in range(i, i+len(matrix[i:])):
            matrix[row_index] = scaling(matrix[row_index],i-1)
            (matrix[i - 1], matrix[row_index]) = replacement(matrix[i-1], matrix[row_index],i-1)
    else:
        matrix[i] = scaling(matrix[i],i)
    return matrix


def backward_elimination(matrix):
    for i in range(len(matrix)-1,0,-1):
        matrix[i] = scaling(matrix[i], i)
        for row_index in range(i,0,-1):
            matrix[row_index - 1] = scaling(matrix[row_index - 1], i)
            (matrix[i], matrix[row_index - 1]) = replacement(matrix[i],matrix[row_index-1],i)
    for i in range(len(matrix)):
        matrix[i] = scaling(matrix[i],i)
    return matrix


def scaling(vec, p):
    if vec[p] == 0:
        pass
    else:
        division = vec[p]
        for i in range(len(vec)):
            vec[i] /= division
    return vec


# 속도개선 필요
def interchange(v1, v2):
    zero_index1 = -1
    for i in v1[:-1]:
        if i == 0:
            zero_index1 += 1
        else:
            break
    zero_index2 = -1
    for i in v2[:-1]:
        if i == 0:
            zero_index2 += 1
        else:
            break
    if zero_index1 > zero_index2:
        return v2, v1
    else:
        return v1, v2


def replacement(v1, v2, p):
    if v2[p]:
        for i in range(len(v1)):
            v2[i] = v2[i]-v1[i]
    return v1, v2


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
    a1=[1,0,0,0,0]
    a2=[0,1,0,0,0]
    a3=[0,0,1,0,0]
    a4=[0,0,0,1,0]
    a5=[0,0,0,0,1]
    m = [a+a1,b+a2,c+a3,d+a4,e+a5]

    q=Vector([2,3,-1])
    p=Vector([1,-1,1])
    r=Vector([3,2,-3])
    qpr = Matrix([q,p,r])
    """
    for i in qpr * Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]]):
        print(i)

    for i in forward_elimination(qpr):
        print(i)
    for i in (backward_elimination(forward_elimination(m))):
        print(i)
    for i in (backward_elimination(forward_elimination(_m))):
        print(i)
    """
    for i in forward_elimination(_m):
        print(i)

from vector import Vector


class Matrix(Vector):
    def __is_square__(self):
        if len(self) == len(self[0]):
            return True
        else:
            return False

    def __str__(self):
        ret_str = ""
        for i in range(0,len(self)-1):
            ret_str += str(self[i]) + "\n"
        else:
            ret_str += str(self[i+1])
        return ret_str

    def get_row(self, index):
        return self[index]

    def get_column(self, index):
        return Vector([self[i][index] for i in range(0, len(self[0]))])

    def __mul__(self, other):
        if isinstance(other, Matrix):
            ret_matrix = Matrix()
            for i in range(len(self)):
                row_vector = Vector()
                for j in range(len(other[0])):
                    inner_product = self.get_row(i) * other.get_column(j)
                    row_vector.append(inner_product)
                ret_matrix.append(row_vector)
            return ret_matrix
        else:
            return Matrix([i*other for i in self])

    def __rmul__(self, other):
        if isinstance(other, Matrix):
            ret_matrix = Matrix()
            for i in range(len(self)):
                row_vector = Vector()
                for j in range(len(other[0])):
                    inner_product = self.get_row(i) * other.get_column(j)
                    row_vector.append(inner_product)
                ret_matrix.append(row_vector)
            return ret_matrix
        else:
            return Matrix([i*other for i in self])

    def __sub__(self, other):
        if self.__is_square__() and other.__is_square__():
            return Matrix([self[i] - other[i] for i in range(len(self))])
        else:
            print("cannot")

    def __add__(self, other):
        if self.__is_square__() and other.__is_square__():
            ret_vec = Matrix()
            for i in range(len(self)):
                ret_vec.append(self[i]+other[i])
            return ret_vec
        else:
            print("cannot")

    def __truediv__(self, other):
        ret_vec = Matrix()
        for i in range(len(self)):
            ret_vec.append(self[i]/other)
        return ret_vec


class IdentityMatrix(Matrix):
    def __init__(self, size):
        Matrix.__init__(Matrix())
        for i in range(size):
            row_vector = Vector()
            for j in range(size):
                if i == j:
                    row_vector.append(1)
                else:
                    row_vector.append(0)
            self.append(row_vector)


if __name__ == "__main__":
    a = Vector([1,2,3,4])
    b = Vector([5,6,7,8])
    c = Vector([9,8,7,6])
    d = Vector([5,4,3,2])
    m = Matrix([a,b,c,d])
    q=Vector([2,3,-1])
    p=Vector([1,-1,1])
    r=Vector([3,2,-3])
    qpr = Matrix([q,p,r])
    print(Matrix([Vector([0.5,0,0]),Vector([0,1,0]),Vector([0,0,1])])*qpr)
    print(IdentityMatrix(10))


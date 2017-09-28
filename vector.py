class Vector(list):
    def __is_same_dimension__(self, other):
        if len(self) == len(other):
            return True
        else:
            return False

    def __add__(self, other):
        if self.__is_same_dimension__(other):
            ret_vec = Vector()
            for i in range(len(self)):
                ret_vec.append(self[i]+other[i])
            return ret_vec
        else:
            print("cannot")

    def __sub__(self, other):
        if self.__is_same_dimension__(other):
            return Vector([self[i] - other[i] for i in range(len(self))])
        else:
            print("cannot")

    def __mul__(self, other):
        if isinstance(other, Vector):
            if self.__is_same_dimension__(other):
                return sum(Vector([self[i]*other[i] for i in range(len(self))]))
            else:
                print("cannot")
        else:
            return Vector([self[i] * other for i in range(len(self))])

    def __rmul__(self, other):
        if isinstance(other, Vector):
            if self.__is_same_dimension__(other):
                return sum(Vector([self[i]*other[i] for i in range(len(self))]))
            else:
                print("cannot")
        else:
            return Vector([self[i] * other for i in range(len(self))])

    def __truediv__(self, other):
        ret_vec = Vector()
        for i in range(len(self)):
            ret_vec.append(self[i]/other)
        return ret_vec


if __name__ == "__main__":
    a = Vector([1,2,3,4])
    b = Vector([5,6,7,8])
    print(a+b+a)
    print(a-b)
    print(3*a)
    print(b/5)
    print(a*b)
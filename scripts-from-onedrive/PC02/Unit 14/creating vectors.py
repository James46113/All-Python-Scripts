import math


class Vector:
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    def __str__(self) -> str:
        return "({:.2f}, {:.2f})".format(self.__x, self.__y)

    def mag(self) -> float:
        return math.sqrt(self.__x**2 + self.__y**2)

    def __add__(self, other):
        return Vector(self.__x + other.__x, self.__y + other.__y)

    def __mul__(self, other: float):
        return Vector(self.__x * other, self.__y * other)


def from_file():
    list_of_vectors = []
    with open("vectors.txt", "r") as f:
        read = f.readlines()
        for vec in read:
            list_of_vectors.append(Vector(int(vec.split(",")[0]), int(vec.split(",")[1])))

    return list_of_vectors


rect = [Vector(0, 0), Vector(100, 0), Vector(100, 100), Vector(0, 100)]

for ind, item in enumerate(rect):
    if ind % 2 == 0:
        print(item, end="")
    else:
        print("\t", item)

v_list = from_file()
for v_ in v_list:
    print(v_)

"""
v = Vector(2, 2)
d = Vector(1, 1)
while True:
    v = v+d
    print(v)

"""
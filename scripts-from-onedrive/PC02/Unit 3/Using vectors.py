from math import sqrt

class vector:
    def __init__(self, x, y):
        self.X = x
        self.Y = y
        
    def __str__(self):
        return "{}, {}".format(self.X, self.Y)
        
    def __add__(self, other: "vector") -> "vector":
        return vector(self.X + other.X, self.Y + other.Y)
    
    def __sub__(self, other: "vector") -> "vector":
        return vector(self.X - other.X, self.Y - other.Y)
    
    def __mul__(self, other: float) -> "vector":
        return vector(self.X * other, self.Y * other)
    
    def __truediv__(self, other: float) -> "vector":
        return vector(self.X / other, self.Y * other)
    
    def __eq__(self, other: "vector") -> bool:
        return self.Y == other.Y and self.X == other.X
    
    def __len__(self):
        return int(sqrt(self.X**2 + self.Y**2))
    
    def get_x(self):
        return self.X
    
    def get_y(self):
        return self.Y
    
    
vec = vector(2, 3)
vec2 = vector(2, 4)
if vec == vec2:
    print("vectors are the same")
else:
    print("vectors are different")
print(vec.get_x(), vec.get_y())
print(vec)
print(len(vec))
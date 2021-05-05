import numpy as np


class Vector:

    def __str__(self) -> str:
        if self.z == 0:
            return f"({self.x}, {self.y})"
        else:
            return f"({self.x}, {self.y}, {self.z})"

    def __init__(self, x, y, z=0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def vector2(self):
        return [float(self.x), float(self.y)]

    def vector3(self):
        return [float(self.x), float(self.y), float(self.z)]


generated_data = np.array([Vector(i, i+3, i+0.23).vector3() for i in range(10, 30)])

print(generated_data.shape)

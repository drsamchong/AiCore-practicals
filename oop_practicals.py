# %%
from math import pi
from dateutil import parser
class Cylinder():
    def __init__(self, height, radius=1):
        self.height = height
        self.radius = radius
        self.surface_area = self.get_surface_area()
        self.volume = self.get_volume()
    
    def get_surface_area(self):
        self.surface_area = round((2 * pi * self.radius * self.height) + (2 * pi * self.radius ** 2), 2)
        return self.surface_area
    
    def get_volume(self):
        self.volume = round(self.height * pi * self.radius ** 2, 2)
        return self.volume

cyl = Cylinder(5,2)
print(cyl.surface_area, cyl.volume, cyl.radius)

# %%
class Person():
    def __init__(self, name, date_of_birth, friends=None):
        self.name = name
        self.date_of_birth = parser.parse(date_of_birth)
        self.friends = friends or []

    def __str__(self):
        return (f"{self.name}, born {self.date_of_birth}, has {len(self.friends)} friends")

    def __gt__(self, other):
        return not(self.date_of_birth > other.date_of_birth)

    def add_friend(self, other):
        self.friends.extend([friend for friend in [other.name, *other.friends] if friend != self.name])
        other.friends.extend([friend for friend in [self.name, *self.friends] if friend != other.name])
        self.friends = [*set(self.friends)]
        other.friends = [*set(other.friends)]

# %%
alan = Person("Alan", "1978-02-12", ["Ahmed", "Ann", "Aisha"])
kayleigh = Person("Kayleigh", "1978-11-03", ["Kasha", "Kate", "Kevin"])

print(alan.friends)
print(kayleigh.friends)
print(alan)
# %%

#print(kayleigh > alan)
kayleigh.add_friend(alan)# %%

# %%
print(kayleigh.friends)
# %%
print(alan.friends)
# %%
class Shape():
    def __init__(self, num_sides, tesselates=False):
        assert(num_sides != 0), "Number of sides cannot be 0"
        self.num_sides = num_sides
        self.tesselates = tesselates

    def __repr__(self):
        return self.get_info()

    def __add__(self, other):
        return Shape(num_sides=(self.num_sides + other.num_sides))

    def get_info(self):
            raise NotImplementedError("This method has not yet been implemented")



class Circle(Shape):
    def __init__(self):
        super().__init__(num_sides=1)

    def get_info(self):
        return(f"{self.num_sides} sides. Tesselates: {self.tesselates}")

class Triangle(Shape):
    def __init__(self):
        super().__init__(num_sides=3, tesselates=True)

    def get_info(self):
        return(f"{self.num_sides} sides. Tesselates: {self.tesselates}")


class Square(Shape):
    def __init__(self):
        super().__init__(num_sides=4, tesselates=True)

    def get_info(self):
        return(f"{self.num_sides} sides. Tesselates: {self.tesselates}")

class Pentagon(Shape):
    def __init__(self):
        super().__init__(num_sides=5)

    def get_info(self):
        return(f"{self.num_sides} sides. Tesselates: {self.tesselates}")


class Hexagon(Shape):
    def __init__(self):
        super().__init__(num_sides=6, tesselates=True)

    def get_info(self):
        return(f"{self.num_sides} sides. Tesselates: {self.tesselates}")

# %%

hex = Hexagon()
pen = Pentagon()
shape = Shape(2)

print(hex)

new_shape = hex + pen
print(new_shape.num_sides)

# %%

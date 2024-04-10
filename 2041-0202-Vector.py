class Vector:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
    
    # methoden zur addition
    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return Vector(self.x + other, self.y + other, self.z + other)
        else:
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        
    def __radd__(self, other):
        return Vector(self.x + other, self.y + other, self.z+  other)
        
    # methoden zur subtraktion
    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            return Vector(self.x - other, self.y - other, self.z - other)
        else:
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        
    def __rsub__(self, other):
        return Vector(other - self.x, other - self.y, other - self.z)
        
    # methoden zur multiplikation von vektoren mit vektoren und vektor mit skalar
    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
    
    def __rmul__(self, other):
        return Vector(self.x * other, self.y * other, self.z * other)
    
    # methode zur berechnung der vektorlänge
    def len(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    # methode zur berechnung des kreuzprodukt
    def cross(self, other):
        return Vector(self.y*other.z - self.z*other.y,
               self.z*other.x - self.x*other.z,
               self.x*other.y - self.y*other.x)
    
    # methode zur berechnung des skalarprodukt
    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z
    
    # methode zur normierung des vektor
    def normalize(self):
        return Vector(self.x/self.len(), self.y/self.len(), self.z/self.len())


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

v1 = Vector(2,3,6)
v2 = Vector(3,6,2)

# test __str__
print(v1)

# test addition
print(2+v1)
print(v1+2)
print(v1+v2)

# test subtraktion
print(2-v1)
print(v1-2)
print(v1-v2)

# test multiplikation
print(v1*v2)
print(2*v1)
print(v1*2)
print(2.5*v1)
print(v1*2.5)

# test kreuzprodukt
print(v1.cross(v2))

# test skalarprodukt
print(v1.dot(v2))

# test normalisierung
print(v1.normalize())

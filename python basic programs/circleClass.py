class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def circleArea(self):
        return 3.14 * self.radius * self.radius
    
    def circlePerimeter(self):
        return 2 * 3.14 * self.radius

c1 = Circle(22)
print(c1.circleArea())         
print(c1.circlePerimeter())    
print(c1.radius)

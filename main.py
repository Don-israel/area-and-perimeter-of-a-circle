class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Take input from the user
radius = float(input("Enter the radius of the circle: "))

# Create an instance of the Circle class
circle = Circle(radius)

# Calculate and display the area and perimeter
print(f"Area of the circle: {circle.area()}")
print(f"Perimeter of the circle: {circle.perimeter()}")

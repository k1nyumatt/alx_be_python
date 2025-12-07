import math


class Shape:
    """
    Base class representing a generic shape.
    """
    
    def area(self):
        """
        Calculate the area of the shape.
        This method must be overridden by derived classes.
        
        Raises:
            NotImplementedError: If not overridden in derived class
        """
        raise NotImplementedError("Subclasses must implement the area() method")


class Rectangle(Shape):
    """
    Derived class representing a rectangle.
    
    Attributes:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    """
    
    def __init__(self, length, width):
        """
        Initialize a Rectangle instance.
        
        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self):
        """
        Calculate the area of the rectangle.
        
        Returns:
            float: The area (length × width)
        """
        return self.length * self.width


class Circle(Shape):
    """
    Derived class representing a circle.
    
    Attributes:
        radius (float): The radius of the circle
    """
    
    def __init__(self, radius):
        """
        Initialize a Circle instance.
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """
        Calculate the area of the circle.
        
        Returns:
            float: The area (π × radius²)
        """
        return math.pi * self.radius ** 2


# Example usage demonstrating polymorphism
if __name__ == "__main__":
    # Create instances of different shapes
    rectangle = Rectangle(5, 3)
    circle = Circle(4)
    
    # Store shapes in a list (polymorphism)
    shapes = [rectangle, circle]
    
    # Calculate and display areas using polymorphism
    print("Demonstrating Polymorphism:")
    print("-" * 40)
    
    for shape in shapes:
        shape_type = shape.__class__.__name__
        area = shape.area()
        print(f"{shape_type} area: {area:.2f}")
    
    # Try to call area() on base Shape class (will raise error)
    print("\nTrying to call area() on base Shape class:")
    try:
        base_shape = Shape()
        base_shape.area()
    except NotImplementedError as e:
        print(f"Error: {e}")
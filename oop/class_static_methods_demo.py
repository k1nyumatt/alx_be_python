class Calculator:
    """
    A calculator class demonstrating static and class methods.
    
    Class Attributes:
        calculation_type (str): Description of the type of calculations
    """
    
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """
        Add two numbers together.
        
        Args:
            a (float): First number
            b (float): Second number
        
        Returns:
            float: The sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Multiply two numbers together.
        Prints the calculation_type class attribute before performing multiplication.
        
        Args:
            cls: The class itself
            a (float): First number
            b (float): Second number
        
        Returns:
            float: The product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Example usage
if __name__ == "__main__":
    print("Calculator Class Demonstration")
    print("=" * 40)
    
    # Using static method (no need for class instance)
    print("\nUsing static method add():")
    result_add = Calculator.add(10, 5)
    print(f"10 + 5 = {result_add}")
    
    # Using class method (prints class attribute first)
    print("\nUsing class method multiply():")
    result_multiply = Calculator.multiply(10, 5)
    print(f"10 × 5 = {result_multiply}")
    
    # Can also call methods on an instance
    print("\nCalling methods on an instance:")
    calc = Calculator()
    print(f"7 + 3 = {calc.add(7, 3)}")
    print("Calling multiply:")
    print(f"7 × 3 = {calc.multiply(7, 3)}")
    
    # Accessing class attribute
    print(f"\nClass attribute: {Calculator.calculation_type}")
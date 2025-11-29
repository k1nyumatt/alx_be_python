def safe_divide(numerator, denominator):
    """
    Safely perform division with error handling.
    
    Args:
        numerator: The number to be divided
        denominator: The number to divide by
    
    Returns:
        str: Result or error message
    """
    try:
        # Convert to float
        num = float(numerator)
        denom = float(denominator)
        
        # Perform division
        result = num / denom
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
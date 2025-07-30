def safe_divide(numerator, denominator):
    
    try:
        nume = float(numerator)
        denom = float(denominator)
        result = nume/denom
        return f"The result of the division is {result}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    
    
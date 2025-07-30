def safe_divide(numerator, denominator):
    numerator = float(numerator)
    denominator = float(denominator)
    try:
        numerator/denominator
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero.",e)
    except ValueError as e:
        print("Error: Please enter numeric values only.",e)
    except Exception as e:
        print(e)
    finally:
        print("division succesful")
def safe_divide(numerator, denominator):
    numerator = float(numerator)
    denominator = float(denominator)
    try:
        numerator/denominator
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero.",e)
    except ValueError as e:
        print("input the correct value",e)
    except Exception as e:
        print(e)
    finally:
        print("division succesful")
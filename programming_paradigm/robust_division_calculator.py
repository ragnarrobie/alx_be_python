def safe_divide(numerator, denominator):
    numerator = float(input("First number: "))
    denominator = float(input("Second number: "))
    try:
        numerator/denominator
    except ZeroDivisionError as e:
        print("number cant be divided by zero",e)
    except ValueError as e:
        print("input the correct value",e)
    except Exception as e:
        print(e)
    finally:
        print("division succesful")
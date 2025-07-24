FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
def main():
    news = float(input("Enter the temperature to convert: "))
    nee = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()
    if nee == "f":
        temp = convert_to_celsius(news)
        print(f"{news}°F is {temp}°C")
    elif nee == "c":
        tem = convert_to_fahrenheit(news)
        print(f"{news}°C is {tem}°F")
    else:
        print("Invalid temperature. Please enter a numeric value.")
main()
# try:
#     # Get user input for temperature
#     temp = input("Input the temperature you'd like to convert? (e.g., 45F, 102C, etc.): ")

#     # Extract numerical value and unit
#     degree = float(temp[:-1])
#     i_convention = temp[-1].upper()

#     # Perform conversion based on input unit
#     if i_convention == "C":
#         result = (9 * degree) / 5 + 32
#         o_convention = "Fahrenheit"
#     elif i_convention == "F":
#         result = (degree - 32) * 5 / 9
#         o_convention = "Celsius"
#     else:
#         print("Input proper convention either C or F.")
#         quit()

#     # Print the result without rounding
#     print(f'The temperature in {i_convention} to {o_convention} is {result:.2f} degrees.')

# except ValueError:
#     print("Invalid input. Please enter a valid temperature value.")
# except:
#     print("An error occurred.")


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    try:
        temperature = float(input("Enter a temperature value: "))
        unit = input("Enter the unit (Celsius or Fahrenheit): ").strip().lower()

        if unit == "celsius":
            converted_temperature = celsius_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted_temperature:.2f}°F")
        elif unit == "fahrenheit":
            converted_temperature = fahrenheit_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted_temperature:.2f}°C")
        else:
            print("Invalid unit. Please enter 'Celsius' or 'Fahrenheit'.")

    except ValueError:
        print("Invalid input. Please enter a numeric temperature value.")
    
    another_conversion = input("Do you want to convert another temperature? (yes/no): ").strip().lower()
    if another_conversion != "yes":
        break

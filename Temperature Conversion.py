print("Hey This is a Simple Temperature Converter Which Converts Celsius to Fahrenheit and viceversa")
print("==================================Temperature Converter=======================================")
print("Enter C for Celsius to Fahrenheit conversion")
print("Enter F for Fahrenheit to Celsius conversion")
choice = input("Enter your choice (C/F): \nNote:Please enter Capital Letter C or F only\n")
if choice == 'C':
    celsius = float(input("Enter temperature to be converted into Fahrenheit:  "))
    fahrenheit = round(((celsius * 9) / 5) + 32,2)
    print(f"{celsius}°C = {fahrenheit}°F")

elif choice == 'F':
    fahrenheit = float(input("Enter temperature to be converted into celsius: "))
    celsius = round(((fahrenheit - 32)*5)/9,2)
    print(f"{fahrenheit}°F = {celsius}°C")
else:
    print("It's a typo! Please enter C or F only. Thankyou...")
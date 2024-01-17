#Get user input
temperature=float(input("Enter the temperature:"))
print("For Fahrenheit the unit is F and for Celcius unit is C")
unit=input("Enter the unit(F/C):")
x=unit.upper()
#Convert the temperature
if x=='C':
    to_fahrenheit=(temperature*9/5)+32
    print("The converted temperature is:", to_fahrenheit)

elif x=='F':
    to_celcius=(temperature-32)*5/9
    print("The converted temperature is:", to_celcius)

else:
    print("Invalid unit")

    
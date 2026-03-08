"""
Hi
This
is 
first
session
"""

#from types import SimpleNamespace
#print()

#print("Hello World")

#Variables
'''
letter or _ 
no spaces
case sensitive
'''

app_name = "Temperature Converter"
version = 1.0
author = "Jai"

#print(app_name, version, author)

print("APP:", app_name)
print("Version:", version)
print("Author:", author)

print()

############ Data Types ############

#str (string) - "Hello"
#int (integer) - 10
#float (float) - 10.5
#bool (boolean) - True/False

city = "Hyd"
celsius_temp = 30.5
is_hot = True
days_in_week = 7

print("City:", city)
print("Celsius Temp:", celsius_temp)
print("Is Hot:", is_hot)
print("Days in Week:", days_in_week)

#conversion formulas
#C to F: (C * 9/5) + 32
#F to C: (F - 32) * 5/9


celsius=100
farenheit = (celsius * 9/5) + 32
print("Farenheit:", farenheit)

#farenheit to celcius   
celsius = (farenheit - 32) * 5/9
print("celcius:", celsius)

body_temp_c = 37.0
body_temp_f = (body_temp_c * 9/5) + 32
print("Body Temp Farenheit:", body_temp_f)

room_teamp_c = 25.0
room_temp_f = (room_teamp_c * 9/5) + 32
print("Room Temp Farenheit:", room_temp_f)

temp_f = 98.6
temp_c = (temp_f - 32) * 5/9
print("Temp Cel:", temp_c)

# string Concatination (+)

first = "Temperature"
second = "converter"
full_name = first + " " + second
print(full_name)

#print ("Temp is" + 37)
print("Temp is" + " " + str(37)+ " " + "Degrees Celsius")

#f-strings
temp = 32
city = "Hyderabad"
print(f"Temperature in {city} is {temp} degrees celcius")

c = 40
print(f"{c} = {(c * 9/5) + 32}")


#Rounding the Decimals :.1f :.2f :.3f
result = 100/3
print(result)
print(f"Rounded to 1 decimal: {result:.1f}")
print(f"Rounded to 2 decimals: {result:.2f}")
print(f"Rounded to 3 decimals: {result:.3f}")

#multi variables at once
c1, c2, c3 = 10, 30, 80
print(c1, c2, c3)
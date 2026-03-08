# ============================================================
# WEEK 1 MINI-PROJECT: Temperature Converter (Celsius ↔ Fahrenheit)
# ============================================================
# What is Python? → A programming language that lets you give instructions to a computer.
# What is a script? → A file ending in .py that Python reads and executes line by line.
# How to run this? → Open terminal, type: python project.py
# ============================================================


# --- STEP 1: Comments ---
# What is a comment? → A line starting with # that Python ignores. It's a note for humans.
# This entire line is a comment. Python skips it.
# Use comments to explain WHY you did something, not just WHAT.


# --- STEP 2: print() ---
# What is print()? → A built-in function that displays text on the screen.

print("--- Temperature Converter ---")    # prints the title to the screen
print("==========================")      # prints a separator line
print()                                  # prints an empty line (adds spacing)


# --- STEP 3: Variables ---
# What is a variable? → A name that stores a value. Like a labeled box.
# Rules: must start with a letter or _, no spaces, case-sensitive.

app_name = "Temperature Converter"       # storing a text value (string) in a variable called app_name
version = 1                              # storing a whole number (integer) in a variable called version
author = "Your Name"                     # change this to your actual name

print("App:", app_name)                  # printing the value stored in app_name
print("Version:", version)               # printing the value stored in version
print("Author:", author)                 # printing the value stored in author
print()                                  # empty line for spacing


# --- STEP 4: Data Types ---
# What is a data type? → The kind of value a variable holds.
# str (string)   → text, written in quotes:  "hello"
# int (integer)  → whole numbers:            42
# float          → decimal numbers:          36.6
# bool (boolean) → True or False

city = "Mumbai"                          # str  → text wrapped in quotes
celsius_temp = 37.5                      # float → a number with a decimal point
is_hot = True                            # bool → either True or False
days_in_week = 7                         # int  → a whole number, no decimal

print("City:", city)                     # prints: City: Mumbai
print("Temperature:", celsius_temp)      # prints: Temperature: 37.5
print("Is it hot?", is_hot)              # prints: Is it hot? True
print("Days in week:", days_in_week)     # prints: Days in week: 7
print()


# --- STEP 5: The Conversion Formula ---
# Formula: Fahrenheit = (Celsius × 9/5) + 32
# Formula: Celsius = (Fahrenheit - 32) × 5/9

celsius = 100                            # setting celsius to 100 (boiling point of water)
fahrenheit = (celsius * 9/5) + 32        # applying the formula: (100 × 9/5) + 32 = 212.0

print("Celsius:", celsius)               # prints: Celsius: 100
print("Fahrenheit:", fahrenheit)          # prints: Fahrenheit: 212.0
print()


# --- STEP 6: More Conversions ---

body_temp_c = 37.0                                    # average human body temperature in Celsius
body_temp_f = (body_temp_c * 9/5) + 32                # converting to Fahrenheit: 98.6
print("Body temp:", body_temp_c, "°C =", body_temp_f, "°F")  # prints both values

freezing_c = 0                                        # water freezing point in Celsius
freezing_f = (freezing_c * 9/5) + 32                  # converting: 32.0
print("Freezing:", freezing_c, "°C =", freezing_f, "°F")

room_temp_c = 22                                      # comfortable room temperature
room_temp_f = (room_temp_c * 9/5) + 32                # converting: 71.6
print("Room temp:", room_temp_c, "°C =", room_temp_f, "°F")
print()


# --- STEP 7: Reverse Conversion (Fahrenheit → Celsius) ---

temp_f = 98.6                            # starting with Fahrenheit value
temp_c = (temp_f - 32) * 5/9            # applying reverse formula: (98.6 - 32) × 5/9 = 37.0
print(temp_f, "°F =", temp_c, "°C")     # prints: 98.6 °F = 37.0 °C

temp_f2 = 212                            # boiling point in Fahrenheit
temp_c2 = (temp_f2 - 32) * 5/9          # converting back: 100.0
print(temp_f2, "°F =", temp_c2, "°C")   # prints: 212 °F = 100.0 °C
print()


# --- STEP 8: String Concatenation ---
# What is concatenation? → Joining strings together with +

first = "Temperature"                    # first part of the text
second = "Converter"                     # second part
full_name = first + " " + second         # joining with a space in between
print(full_name)                         # prints: Temperature Converter

# You CANNOT concatenate a string + number directly. This would crash:
# print("Temp is " + 37)               # ❌ ERROR: can't add str + int
# Fix: convert the number to string with str()
print("Temp is " + str(37) + "°C")      # ✅ prints: Temp is 37°C
print()


# --- STEP 9: f-strings (Best Way to Format Text) ---
# What is an f-string? → A string starting with f"..." that lets you put variables inside {}.

temp = 25                                           # temperature value
city = "Delhi"                                      # city name
print(f"The temperature in {city} is {temp}°C")     # prints: The temperature in Delhi is 25°C

# You can put math inside {} too
c = 40                                              # 40 degrees Celsius
print(f"{c}°C = {(c * 9/5) + 32}°F")               # prints: 40°C = 104.0°F

# Rounding decimals with :.1f (1 decimal place) and :.2f (2 decimal places)
# (the degree symbol works fine on Windows)
result = 100 / 3                                    # equals 33.33333...
print(f"Rounded to 1 decimal: {result:.1f}")        # prints: 33.3
print(f"Rounded to 2 decimals: {result:.2f}")       # prints: 33.33
print()


# --- STEP 10: Multiple Variables at Once ---
# What is multiple assignment? → Setting several variables in one line.

c1, c2, c3 = 0, 20, 100                 # assigning 3 values to 3 variables in one line
f1 = (c1 * 9/5) + 32                    # converting each one
f2 = (c2 * 9/5) + 32
f3 = (c3 * 9/5) + 32

print(f"{c1}°C = {f1}°F")               # prints: 0°C = 32.0°F
print(f"{c2}°C = {f2}°F")               # prints: 20°C = 68.0°F
print(f"{c3}°C = {f3}°F")               # prints: 100°C = 212.0°F
print()


# ============================================================
# FINAL OUTPUT: A Nice Summary Table
# ============================================================

print("=" * 40)                          # prints 40 equal signs (= repeated 40 times)
print(f"{'Celsius':>15} {'Fahrenheit':>15}")  # right-aligned headers with :>15
print("=" * 40)

# Converting a batch of temperatures
temps_celsius = [0, 10, 20, 25, 30, 37, 40, 100]    # a list of Celsius values (lists are covered in Week 5)

for c in temps_celsius:                  # for loop goes through each value (loops are covered in Week 4)
    f = (c * 9/5) + 32                  # convert each Celsius value
    print(f"{c:>12}°C {f:>12.1f}°F")    # print formatted: right-aligned, 1 decimal

print("=" * 40)
print()


# ============================================================
# 🎯 CHALLENGES — Try these yourself!
# ============================================================
# 1. Add 5 more temperatures to the list and run the script
# 2. Create a variable for YOUR city's temperature and convert it
# 3. Convert -40°C to Fahrenheit (hint: something interesting happens)
# 4. Make a "Kelvin Converter" → Kelvin = Celsius + 273.15
# 5. Print your name, age, and favorite temperature using f-strings
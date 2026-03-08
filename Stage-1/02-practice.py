# ============================================================
# WEEK 2 MINI-PROJECT: Simple Calculator
# ============================================================
# What you'll learn by building this:
#   - Strings, integers, floats, booleans
#   - Basic math operations (+, -, *, /, //, %, **)
#   - String formatting (f-strings, .format())
#   - Type conversion (int(), float(), str())
# ============================================================


# --- STEP 1: Math Operations ---
# What are operators? → Symbols that perform math on numbers.

a = 20                                   # first number
b = 7                                    # second number

print("📐 Basic Math Operations")
print("=" * 35)
print(f"a = {a}, b = {b}")              # showing the values we're working with
print()

print(f"{a} + {b} = {a + b}")           # addition → 27
print(f"{a} - {b} = {a - b}")           # subtraction → 13
print(f"{a} * {b} = {a * b}")           # multiplication → 140
print(f"{a} / {b} = {a / b}")           # division → 2.857... (always returns a float)
print(f"{a} // {b} = {a // b}")         # floor division → 2 (drops the decimal, keeps whole number)
print(f"{a} % {b} = {a % b}")           # modulo → 6 (remainder after division: 20 ÷ 7 = 2 remainder 6)
print(f"{a} ** {b} = {a ** b}")         # exponent → 20^7 = 1,280,000,000
print()


# --- STEP 2: Integer vs Float ---
# What is an int? → A whole number with no decimal point: 5, -3, 100
# What is a float? → A number WITH a decimal point: 3.14, -0.5, 7.0

x = 10                                   # this is an int (no decimal)
y = 3.0                                  # this is a float (has decimal)

print("📊 Integer vs Float")
print("=" * 35)
print(f"{x} is type: {type(x)}")         # type() tells you what kind of value it is → <class 'int'>
print(f"{y} is type: {type(y)}")         # → <class 'float'>

# When you mix int and float, Python gives you a float
result = x + y                           # int + float = float
print(f"{x} + {y} = {result}")           # 10 + 3.0 = 13.0
print(f"Result type: {type(result)}")    # → <class 'float'>

# Division ALWAYS returns a float, even with two ints
print(f"10 / 2 = {10 / 2}")             # 5.0 (not 5)
print(f"10 // 2 = {10 // 2}")           # 5 (floor division keeps it as int)
print()


# --- STEP 3: Strings ---
# What is a string? → Text wrapped in quotes. Single '' or double "" both work.

name = "Calculator"                      # double quotes
version = 'v2.0'                         # single quotes — same thing
description = "A simple math tool"       # use whichever you prefer, just be consistent

print("📝 Strings")
print("=" * 35)
print(f"Name: {name}")
print(f"Version: {version}")
print(f"Description: {description}")
print(f"Name length: {len(name)}")       # len() counts characters in a string → 10
print()

# String methods — built-in functions that transform strings
text = "hello world"
print(f"Original:    '{text}'")
print(f".upper():    '{text.upper()}'")       # converts to ALL CAPS → 'HELLO WORLD'
print(f".lower():    '{text.lower()}'")       # converts to all lowercase → 'hello world'
print(f".title():    '{text.title()}'")       # capitalizes First Letter Of Each Word → 'Hello World'
print(f".capitalize(): '{text.capitalize()}'") # capitalizes only the first letter → 'Hello world'
print(f".replace():  '{text.replace('world', 'Python')}'")  # replaces text → 'hello Python'
print(f".count('l'): {text.count('l')}")      # counts how many times 'l' appears → 3
print(f".find('world'): {text.find('world')}") # finds position of 'world' → 6 (0-indexed)
print(f".startswith('hello'): {text.startswith('hello')}")  # True
print(f".endswith('world'): {text.endswith('world')}")      # True
print()


# --- STEP 4: String Indexing & Slicing ---
# What is indexing? → Accessing a single character by position. Starts at 0.
# What is slicing? → Grabbing a portion of a string with [start:end].

word = "PYTHON"
#        P  Y  T  H  O  N
#        0  1  2  3  4  5     ← positive index (left to right)
#       -6 -5 -4 -3 -2 -1    ← negative index (right to left)

print("🔡 String Indexing & Slicing")
print("=" * 35)
print(f"word = '{word}'")
print(f"word[0] = '{word[0]}'")          # first character → 'P'
print(f"word[1] = '{word[1]}'")          # second character → 'Y'
print(f"word[-1] = '{word[-1]}'")        # last character → 'N'
print(f"word[-2] = '{word[-2]}'")        # second to last → 'O'
print(f"word[0:3] = '{word[0:3]}'")      # characters 0,1,2 (end is excluded) → 'PYT'
print(f"word[2:5] = '{word[2:5]}'")      # characters 2,3,4 → 'THO'
print(f"word[:3] = '{word[:3]}'")        # from start to index 3 → 'PYT'
print(f"word[3:] = '{word[3:]}'")        # from index 3 to end → 'HON'
print(f"word[::-1] = '{word[::-1]}'")    # reversed → 'NOHTYP'
print()


# --- STEP 5: Booleans ---
# What is a boolean? → A value that is either True or False. Used for decisions.

print("✅ Booleans & Comparisons")
print("=" * 35)

is_positive = 10 > 0                     # 10 greater than 0? → True
is_negative = 10 < 0                     # 10 less than 0? → False
is_equal = 5 == 5                        # 5 equals 5? → True (== is comparison, = is assignment)
is_not_equal = 5 != 3                    # 5 not equal to 3? → True
is_big = 100 >= 50                       # 100 greater than or equal to 50? → True

print(f"10 > 0  → {is_positive}")
print(f"10 < 0  → {is_negative}")
print(f"5 == 5  → {is_equal}")
print(f"5 != 3  → {is_not_equal}")
print(f"100 >= 50 → {is_big}")

# Booleans with strings
print(f"'abc' == 'abc' → {'abc' == 'abc'}")      # True — same text
print(f"'abc' == 'ABC' → {'abc' == 'ABC'}")      # False — case matters
print(f"'a' < 'b' → {'a' < 'b'}")                # True — alphabetical comparison

# bool() converts values to True or False
print(f"bool(1) → {bool(1)}")           # True — any non-zero number is True
print(f"bool(0) → {bool(0)}")           # False — zero is False
print(f"bool('hello') → {bool('hello')}")  # True — any non-empty string is True
print(f"bool('') → {bool('')}")          # False — empty string is False
print()


# --- STEP 6: Type Conversion ---
# What is type conversion? → Changing a value from one type to another.
# int()   → converts to integer
# float() → converts to decimal
# str()   → converts to string
# bool()  → converts to boolean

print("🔄 Type Conversion")
print("=" * 35)

# String to Number
age_str = "25"                           # this is a string, not a number
age_int = int(age_str)                   # converting string → integer
print(f"'{age_str}' (str) → {age_int} (int)")
print(f"Can do math now: {age_int + 5}") # 30 — works because it's now a number

# Float to Int (drops the decimal, does NOT round)
price = 19.99
price_int = int(price)                   # chops off .99 → 19
print(f"{price} (float) → {price_int} (int)")

# Int to Float
count = 42
count_float = float(count)              # adds .0 → 42.0
print(f"{count} (int) → {count_float} (float)")

# Number to String
score = 100
score_str = str(score)                  # now it's "100" (text, not number)
print(f"{score} (int) → '{score_str}' (str)")
print(f"Can concatenate: 'Score: ' + '{score_str}' = 'Score: {score_str}'")

# round() — proper rounding
pi = 3.14159
print(f"round({pi}, 2) = {round(pi, 2)}")     # 3.14 — round to 2 decimal places
print(f"round({pi}, 0) = {round(pi, 0)}")     # 3.0 — round to 0 decimals
print(f"round(2.5) = {round(2.5)}")            # 2 — Python rounds to nearest EVEN (banker's rounding)
print(f"round(3.5) = {round(3.5)}")            # 4
print()


# --- STEP 7: String Formatting (3 Ways) ---
# There are 3 ways to insert variables into strings:

name = "Python"
year = 2026

# Way 1: f-strings (BEST — use this one)
print(f"Learning {name} in {year}")      # f"..." with {variable} inside

# Way 2: .format() method (older but still common)
print("Learning {} in {}".format(name, year))  # {} gets replaced in order

# Way 3: % formatting (oldest, avoid in new code)
print("Learning %s in %d" % (name, year))  # %s = string, %d = integer
print()

# f-string formatting tricks
price = 49.99
quantity = 1000000

print(f"Price: ${price:.2f}")            # .2f → 2 decimal places → $49.99
print(f"Price: ${price:.0f}")            # .0f → no decimals → $50
print(f"Quantity: {quantity:,}")          # :, → adds commas → 1,000,000
print(f"Percentage: {0.856:.1%}")        # :.1% → converts to percentage → 85.6%
print(f"{'Left':<15}|")                  # :<15 → left-align in 15 chars
print(f"{'Center':^15}|")               # :^15 → center in 15 chars
print(f"{'Right':>15}|")                # :>15 → right-align in 15 chars
print()


# ============================================================
# STEP 8: THE CALCULATOR — Putting It All Together
# ============================================================

print("🧮 SIMPLE CALCULATOR")
print("=" * 40)

# Defining two numbers to calculate with
num1 = 150.75                            # first number (float)
num2 = 23                                # second number (int)

print(f"Number 1: {num1}")
print(f"Number 2: {num2}")
print(f"Types: {type(num1).__name__}, {type(num2).__name__}")  # __name__ gives just "float", "int"
print("-" * 40)

# Perform all operations
addition = num1 + num2                   # 173.75
subtraction = num1 - num2               # 127.75
multiplication = num1 * num2            # 3467.25
division = num1 / num2                  # 6.554...
floor_div = num1 // num2               # 6.0
remainder = num1 % num2                 # 12.75
power = num2 ** 2                       # 529

# Display results with formatting
print(f"  {num1} + {num2}  = {addition:.2f}")
print(f"  {num1} - {num2}  = {subtraction:.2f}")
print(f"  {num1} × {num2}  = {multiplication:.2f}")
print(f"  {num1} ÷ {num2}  = {division:.2f}")
print(f"  {num1} // {num2} = {floor_div:.2f}")
print(f"  {num1} % {num2}  = {remainder:.2f}")
print(f"  {num2}²          = {power}")
print("-" * 40)

# Absolute value — distance from zero
print(f"  abs(-42) = {abs(-42)}")        # abs() removes the negative sign → 42
print(f"  abs(42)  = {abs(42)}")         # already positive → 42

# Min and Max
print(f"  min({num1}, {num2}) = {min(num1, num2)}")  # smaller value → 23
print(f"  max({num1}, {num2}) = {max(num1, num2)}")  # larger value → 150.75

print("=" * 40)
print()


# ============================================================
# STEP 9: Batch Calculations Table
# ============================================================

print("📊 BATCH CALCULATION TABLE")
print("=" * 55)
print(f"{'A':>6} {'B':>6} {'A+B':>8} {'A-B':>8} {'A×B':>10} {'A÷B':>8}")
print("-" * 55)

# Each pair is (a, b) — we calculate all operations for each
pairs = [(10, 3), (25, 4), (100, 7), (50, 8), (99, 11)]

for a, b in pairs:                       # loop through each pair (loops = Week 4, sneak peek)
    print(f"{a:>6} {b:>6} {a+b:>8} {a-b:>8} {a*b:>10} {a/b:>8.2f}")

print("=" * 55)
print()


# ============================================================
# 🎯 CHALLENGES — Try these yourself!
# ============================================================
# 1. Change num1 and num2 to your own values and run the script
# 2. Add a "square root" operation (hint: number ** 0.5)
# 3. Convert a temperature string "98.6" to a float, then to Celsius
# 4. Create a receipt: item name (str), price (float), quantity (int), total
# 5. Use string methods to check if a user's input "YES" matches "yes"
# 6. Try: what happens when you do int("hello")? Why does it crash?
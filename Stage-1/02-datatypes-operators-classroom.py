a = 20 
b = 7

print("Basic math operations")
print("=" * 35)
print(f"a = {a}, b = {b}")
print()

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a**b}")

## "" ''

print("strings")
print("*" * 35)

name = "calc"
version = '2.0'
description = "A math tool"

print(f"Name: {name}")
print(f"Version: {version}")
print(f"Name length: {len(name)}")
print()    

text = "DevOps AI"
print(f"Original: '{text}'")
print(f"upper: {text.upper()}")
print(f"lower: {text.lower()}")
print(f"title: {text.title()}")
#print(f"capitalie: {text.capitalie()}")
print(f"replace: {text.replace('AI','AgenticAI')}")

word = "PYTHON"
# P Y T H O N
# 0 1 2 3 4 5
# -6 -5 -4 -3 -2 -1

print(f"word[0] = {word[0]}")
print(f"word[1] = {word[1]}")
print(f"word[-1] = {word[-1]}")
print(f"word[0:3] = {word[0:3]}")
print(f"word[::-1] = {word[::-1]}")

is_positive = 10 > 0
is_negative = 10 < 0
is_equal = 20 == 20

print(f"{is_positive}")
print(f"{is_equal}")
print(f"{is_negative}")

#int() 
#float()
#str()
#bool()

age_str = "25"
age_int = int(age_str)

print(f"{age_int} + 5")

#print(f"{age_str + 5}")
print(f"{age_int + 5}")

###################################

print("Simple calc")
print("=" * 50)

num1 = 250.40
num2 = 23

addition = num1 + num2
print(f"{'Center':>9}")
print(f"{'Right':>9}")
print(f"{'Left':>9}")
# ============================================================
# PYTHON CHEAT SHEET — Stage 1 Syntax Only
# ============================================================

# --- COMMENTS ---
# Single line comment
# Use # to write notes Python ignores

# --- PRINT ---
print("Hello")                        # print text
print()                               # print empty line
print("=" * 30)                       # repeat character 30 times

# --- VARIABLES ---
name = "Jai"                          # str   → text in quotes
age = 25                              # int   → whole number
temp = 36.6                           # float → decimal number
is_active = True                      # bool  → True or False

# --- MULTIPLE ASSIGNMENT ---
a, b, c = 1, 2, 3                     # assign 3 values in one line

# --- DATA TYPES ---
str("42")                             # convert to string
int("42")                             # convert to integer
float("3.14")                         # convert to float
bool(1)                               # convert to boolean → True

# --- ARITHMETIC OPERATORS ---
# +   addition         10 + 3  = 13
# -   subtraction      10 - 3  = 7
# *   multiplication   10 * 3  = 30
# /   division         10 / 3  = 3.333
# //  floor division   10 // 3 = 3
# %   modulus          10 % 3  = 1
# **  power            10 ** 3 = 1000

# --- COMPARISON OPERATORS ---
# ==  equal            10 == 10  → True
# !=  not equal        10 != 5   → True
# >   greater than     10 > 5    → True
# <   less than        5  < 10   → True
# >=  greater or equal 10 >= 10  → True
# <=  less or equal    5  <= 10  → True

# --- LOGICAL OPERATORS ---
# and  both must be True     True and True  → True
# or   at least one True     True or False  → True
# not  flips the value       not True       → False

# --- F-STRINGS ---
print(f"Name: {name}")                # insert variable into string
print(f"Age: {age + 1}")              # math inside {}
print(f"{3.14159:.2f}")               # round to 2 decimal places → 3.14
print(f"{'Right':>10}")               # right-align in 10 chars
print(f"{'Left':<10}")                # left-align in 10 chars
print(f"{'Center':^10}")              # center-align in 10 chars

# --- STRING METHODS ---
text = "hello world"
text.upper()                          # → "HELLO WORLD"
text.lower()                          # → "hello world"
text.title()                          # → "Hello World"
text.replace("world", "Python")       # → "hello Python"
len(text)                             # → 11 (number of characters)

# --- STRING INDEXING & SLICING ---
word = "PYTHON"
# Index:  P  Y  T  H  O  N
#         0  1  2  3  4  5
#        -6 -5 -4 -3 -2 -1
word[0]                               # → "P"   (first char)
word[-1]                              # → "N"   (last char)
word[0:3]                             # → "PYT" (index 0 to 2)
word[::-1]                            # → "NOHTYP" (reversed)

# --- STRING CONCATENATION ---
full = "Hello" + " " + "World"        # join strings with +
print("Age: " + str(25))              # must convert int to str first

# --- INPUT ---
name = input("Enter name: ")          # always returns a string
age  = int(input("Enter age: "))      # convert to int right away

# --- IF / ELIF / ELSE ---
if age > 18:
    print("Adult")
elif age == 18:
    print("Just turned adult")
else:
    print("Minor")

# --- NESTED CONDITIONS ---
if age > 18:
    if age > 60:
        print("Senior")
    else:
        print("Adult")

# --- IMPORT ---
import random                         # import a built-in module
random.randint(1, 10)                 # random integer between 1 and 10

# ============================================================
# QUICK REFERENCE CARD
# ============================================================
# print(x)              → display x
# input("msg")          → get user input as string
# int() float() str()   → type conversion
# f"{var}"              → f-string formatting
# f"{val:.2f}"          → 2 decimal places
# f"{val:>10}"          → right-align width 10
# len(text)             → length of string
# text.upper/lower()    → change case
# text.replace(a,b)     → swap substring
# word[i]               → index character
# word[a:b]             → slice string
# word[::-1]            → reverse string
# if/elif/else          → conditional branching
# import module         → load extra tools
# random.randint(a,b)   → random number a to b
# ============================================================

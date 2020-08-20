
"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A value Error occurs when the number is divided by a decimal example 5/2.5 gives an error
2. When will a ZeroDivisionError occur?
A ZeroDivisionError occurs when dividing by 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Not sure
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")


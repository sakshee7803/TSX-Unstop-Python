#Program to calculate the area and perimeter of a rectangle
length = 5
width = 3

area = length * width
perimeter = 2 * (length + width)

print("Area:", area)
print("Perimeter:", perimeter)

#Program to compare two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is greater.")
elif a < b:
    print("First number is smaller.")
else:
    print("Both numbers are equal.")


#Program to check leap year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")


##Program for arithmetic and logical operators
# Taking input from the user
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
# Arithmetic Operations
print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
# Logical Operators
print("Logical Operators:")
print("a > 0 and b > 0:", a > 0 and b > 0)
print("a > 0 or b > 0:", a > 0 or b > 0)
print("not (a > 0):", not (a > 0))



#Program to Concatenate two strings
str1 = "Hello"
str2 = "World"

result = str1 + " " + str2
print("Concatenated string:", result)


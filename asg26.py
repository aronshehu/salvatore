# 1. Area or Perimeter of a Rectangle
def rectangle_calc():
    num1 = 4
    num2 = 8
    choice = input("Do you want to find area or perimeter: ")

    if choice == "area":
        print(num1 * num2)
    elif choice == "perimeter":
        print(2 * num1 + 2 * num2)
    else:
        print("Invalid choice")


# 2. Celsius to Fahrenheit
def celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    print((celsius * 9 / 5) + 32)


# 3. Fahrenheit to Celsius
def fahrenheit_to_celsius():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print((fahrenheit - 32) * 5 / 9)


# 4. Separating Tens and Ones
def separate_digits():
    number = int(input("Enter a 2-digit number: "))
    tens = number // 10
    ones = number % 10
    print("Tens:", tens)
    print("Ones:", ones)


# 5. Single Student Grade and Result
def student_grade():
    name = input("Student name: ")
    score = float(input("Enter the test score: "))

    if score >= 90:
        grade = "A"
        result = "Pass"
    elif score >= 80:
        grade = "B"
        result = "Pass"
    elif score >= 70:
        grade = "C"
        result = "Pass"
    elif score >= 60:
        grade = "D"
        result = "Pass"
    else:
        grade = "F"
        result = "Fail"

    print("Student Name:", name)
    print("Score:", score)
    print("Grade:", grade)
    print("Result:", result)


# 6. Counting Even and Odd Numbers
def count_even_odd():
    even_count = 0
    odd_count = 0

    num = 1
    while num != 0:
        num = int(input("Enter a number (0 to stop): "))
        if num != 0:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    print("Even numbers:", even_count)
    print("Odd numbers:", odd_count)


# 7. Pyramid Layers
def pyramid_layers():
    top_layer = 1
    layers = 0
    blocks = int(input("Enter the number of blocks: "))

    while blocks >= top_layer:
        blocks -= top_layer
        top_layer += 1
        layers += 1

    print("Number of layers:", layers)
    print("Remaining blocks:", blocks)


# 8. Multiple Students and Grades (Lists)
def multiple_students():
    names = []
    grades = []

    name = input("Student name (type 'stop' to finish): ")

    while name != "stop":
        score = float(input("Enter the test score: "))

        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"

        names.append(name)
        grades.append(grade)

        name = input("Student name (type 'stop' to finish): ")

    print("All student names:")
    print(names)

    print("All grades:")
    print(grades)

    print("Students with their grades:")
    for i in range(len(names)):
        print(names[i], "-", grades[i])


# 9. Uppercase Word Without Vowels
def no_vowels():
    word = input("Enter a word: ")
    word = word.upper()

    for letter in word:
        if letter not in "AEIOU":
            print(letter, end="")
    print()


# ---- FUNCTION CALLS ----
rectangle_calc()
celsius_to_fahrenheit()
fahrenheit_to_celsius()
separate_digits()
student_grade()
count_even_odd()
pyramid_layers()
multiple_students()
no_vowels()

#2
def days_in_month(year, month):
    if month == 2:
        return 28
    elif month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    else:
        return "invalid"
print(days_in_month(2007, 9))

#3
def day_in_week(year, month, day):
    if month == 1:
        month = 13
        year = year - 1
    elif month == 2:
        month = 14
        year = year - 1

    k = year % 100
    j = year // 100

    h = (day + (13 * (month + 1)) // 5 + k + (k // 4) + (j // 4) + 5 * j) % 7

    if h == 0:
        return "Saturday"
    elif h == 1:
        return "Sunday"
    elif h == 2:
        return "Monday"
    elif h == 3:
        return "Tuesday"
    elif h == 4:
        return "Wednesday"
    elif h == 5:
        return "Thursday"
    else:
        return "Friday"


print(day_in_week(2026, 1, 26))

def prime_nr(a):
    if a <= 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i + 1
    return True

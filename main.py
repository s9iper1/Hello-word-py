# def print_hi(name):
#     print("Hello Bilal") # Press Ctrl+F8 to toggle the breakpoint.
#
#
# if __name__ == '__main__':
#     print_hi('PyCharm')

print("This is a test")
print("" * 10)
price = 10
rating = 1.0
is_published = True
print(price)
name = input('What is your name ? \n')
favorite_color = input('What is your favorite color ? \n')
print(name + ' likes '+ favorite_color + ' color')
birth_year = input("whats is your birth year ? \n")
print(type(birth_year))
age = 2022 - int(birth_year)
print(type(age))

print(age)
user_weight_in_pounds = float(input("what is your weight in pounds ? \n"))
weight_in_kilo_grams = user_weight_in_pounds * 0.453592
print('weight in kg is ' + str(weight_in_kilo_grams))
course = 'Python for starters'
print(course[-3])
print(course[:4])
name = 'Bilal'
print(name[1:-1])
first_name = 'Bilal'
last_name = 'shahid'
message = first_name + '[' + last_name + '] is programmer'
msg = f'{first_name} [{last_name}] is a programmer'
print(msg)
print(message)
course = 'Python for beginners'
print(course.replace('P', 'J'))
if "Python" in course:
    print("yes")
else:
    print("No")
print(10 ** 3)
x = (2+3) * (10 - 3)
print(x)

import math

print(math.floor(2.9))

is_hot = False
is_cold = True

if is_hot:
    print("it's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear Warm clothes")
else:
    print("Enjoy your day")
price = 100000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment : {down_payment}")

has_high_income = False
has_good_credit = True
has_no_criminal_record = False

# if has_high_income and has_good_credit:
#     print("Eligible for loan")

if not has_no_criminal_record and has_good_credit:
    print("Eligible for loan")

temperature = 35

if temperature != 30:
    print("its a hot day")
else:
    print("its not a hot day")

name = 'My name is bilal shahid and this is a test test test'
print(len(name))
if len(name) < 5:
    print("Name cannot be too short")
elif len(name) >= 50:
    print("Name is too long")
else:
    print("Name looks good")
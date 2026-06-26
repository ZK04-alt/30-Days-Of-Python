# Day 2: 30 Days of python programming

first_name = "zunair"
last_name = "ali khan"

full_name = first_name + " " + last_name

country = "Pakistan"
city = "Lahore"
age = "18"

year = "2026"

is_married = False
is_true = True

is_light_on = True

school, grade = "ISL", "A2"

print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(school))
print(type(grade))

first_name = input("first name: ")
last_name = input("last name: ")
full_name = first_name + " " + last_name
country = input("country: ")
age = int(input("age: "))


len_first_name = len(first_name)
print(len_first_name)

if len_first_name > len(last_name):
    print("first name bigger")
else:
    print("last name bigger")

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
diff = num_one / num_two
remainder = num_one % num_two
exp = num_one**num_two
floor_division = num_one // num_two

area_of_circle = 3.14 * (30**2)
circum_of_circle = 2 * 3.14 * 30
radius = input("radius: ")
user_area_of_circle = 3.14 * (radius**2)

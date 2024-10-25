def my_function():
    Local_var = 10


    global_var = 20 
    print("Inside the function, global_var =", global_var)


Global_var = 5

my_function()

print("Outside the function, global_var =", Global_var)

#--------------------------------------------------------


x = 10
y = float(x)  # y becomes 10.0
z = complex(x)  # z becomes 10+0j

# Set conversions
my_set = {1, 2, 3}
my_frozen_set = frozenset(my_set)  # my_frozen_set becomes frozenset({1, 2, 3})


#-----------------------------------------------------------
import copy

# Create a list of lists
original_list = [[1, 2], [3, 4]]

# Shallow copy
shallow_copy = original_list[:]

# Deep copy
deep_copy = copy.deepcopy(original_list)

# Modify the original list
original_list[0][0] = 5

# Print the original list, shallow copy, and deep copy
print("Original list:", original_list)
print("Shallow copy:", shallow_copy)
print("Deep copy:", deep_copy)

#-----------------------------------------------------------

my_list = [1, 2, 3]
my_list.append(5)
print(my_list)

my_tuple = (1, 2, 3)
my_tuple.append(5)
print(my_tuple)


#-----------------------------------------------------------
def divide(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

# Test the function
divide(10, 2)  # Output: Result: 5.0
divide(10, 0)  # Output: Error: Cannot divide by zero.

#-------------------------------------------

# Using list comprehension
squares = [x**2 for x in range(1, 6)]

# Using a for loop
squares = []
for x in range(1, 6):
    squares.append(x**2)

print(squares)  # Output: [1, 4, 9, 16, 25]

#-----------------------------------------------------

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
union_set = set1 | set2
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection
intersection_set = set1 & set2
print("Intersection:", intersection_set)  # Output: {3, 4}

# Difference
difference_set = set1 - set2
print("Difference:", difference_set)  # Output: {1, 2}

#----------------------------------------------------------------------

add = lambda x, y: x + y
result = add(3, 4)
print(result)  # Output: 7

#-----------------------------------------------------------
#filter----------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers)) 

#map----------------------------
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers)) 

#reduce------------------------
from functools import reduce

numbers = [1, 2, 3, 4, 5]

product = reduce(lambda x, y: x * y, numbers)
print(product)  

#--------------------------------------------------------------------

def create_and_write_file(filename, data):

    with open(filename, 'w') as file:
        file.write(data)

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

filename = "my_file.txt"
data_to_write = "This is some sample data to write to the file."

create_and_write_file(filename, data_to_write)

data_from_file = read_file(filename)

print("Data from the file:", data_from_file)

#---------------------------------------------------------

def calculate_area_of_circle(radius):
  area = 3.14159 * radius * radius
  return area

radius = float(input("Enter the radius of the circle: "))

area = calculate_area_of_circle(radius)

print("The area of the circle is:", area)

#---------------------------------------------

my_variable = 10
_private_variable = 20
number_123 = 30
camelCaseVariable = 40
snake_case_variable = 50
print(my_variable)
print(_private_variable)
print(number_123)
print(camelCaseVariable)
print(snake_case_variable)

#---------------------------------------------

def calculate_average(grades):
assert len(grades) > 0, "Grades list cannot be empty."

#-------------------------------
a=10
b=5
result = a+b
print(result)

c=10
d=8
result=c-d
print(result)

# AND operation
x = True
y = False
result_and = x and y
print("x AND y:", result_and)  

# OR operation
result_or = x or y
print("x OR y:", result_or) 


#----------------------------------------------------

def fibonacci_generator();
    a,b=0,1
    count=0
    while count<10:
        yeild 
        a,b = b,a+b
        count +=1
        fib_gen= fibonacci_generator()
        for num in fib_gen:
            print(num)
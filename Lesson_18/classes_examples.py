class River:
    # list of all rivers
    all_rivers = []

    def __init__(self, name, length):
        self.name = name
        self.length = length

        # adding current river to the list of all rivers.
        River.all_rivers.append(self)

    def get_info(self):
        print(f'The length of the {self.name} is {self.length} km.')


        # creating class instances/objects.
nile = River('Nile', 39405)
ganga = River('Ganga', 34566)
cavery = River('Cavery', 345)

# print all river names
for river in River.all_rivers:
    print(river.name)

# calling a method.
# self.method()
nile.get_info()
# we could also call the method in a different way.
# class.method(self)
River.get_info(ganga)


########################################################################################

#Right triangle
     A right triangle is a triangle in which one angle is a right angle (90-degree angle).
The side opposite to the right angle is called a hypotenuse and the other two sides are called legs (or catheti).
The Pythagorean theorem holds for right triangles with integer lengths of all sides:
c**2 = a**2 + b**2, where c is the length of the hypotenuse, and a and b are the lengths of the legs.
 
Here's a class RightTriangle with the class constructor. The constructor is missing the area attribute. Calculate the area S according to this formula:
S = (1/2)ab

Three numbers ( input_c, input_a, and input_b) have already been read from the input.
They represent a triangle: the first number is the length of the supposed hypotenuse, the other two are the legs.
If the triangle with these sides is right, create an instance of the class RightTriangle and print its area (with one decimal).
If the triangle is not right, print "Not right".
'''

class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # Calculate the area of the right triangle
        self.area = 0.5 * self.a * self.b


# Read input
input_c, input_a, input_b = [int(x) for x in input().split()]

# Check if the given sides form a right triangle
if input_c**2 == input_a**2 + input_b**2:
    # Create an instance of RightTriangle
    triangle = RightTriangle(input_c, input_a, input_b)
    # Print the area with one decimal place
    print(f"{triangle.area:.1f}")
else:
    print("Not right")


########################################################################################
# Students
   John works at the university. He deals with the information about a lot of students and he decided to create a program that would help him with it.
He devised a system for creating an id for each student: first letter of the name, last name, and then the birth year.
For example, the id for John Smith (b. 1989) would look like JSmith1989.
John needs help finishing the code for the id and then applying it to the students.
Your task is to define an instance attribute student_id in the __init__ method, calculate it, create an object of the class Student with the parameters from the input, and print the value of the id.
Do NOT print the value inside of the __init__ method!

The input format:
Student information: the first line has the name, the second line has the last name, and the third has the birth year.
The output format:
The student_id of the student.

NOTE: the attribute names are case sensitive, so check that the attribute is named exactly student_id. Other names lead to an AttributeError!

'''


class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the student_id here
        self.student_id = f'{name[0]}{last_name}{birth_year}'


# read the inputs
# name = input().strip()
# last_name = input().strip()
# birth_year = input().strip()

name = input()
last_name = input()
birth_year = input()

# creating a student object.
student = Student(name, last_name, birth_year)

# print the student_id
print(student.student_id)
########################################################################################


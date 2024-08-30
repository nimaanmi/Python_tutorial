Classes and Objects

A class is a user-defined blueprint or prototype from which objects are created. Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it to maintain its state. Class instances can also have methods (defined by their class) for modifying their state.

# Attributes are variables that hold the class data, while methods are functions that provide behavior and typically act on the class data.
# In Python, the body of a given class works as a namespace where attributes and methods live. You can only access those attributes and methods through the class or its objects.


Syntax: Class Definition
class ClassName:
    # Statement

Syntax: Object Definition
obj = ClassName()
print(obj.atrr)

The class creates a user-defined data structure, which holds its own data members and member functions, which can be accessed and used by creating an instance of that class. A class is like a blueprint for an object.

Some points on Python class:
Classes are created by keyword class.
Attributes are the variables that belong to a class.
Attributes are always public and can be accessed using the dot (.) operator. Eg.: My class.Myattribute


https://www.youtube.com/watch?v=H2EJuAcrZYU


class Vehicle:
    def moves(self):
        print('Moves along..')


my_car = Vehicle()

my_car.moves()

Output:
Moves along..
########################################################################################

class Vehicle:					# using class to create the class, naming the class with a starting capital letter.
    def moves(self):				# we are defining a method called moves, and pass 'self' in to our method. Self is just referring to itself.
        print('Moves along..')


my_car = Vehicle()				# we are creating an object from the Vehicle class [we are calling the class with parantheses, and assigning it to a variable]

my_car.moves()					# calling moves method [write the object that we created, use a dot after it, select the moves method and after add parentheses to call that method.]


Output:
Moves along..
########################################################################################

Adding parameters:


class Vehicle:
    def __init__(self, make, model):                # in order to pass properties, we'll have create an def __init__() method, which receives self and then pass in properties like make and model to craete objects
        self.make = make                            # we are referring the object 'make' to itself once it's created. So, self just represents the object that is created.
        self.model = model                          # this is just a blue print, we actually create the objects when we set out variable like 'my_car = Vehicle( and we call Vehicle by adding the parentheses after it)'
    def moves(self):
        print('Moves along..')


my_car = Vehicle()

my_car.moves()


# we can't just call the Vehicle(), we'll have to pass in make and model for the car 


class Vehicle:
    def __init__(self, make, model):                # in order to pass properties, we'll have create an def __init__() method, which receives self and then pass in properties like make and model to craete objects
        self.make = make                            # we are referring the object 'make' to itself once it's created. So, self just represents the object that is created.
        self.model = model                          # this is just a blue print, we actually create the objects when we set out variable like 'my_car = Vehicle( and we call Vehicle by adding the parentheses after it)'
    def moves(self):
        print('Moves along..')


my_car = Vehicle('Tesla', 'Model 3')		   # now the object my_car is going to have the values for make and model [Tesla, Model 3].

print(my_car.make)				   # we are retrieving the values from the object my_car that we created above
print(my_car.model)
my_car.moves()

Output:
Tesla
Model 3
Moves along..


# in place of using my_car.make / my_car.model, we'll be using getter which makes it more simple



class Vehicle:
    def __init__(self, make, model):                # in order to pass properties, we'll have create an def __init__() method, which receives self and then pass in properties like make and model to craete objects
        self.make = make                            # we are referring the object 'make' to itself once it's created. So, self just represents the object that is created.
        self.model = model                          # this is just a blue print, we actually create the objects when we set out variable like 'my_car = Vehicle( and we call Vehicle by adding the parentheses after it)'
    def moves(self):
        print('Moves along..')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


my_car = Vehicle('Tesla', 'Model 3')		   # now the object my_car is going to have the values for make and model [Tesla, Model 3].

my_car.get_make_model()
my_car.moves()

Ouptut:
I'm a Tesla Model 3.
Moves along..
########################################################################################

# we can create more objects [cars] from the same class [vehicle].

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Moves along..')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


my_car = Vehicle('Tesla', 'Model 3')

my_car.get_make_model()
my_car.moves()

your_car = Vehicle('Maruti', '3')
your_car.get_make_model()
your_car.moves()

Output:
I'm a Tesla Model 3.
Moves along..
I'm a Maruti 3.
Moves along..
########################################################################################

# Inheritance: 

# Inheritance consists of creating hierarchical relationships between classes, where child classes inherit attributes and methods from their parent class.
# In Python, one class can have multiple parents or, more broadly, ancestors.

# we currently have a very generic class Vehicle.
# We are creating a vehicle but it doesn't say what type of vehicle, we might want to get more specific as we create classes that depend on this Vehicle class.
# we can do that with inheritance.

# so, we'll create a couple of new classes


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Moves away...')

    def get_make_mode(self):
        print(f'I\'m a {self.make} {self.model}.')


my_car = Vehicle('Tesla', '3')
my_car.get_make_mode()
my_car.moves()

your_car = Vehicle('Maruti', '3')
your_car.get_make_mode()
your_car.moves()


class Airplane(Vehicle):
    def moves(self):				# Notice, if we put same method in here, it'll override whatever it would inherit from the Vehicle class.
        print('Flies along...')


class Truck(Vehicle):
    def moves(self):
        print('Rumbles along...')


class GolfCart(Vehicle):			# this means it inherits everything as is, we are not overriding anything [like we did with class Airplane and class Truck with the moves() method]
    pass

# creating subclass objects
airplane = Airplane('Cessna', 'Shyhawk')
truck = Truck('mack', 'Pinnacle')
golfcart = GolfCart('Yamaha', 'GC100')

# calling functions/methods using the newly created subclass objects
airplane.get_make_mode()
airplane.moves()
truck.get_make_mode()
truck.moves()
golfcart.get_make_mode()
golfcart.moves()


Output:
I'm a Tesla 3.
Moves away...
I'm a Maruti 3.
Moves away...
I'm a Cessna Shyhawk.
Flies along...
I'm a mack Pinnacle.
Rumbles along...
I'm a Yamaha GC100.
Moves away...
########################################################################################

# What if we wanted to pass in more information besides the make and model
# Let's say the Airplane also needs the FAA identification number, but you have to have that identification for every airplane.
# So, Let's go inside Airplane class, and create a new initialize method/function and enter new attribute/parameter inside it.


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Moves away...')

    def get_make_mode(self):
        print(f'I\'m a {self.make} {self.model}.')


# creating a class object [the  process is called instantiation]
my_car = Vehicle('Tesla', '3')
my_car.get_make_mode()
my_car.moves()

your_car = Vehicle('Maruti', '3')
your_car.get_make_mode()
your_car.moves()

# creating sub classes:


class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        # self.make = make
        # self.model = model
        # instead of writing self.make = make, self.model = model, we can just use super() function and refer to the Vehicle parent class and use .__init__(make, model)
        super().__init__(make, model)		# here we are just passing in the 2 arrtibutes/parameters that is from the parent Vehicle class.
        self.faa_id = faa_id

    def moves(self):
        print('Flies along...')


class Truck(Vehicle):
    def moves(self):
        print('Rumbles along...')


class GolfCart(Vehicle):
    pass


# creating subclass objects
airplane = Airplane('Cessna', 'Shyhawk', 'N-12345')
truck = Truck('mack', 'Pinnacle')
golfcart = GolfCart('Yamaha', 'GC100')

# calling functions/methods using the newly created subclass objects
airplane.get_make_mode()
airplane.moves()
truck.get_make_mode()
truck.moves()
golfcart.get_make_mode()
golfcart.moves()


Output:
I'm a Tesla 3.
Moves away...
I'm a Maruti 3.
Moves away...
I'm a Cessna Shyhawk.
Flies along...
I'm a mack Pinnacle.
Rumbles along...
I'm a Yamaha GC100.
Moves away...
########################################################################################

# Polymorphism

# It refers to the usage of a single type entity (method, operator, or object) to represent several types in various contexts. Polymorphism is made from 2 words – ‘poly‘ and ‘morphs.’ The word ‘poly’ means ‘many’ and ‘morphs’ means ‘many forms.’ Polymorphism, in a nutshell, means having multiple forms. To put it simply, polymorphism allows us to do the same activity in a variety of ways.

# Polymorphism has the following advantages:
	It is beneficial to reuse the codes.
	The codes are simple to debug.
	A single variable can store multiple data types.

# Polymorphism may be used in one of the following ways in an object-oriented language:

	1. Overloading of operators
	2.Class Polymorphism in Python
	3. Method overriding, also referred to as Run time Polymorphism
	4. Method overloading, also known as Compile time Polymorphism

# creating a class

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Moves away...')

    def get_make_model(self):
        print(f'I\'m a {self.make} {self.model}.')


# making an instance of it by creating a class object.
my_car = Vehicle('Tesla', '3')
my_car.get_make_model()
my_car.moves()

# we can have more than one class object
your_car = Vehicle('Maruti', '300')
your_car.get_make_model()
your_car.moves()

# creating subclasses / class inheritances.


class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print('Flees away...')


class Truck(Vehicle):
    def moves(self):
        print('Rubmles away...')


class Golfcart(Vehicle):
    pass


# creating object instances of the subclasses.
airplane = Airplane('Cessna', 'Skyhawk', 'N-1999')
truck = Truck('Mack', 'Pinnacle')
golfcart = Golfcart('Yamaha', 'K1000')

# calling the attributes/methods
airplane.get_make_model()
airplane.moves()
truck.get_make_model()
truck.moves()
golfcart.get_make_model()
golfcart.moves()
print('\n\n\n')

# polymorphism


for x in (my_car, your_car, airplane, truck, golfcart):
    x.get_make_model()
    x.moves()


Output:
I'm a Tesla 3.
Moves away...
I'm a Maruti 300.
Moves away...
I'm a Cessna Skyhawk.
Flees away...
I'm a Mack Pinnacle.
Rubmles away...
I'm a Yamaha K1000.
Moves away...




I'm a Tesla 3.
Moves away...
I'm a Maruti 300.
Moves away...
I'm a Cessna Skyhawk.
Flees away...
I'm a Mack Pinnacle.
Rubmles away...
I'm a Yamaha K1000.
Moves away...
########################################################################################

# Simple Inheritance
  When you have a class that inherits from a single parent class, then you’re using single-base inheritance or just simple inheritance

# Super class, Parent class, and Base class
  You'll use these interchangeably to refer to the class that you inherit from.

# Child class, derived class, and subclass to refer to classes that inherit from other classes.

# Creating and initializing objects of a given class is a fundamental step in object-oriented programming. This step is often referred to as object construction or instantiation. The tool responsible for running this instantiation process is commonly known as a class constructor.
########################################################################################

# Abstract Classes and Abstract Methods

# An abstract class can be considered a blueprint for other classes.
# It allows you to create a set of methods that must be created within any child classes built from the abstract class.

# A class that contains one or more abstract methods is called an abstract class.
# An abstract method is a method that has a declaration but does not have an implementation.

# We use an abstract class while we are designing large functional units or when we want to provide a common interface for different implementations of a component. 

# Working on Python Abstract classes 
# By default, Python does not provide abstract classes.
# Python comes with a module that provides the base for defining Abstract Base classes(ABC) and that module name is ABC.

# ABC works by decorating methods of the base class as an abstract and then registering concrete classes as implementations of the abstract base.
# A method becomes abstract when decorated with the keyword @abstractmethod.

Example: 
# This code defines an abstract base class called “Polygon” using the ABC (Abstract Base Class) module in Python.
# The “Polygon” class has an abstract method called “noofsides” that needs to be implemented by its subclasses.
# There are four subclasses of “Polygon” defined: “Triangle,” “Pentagon,” “Hexagon,” and “Quadrilateral.”
# Each of these subclasses overrides the “noofsides” method and provides its own implementation by printing the number of sides it has.

# In the driver code, instances of each subclass are created, and the “noofsides” method is called on each instance to display the number of sides specific to that shape.


from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")


class Hexagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")


class Quadrilateral(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")


# Driver code
R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()

Output: 
I have 3 sides
I have 4 sides
I have 5 sides
I have 6 sides
########################################################################################

# Concrete Methods in Abstract Base Classes

# Concrete classes contain only concrete (normal) methods whereas abstract classes may contain both concrete methods and abstract methods.
# The concrete class provides an implementation of abstract methods, the abstract base class can also provide an implementation by invoking the methods via super().
# Let look over the example to invoke the method using super(): 

# Python program invoking a 
# method using super()
from abc import ABC

class R(ABC):
    def rk(self):
        print("Abstract Base Class")

class K(R):
    def rk(self):
        super().rk()
        print("subclass ")

# Driver code
r = K()
r.rk()

Output: 
Abstract Base Class
subclass 


In the above program, we can invoke the methods in abstract classes by using super(). 
########################################################################################

https://www.geeksforgeeks.org/abstract-classes-in-python/


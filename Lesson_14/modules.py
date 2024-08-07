# A module is a file consisting of python codes
# It can define functions, classes, and variables and can also include runnable code. Any Python file can be referenced as a module.

# Modules can be considered small code libraries that are based on related features.
# one example of this is the math module that it contains functions and constant values for use in mathematical equations.

import math

print(math.pi)

Output:
3.141592653589793

# here we are importing the entire module and then we're using dot notation to pull a function or a value from that module.

# Instead of importing the entire module we can pull out what we need 

from math import pi

print(pi)

Output:
3.141592653589793
########################################################################################

# If we don't want to refer to a module by its name, we can create an alias.

import random as rdm

print(rdm.choice('123'))

Output:
2
########################################################################################

How do we know what to use from a module?

There are a few way to find out what's inside a module

1. use dir() function, and inside of it we can pass whatever module we want to

import random as rdm

print(dir(rdm))

Output:
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', '_Sequence', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_fabs', '_floor', '_index', '_inst', '_isfinite', '_lgamma', '_log', '_log2', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'binomialvariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

# The values look jumbled. We can print them line by line to make it look simple.

import random as rdm

for item in dir(rdm):
    print(item)

Output:
BPF
LOG4
NV_MAGICCONST
RECIP_BPF
Random
SG_MAGICCONST
SystemRandom
TWOPI
_ONE
_Sequence
__all__
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__spec__
_accumulate
_acos
_bisect
_ceil
_cos
_e
_exp
_fabs
_floor
_index
_inst
_isfinite
_lgamma
_log
_log2
_os
_pi
_random
_repeat
_sha512
_sin
_sqrt
_test
_test_generator
_urandom
_warn
betavariate
binomialvariate
choice
choices
expovariate
gammavariate
gauss
getrandbits
getstate
lognormvariate
normalvariate
paretovariate
randbytes
randint
random
randrange
sample
seed
setstate
shuffle
triangular
uniform
vonmisesvariate
weibullvariate
########################################################################################

2. 

import random as rdm

rdm.			# after the dot notation it'll bring a list of all the functions/values from that module.
########################################################################################

But neither one of the above two ways actually tell us what any of these constants or different data types or functions are inside of the module.

Let's go to the python doc.

docs.python.org/3/py-modindex.html

Here it'll give an alphabetical list of all the different modules that are available. 
########################################################################################


We are creating a new file called kansas.py

from random import choice

capital = 'Delhi'
bird = 'peachock'
flower = 'lotus'
song = 'Jana Gana Mana'


def randomfunfact():
    funfact = [
        'Delhi is the captial city of free India.',
        'Delhi is very small.',
        'Delhi is also an union territory.',
        'Guess who is from Delhi?'
    ]

    index = choice('0123')
    print(funfact[int(index)])


Now, inside the main file modules.py, we'll import the custom file/module Kansas. And we'll run it inside the main file.

import kansas

print(kansas.flower)
kansas.randomfunfact()

Output:
lotus
Delhi is also an union territory.
########################################################################################

we'll talk about a special value that every module has, and that is the name value.
The current file that we are running is named as modules.py
So, when we print(__name__), it'll print __main__ which is the default name of the current file.

print(__name__)

Output:
__main__

# we could also use __name__ for inbuilt modules/ custom modules.

import math

print(math.__name__)

Output:
math
########################################################################################

Inside of kansas.py
# This function is only going to run/call into action if this is the main file.

from random import choice

capital = 'Delhi'
flower = 'lotus'
bird = 'peacock'
song = 'Jana Gana Mana'


def randomfunfact():
    funfact = [
        'Delhi is the capital of India.',
        'Delhi is beautiful.',
        'Delhi is also an union terriroty.',
        'Guess who is from Delhi?'
    ]

    index = choice('0123')
    print(funfact[int(index)])


if __name__ == '__main__':
    randomfunfact()

Output:
Guess who is from Delhi?
########################################################################################

we'll talk about a special value that every module has, and that is the name value.
Any current file that we are running is by default the main file.
So, when we print(__name__), it'll print __main__ which is the default name of the current file.


To avoid having the custom module/file run a function while importing that custom module, it's always recommended that we call the function inside of that custom module inside of if statement only when
__name__ = '__main__'
If we just call the function inside the custom module without the if statement, when we import the custom module, it'll call the function by default which we do not want.


example: inside the custom module called kansas.py

from random import choice

capital = 'Delhi'
flower = 'lotus'
bird = 'peacock'
song = 'Jana Gana Mana'


def randomfunfact():
    funfact = [
        'Delhi is the capital of India.',
        'Delhi is beautiful.',
        'Delhi is also an union terriroty.',
        'Guess who is from Delhi?'
    ]

    index = choice('0123')
    print(funfact[int(index)])


randomfunfact()

# now when we import this inside the different file, even without calling the function when we run it'll call the function by default.
# inside the modules.py file

import kansas

Output:
Delhi is also an union territorty.
########################################################################################

we can correct this by calling the function inside the custom module inside an if statement with __name__ == '__main__'

# inside the custom module kansas.py

from random import choice

capital = 'Delhi'
flower = 'lotus'
bird = 'peacock'
song = 'Jana Gana Mana'


def randomfunfact():
    funfact = [
        'Delhi is the capital of India.',
        'Delhi is beautiful.',
        'Delhi is also an union terriroty.',
        'Guess who is from Delhi?'
    ]

    index = choice('0123')
    print(funfact[int(index)])


if __name__ == '__main__':
    randomfunfact()

# now we go to modules.py file and import the file and run without calling any function.

import kansas					# save and run the file

Output:
						          # nothing gets called out, because we are not manually calling it but just importing it.
########################################################################################

# if we want to call the function, it' then get called. 
# so, inside the modules.py

import kansas

kansas.randomfunfact()

Output:
Delhi is the capital of India.
########################################################################################


Lesson15

Command Line Arguments		|| https://docs.python.org/3/library/argparse.html#module-argparse

Command line argument is another way of accepting inputs from the users without using the input() function.

https://www.youtube.com/watch?v=88pl8TuuKz0

A Command Line Interface (CLI) is software mechanism you use to interact with your operating system using your keyboard.
How to build professional CLI  applications and parse arguments using the argparse package in python.

Parsing is a technique used to analyze and interpret the syntax of a text or program to extract relevant information.
Essentially, parsing involves breaking down a complex set of data structures or code into smaller, more manageable components that can be analyzed and understood.


argparse package allows us to easily parse command line arguments for our applications in python.

Example in cmd on windows: pwd --help				# It'll show what different arguments are and what different options are.

Usage: pwd [OPTION]...
Print the full filename of the current working directory.

  -L, --logical   use PWD from environment, even if it contains symlinks
  -P, --physical  avoid all symlinks
      --help     display this help and exit
      --version  output version information and exit

If no option is specified, -P is assumed.
########################################################################################

# The argparse module’s support for command-line interfaces is built around an instance of argparse.ArgumentParser. It is a container for argument specifications and has options that apply to the parser as whole:

parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

# The ArgumentParser.add_argument() method attaches individual argument specifications to the parser. It supports positional arguments, options that accept values, and on/off flags:

parser.add_argument('filename')           # positional argument
parser.add_argument('-c', '--count')      # option that takes a value
parser.add_argument('-v', '--verbose',
                    action='store_true')  # on/off flag

The ArgumentParser.parse_args() method runs the parser and places the extracted data in a argparse.Namespace object:

args = parser.parse_args()
print(args.filename, args.count, args.verbose)
########################################################################################

# How to add our own options and arguments to our command line application: 

we are creating a new file called hello_person.py
we are going to have different options on how to display the result and what to do with the result.


# importing the argparse module
import argparse

# calling the function and assisgning the instance.
parser = argparse.ArgumentParser(description='Provides a personal greeting.')

# adding in the arguments
parser.add_argument(
    '-n', '--name', metavar='name',
    required=True, help='The name of the person to greet.'
    # '-n' is abbrivated for '--name', here we could use any other name in place '--name', like '--tomato'
    # metavar='name' is just the display name if we get a message that refers back to this argument.
    # help='The name of the person to greet.' here we can provide the help message and write anything.
)

# now calling in another function onto the as the last step || parser.parse_args() here we'll pass in the arguments

args = parser.parse_args()
msg = print(f'Hello {args.name}!')

# Time to run,, but we cannot use the run/play button like we do it for other files, we'll have to use ther CLI/terminal.
# Note: Make sure we are in the right directory in the terminal to run the file, if not it'll  show 'no such file' message.
# open the terminal and type in: py hello_person.py    
# But if we press enter now, it'll show error as required=True was defined.

Output: 
usage: hello_person.py [-h] -n name
hello_person.py: error: the following arguments are required: -n/--name

# To overcome we'll have to pass in -n or --name and enter a name,  but before that let's check with -h (help) option.

Terminal: py hello_person.py -h

Output: 
usage: hello_person.py [-h] -n name

Provides a personal greeting.

options:
  -h, --help            show this help message and exit
  -n name, --name name  The name of the person to greet.

# So, we can see that it does displays the option. Now, we can enter the -n / --name and enter our name.

Terminal: py hello_person.py -n Tom

Output: 
Hello Tom!
########################################################################################

Now we can wrap this code into a function, even the import [something new]


def hello(lang, name):
    greetings = {
        'English': 'Hello',
        'Spanish': 'Hola',
        'German': 'Hallo'
    }
    msg = f'{greetings[lang]} {name}!'
    print(msg)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='This is a description.')
    parser.add_argument(
        '-n', '--name', metavar='name',
        required=True, help='This is a help message.'
    )
    parser.add_argument(
        '-l', '--lang', metavar='language',
        required=True, choices=['English', 'Spanish', 'German'],
        help='This is a second message.'
    )
    args = parser.parse_args()
    hello(args.lang, args.name)

Terminal:  py rps7.py -n 'Dave' -l 'German'
Hallo Dave!
########################################################################################


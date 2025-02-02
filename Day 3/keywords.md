# Keywords in Python:

Keywords are reserved words in Python that have predefined meanings and cannot be used as variable names or identifiers. These words are used to define the structure and logic of the program. They are an integral part of the Python language and are case-sensitive, which means you must use them exactly as specified.

Here are some important Python keywords:

1. **and**: It is a logical operator that returns `True` if both operands are true.

2. **or**: It is a logical operator that returns `True` if at least one of the operands is true.

3. **not**: It is a logical operator that returns the opposite of the operand's truth value.

4. **if**: It is used to start a conditional statement and is followed by a condition that determines whether the code block is executed.

5. **else**: It is used in conjunction with `if` to define an alternative code block to execute when the `if` condition is `False`.

6. **elif**: Short for "else if," it is used to check additional conditions after an `if` statement and is used in combination with `if` and `else`.

7. **while**: It is used to create a loop that repeatedly executes a block of code as long as a specified condition is true.

8. **for**: It is used to create a loop that iterates over a sequence (such as a list, tuple, or string) and executes a block of code for each item in the sequence.

9. **in**: Used with `for`, it checks if a value is present in a sequence.

10. **try**: It is the beginning of a block of code that is subject to exception handling. It is followed by `except` to catch and handle exceptions.

11. **except**: Used with `try`, it defines a block of code to execute when an exception is raised in the corresponding `try` block.

12. **finally**: Used with `try`, it defines a block of code that is always executed, whether an exception is raised or not.

13. **def**: It is used to define a function in Python.

14. **return**: It is used within a function to specify the value that the function should return.

15. **class**: It is used to define a class, which is a blueprint for creating objects in object-oriented programming.

16. **import**: It is used to import modules or libraries to access their functions, classes, or variables.

17. **from**: Used with `import` to specify which specific components from a module should be imported.

18. **as**: Used with `import` to create an alias for a module, making it easier to reference in the code.

19. **True**: It represents a boolean value for "true."

20. **False**: It represents a boolean value for "false."

21. **None**: It represents a special null value or absence of value.

22. **is**: It is used for identity comparison, checking if two variables refer to the same object in memory.

23. **lambda**: It is used to create small, anonymous functions (lambda functions).

24. **with**: It is used for context management, ensuring that certain operations are performed before and after a block of code.

25. **global**: It is used to declare a global variable within a function's scope.

26. **nonlocal**: It is used to declare a variable as nonlocal, which allows modifying a variable in an enclosing (but non-global) scope.



---------------------------

My personal note on few of the keywords:

Try and Except:
The try and except keywords are used to handle exceptions in Python. The try block contains the code that might raise an exception, and the except block contains the code that will be executed if an exception occurs.

For example:

try:
    result = 10 / 0
except ZeroDivisionError:
    result = "Cannot divide by zero"
print(result)
In this example, the try block attempts to divide 10 by 0, which will raise a ZeroDivisionError. The except block catches this exception and assigns the string "Cannot divide by zero" to the result variable. The result variable is then printed, which will output "Cannot divide by zero".

----------------
Finally:
The finally keyword is used in conjunction with try and except to ensure that the file is closed regardless of whether an exception occurred or not

For example:
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    file.close()

In this example, the try block attempts to open a file named "example.txt" in read mode. If the file is not found, a FileNotFoundError exception is raised. The except block catches this exception and prints "File not found". The finally block ensures that the file is closed, regardless of whether an exception occurred or not.

----------------

Class:
The class keyword is used to define a class in Python. A class is a blueprint for creating objects.

For example:

class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Buddy")
print(my_dog.bark())

In this example, the class keyword is used to define a class named Dog. The __init__ method is a special method that is called when an object is created from the class. The self parameter refers to the object itself. The bark method is a regular method that returns a string. An object named my_dog is created from the Dog class, and the bark method is called on it, which returns "Buddy says Woof!".

----------------

Difference between class and def:
The class keyword is used to define a class in Python, while the def keyword is used to define a function.

A class is a blueprint for creating objects, while a function is a block of code that can be called to perform a specific task.

-----------------

None:
The None keyword is used to represent the absence of a value. It is often used as a default value for variables or function return values.

def no_return_function():
    pass

result = no_return_function()
print(result)  # Output: None

In this example, the no_return_function does not return a value, so the result variable is assigned the value None.

----------------

Is:
The is keyword is used to check if two variables refer to the same object in memory. It is often used to compare objects for equality.

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)  # False
print(a is c)  # True

In this example, the a and b variables are lists with the same values, but they are not the same object in memory. The c variable is assigned the same list as a, so it is the same object in memory.

----------------

Lambda:
The lambda keyword is used to define an anonymous function in Python. It is often used for short, simple functions that can be defined in a single line.

add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

In this example, the lambda function adds two numbers and returns the result. The add variable is assigned the lambda function, which is then called with the arguments 2 and 3.

----------------
Difference between lambda and def:
The lambda keyword is used to define an anonymous function in Python, while the def keyword is used to define a regular function.

----------------

with:
The with keyword is used for context management in Python. It is often used to ensure that certain operations are performed before and after a block of code.

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

In this example, the with keyword is used to open a file named "example.txt" in read mode. The file is automatically closed after the block of code is executed, regardless of whether an exception occurs or not.

----------------

Difference between finally and with:
The finally keyword is used in conjunction with try and except to ensure that certain operations are performed regardless of whether an exception occurs or not. The with keyword is used for context management in Python, and it is often used to ensure that certain operations are performed before and after a block of code.

----------------

global:
The global keyword is used to declare a variable as a global variable. It is often used when a variable needs to be accessed from within a function that is not the global scope.
Also, the global keyword is used to modify the value of a global variable within a function.

x = 10

def modify_global():
    global x
    x = 20

modify_global()
print(x)  # Output: 20

----------------------
nonlocal:
The nonlocal keyword is used to declare a variable as a nonlocal variable. It is often used when a variable needs to be accessed from within a nested function that is not the global scope.

def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    print("Before inner:", x)  # Output: 10
    inner()
    print("After inner:", x)   # Output: 20

outer()

Here, nonlocal x in the inner function allows it to modify the x variable in the outer function's scope.

----------------------
Difference between global and nonlocal:

Usage Context
Global
Can be used in any function, regardless of nesting level.
Refers to variables at the module level (top-level of a script or module).
Nonlocal
Can only be used inside nested functions.
Refers to variables in the nearest enclosing scope, excluding the global scope.



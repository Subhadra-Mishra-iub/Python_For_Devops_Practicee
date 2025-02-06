os.listdir()

--------------------------
Exceptional handling: (User defined exceptions)
Exception handling is a control flow mechanism that allows you to handle errors and exceptions in your code.

Example:
try:
    # Code that may raise an exception
    files = os.listdir(folder)
except FileNotFoundError:
    print("Please provide a valid folder name, looks like this folder doesn't exist." + folder)
    break

--------------------------

If we have one more except condition.

try:
    # Code that may raise an exception
    files = os.listdir(folder)
except FileNotFoundError:
    print("Please provide a valid folder name, looks like this folder doesn't exist." + folder)
    break
except PermissionError:
    print("You don't have permission to access this folder." + folder)
    break


--------------------------



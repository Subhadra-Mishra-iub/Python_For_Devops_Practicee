import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

try:
    div = num1/num2
except ZeroDivisionError:
    print("Cannot divide by zero")
    
    
#Note:Use input() when you need real-time user interaction within the program.
#Use sys.argv[] when you want to pass arguments to the script before it starts, 
#especially for automation or when processing multiple files
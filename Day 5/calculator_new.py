import sys

def add(num1, num2):
    add = num1 + num2
    return add

def sub(num1, num2):
    s = num1 - num2
    return s

def mul(num1, num2):
    m = num1 * num2
    return m

#Want to get the values from the user
num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == 'add':
    output = add(num1, num2)
    print(output)
elif operation == 'sub':
    output = sub(num1, num2)
    print(output)
elif operation == 'mul':
    output = mul(num1, num2)
    print(output)


#command to run the file is: (Example)
#Go to the folder Day 5, then run the following command
#python calculator_new.py 10 add 20
# num1 = 10
# num2 = 5
#giving the values of num1 and num2

#function approach

def addition(num1, num2):
    #why open close bracket?
    #Because function definition is a block of code that can contain multiple lines of code.
    #It allows us to encapsulate a set of related statements in a single unit.
    #When we call the function, it executes all the statements inside it.
    #The open and close brackets ensure that the function body is defined correctly.
    #The open bracket indicates the start of the function body, and the close bracket indicates the end of the function body.
    add = num1 + num2
    # print(add)
    return add  # returning the result of addition
    
def sub(num1, num2):
    s = num1 - num2
    # print(s)
    return s

def mul(num1, num2):
    m = num1 * num2
    # print(m)
    return m
    
#without these there wont be any output like say i dont write mul() then i wont be able to see the multiplication output
addition(5, 10)
sub(5, 10)
mul(5, 10)
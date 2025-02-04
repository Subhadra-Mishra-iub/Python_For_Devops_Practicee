import sys

type = sys.argv[1]

if type == "t2.micro":
    print("Oka, we will create the instance for you")
else:
    print("your input is not t2.micro, so we can't create")
    
    
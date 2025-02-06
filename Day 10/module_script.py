def some_function():
    return "This is a function from module_script"

print("This is the module_script file")

if __name__ == "__main__":
    print("module_script.py is being run directly")
    print(some_function())
else:
    print("module_script.py is being imported as a module")
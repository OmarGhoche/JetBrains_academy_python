# Calculators are the oldest programs humans have made! So I didn't want to re-invent it!
# For this reason I simply used python built-in functions `eval()` and `exec()` to handle
# the already very good implemented arithmetic operations, with some minor modifications and limitations!


import re  # to look for numbers in variable names (invalid variable)
from sys import exit  # to exit the infinite while loop!


# From StackOverFlow
# Function that returns True if variable has digit `\d` in the name
def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))

while 1:  # AKA while True
    nums = ""
    while nums == "":
        # while nums is empty, nothing will happen
        nums = input().strip()
    
    # First checks for `keywords`
    if nums == "/exit":
        print("Bye!")
        exit(0)
    if nums == "/help":
        print("This Program calculates the SUM, the SUB, the MULT, the DIV and the POW of numbers or variables")
        continue
    
    # when the user wants to add a variable
    if "=" in nums:
        # if the variable name, before the `=` has numbers,
        # then it is not a valid variable name
        if hasNumbers(nums.split("=")[0]):
            print("Invalid identifier")
            continue
        try:
            # by using `exec()` built-in function, a string is treated as a Python command
            # than a variable is created if an error is raised, then `except` handles it!
            exec(nums)
            continue
        except:
            print("Invalid assignment")
            continue
    
    # Since `^` should be interpreted as `**` (power):
    nums = nums.replace("^", "**")
    # and `//` (integer division) is not supported:
    if "//" in nums:
        print("Invalid assignment")
        continue
    
    # Finally, at the end of the algorythm calculations are performed (+, -, *, / and ^)
    # using `eval()` built-in function, if variables are declared, then simply,
    # prints the result to the user, otherwise, except handles the errors
    try:
        print(int(eval(nums)))  # because it only accepts integer results!!
    except NameError:
        print("Unknown variable")
    except SyntaxError:
        if nums.startswith('/'):
            print("Unknown command")
        else:
            print("Invalid expression")
            

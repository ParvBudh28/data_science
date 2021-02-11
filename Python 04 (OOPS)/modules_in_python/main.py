# import calculator

# Filtered import way
# we can specify what all do we need from this module
# from calculator   # imports everything

# from calculator import add      # filtered way

# in the above way we don't have a variable called calculator we can directly
# use add function inside this file because calculator module has been
# destructured
# from calculator import *  # here also we don't need to refer by calculator.add()


# to make code more readable
# from calculator import(
#     add,
#     sub,
#     mul,
#     div
# )

#  Aliases
# import calculator as lib

# from calculator import(
#     add as addition,
#     sub as subtraction
# )

# print(globals())
# used to get all the global variables

# print(add(2,2))

# a = calculator.A()
# print(type(a))


# Modules is a file in python
# Package is collection of modules
#  to specify that a folder is a package we need to create a __init__.py file

# ------------------------------# ------------------------------# ------------------------------
# PACKAGES

# use of __init__.py file

from math.simple import(
    add
)

print(add(1,2))
# print(complex.cube(3))

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    return a//b

# will be printed even if someone imports this file
# print("hello")

print(__name__)

# how to tackle this problem
if __name__=='__main__':
    print("hello")

# if we use the above conditional check then we can specify what all to run when we run this file
# as a script by itself

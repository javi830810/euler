import random

def rand4():
    return random.randint(0,4)

def rand7():
    return (rand4() + rand4())%7


print rand7()

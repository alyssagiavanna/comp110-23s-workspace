"""Practice importing from other modules"""

from lessons import my_functions

if __name__ == "__main__":
    print("Howdy!")

print(my_functions.addition(1,2))
print(my_functions.my_variable)

from lessons.my_functions import addition

print(addition(1,2))
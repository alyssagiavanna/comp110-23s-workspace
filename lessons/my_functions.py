"""Things I'll be importoing"""

def addition(x: int, y: int):
    return x + y

my_variable: str = "hello"

if __name__  == "__main__":
    print("This should only print when running my_functions")
else:
    print("my_functions is being imported")
"""
Functional Programming functions treated as values just like any other variable




"""


def announce(f):

    def wrapper():
        print("About to run the function")
        f()
        print("Done with function")

    return wrapper

@announce
def hello():
    print("hello world!")


hello()
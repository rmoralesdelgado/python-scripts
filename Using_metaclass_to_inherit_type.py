# Script to understand the use of a meta-class to set the type of inheriting classes.
# Created by Raul Morales Delgado
# Based on https://stackoverflow.com/a/48846044/11905552


class MyMetaClass(type):  # 'type' is necessary
    def __repr__(cls):
        return "Meta-class that sets 'type' to inherit."


class MyRegularClass(object, metaclass=MyMetaClass):  # 'object' is redundant
    def __init__(self, num, denom):
        self.numerator = num
        self.denominator = denom

    def regular_method(self):
        return self.numerator / float(self.denominator)

    def __repr__(self):  # __repr__ is more for developer use
        return "Regular class __repr__ method"

    def __str__(self):  # __str__ is for end-user use
        return "Regular class __str__ method"


def example():
    #  Creating an instance of MyRegularClass:
    f = MyRegularClass(1, 3)
    #  Printing different attributes:
    print(type(f))  # Prints meta-class type
    print(f)  # Prints __str__ method
    print(repr(f))  # Prints __repr__ method
    print(f.numerator)  # Prints class attribute 'numerator'
    print(f.regular_method())  # Prints the return of 'regular_method'
    print(type(f.regular_method()))  # Prints type of the return


example()

# if __name__ == "__main__":
#    example()

# Script that creates a recursive function to get an interactive input that
# will not be satisfied until assertion is True.
# Created by Raul Morales Delgado.


def recursive_input(message, req_answer):
    try:
        my_input = input(message)
        assert my_input == req_answer, "My assertion error."
    except AssertionError:
        print("There was an exception!")
        recursive_input(message, req_answer)
    else:
        print("Input accepted")
    finally:
        print("Thank you")
        return my_input

recursive_input('Hello: (Answer must be "World") ', 'World')

# if __name__ == "__main__":
#    recursive_input()
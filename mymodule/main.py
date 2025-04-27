# main.py
"""
Main entry point for the application.
"""

from mymodule.utils import greet_user

def main(name):
    """
    Main function that runs the application.
    
    Parameters:
        name (str): Name of the user to greet.
    """
    greeting = greet_user(name)
    print(greeting)

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    main(user_name)
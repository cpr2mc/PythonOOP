#Chris learning Python OOP exercises
'''
Using the classmethod class (do it in the standard way) implement a class name Person
that has a class method named show_details() which displays the following text to the console:
'Running from Person class.'
Try to pass the class name using the appropriate attribute of the Person class. In response,
call the show_details() class method.
'''
class Person:
    
    def show_details(cls):
        print(f'Running from {cls.__name__} class.')

    show_details = classmethod(show_details)

Person.show_details()
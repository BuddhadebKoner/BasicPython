class Animal:  # parent
    # attribute and method of the parent class
    def __init__(self, name):
        self.name = name


class Dog(Animal):  # child
    def display(self):
        print("My name is", self.name)


# Creating an instance of Dog
my_dog = Dog("Buddy")
my_dog.display()  # Output: My name is Buddy

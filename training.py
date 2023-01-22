# Hello Training print out
print('Let the training begin')

# Write a class with a constructor and a method
class Training:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_info(self):
        print(self.name)
        print(self.age)

# Call the method print_name and print the name 'Thomas'
training = Training('Thomas', 9)
training.print_info()
print("The name of the person is " + str(training.name) + " and the person is " + str(training.age) + " years old.")
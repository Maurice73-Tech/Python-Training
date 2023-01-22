# Hello Training print out
print('Let the training begin')

# Write a class with a constructor and a method
class Training:
    def __init__(self, name):
        self.name = name
    def print_name(self):
        print(self.name)

# Call the method print_name and print the name 'Thomas'
training = Training('Thomas')
training.print_name()
# variables
# number = 5
# string = "John"
# boolean = False
# none = None
# print(number, string, boolean, none)




# assign multiple
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)


# dictionary = {
#     "name" : "John", 
#     "age" : 36
# }
# print(dictionary.get('name'))
# print(dictionary["age"])


### condition
# a = 200
# b = 33
# if b or a:
#     print("b is greater than a")
# else:
#   print("b is not greater than a")


### array
#thislist = ["apple", "banana", "cherry"]
# for i in range(0, len(thislist)):
#   print(thislist[i])

# for i, value in enumerate(thislist):
#     print(i, value)

# modified = [f"{i} {x}" for i, x in enumerate(thislist)]
# print(modified)


### function
# def my_function(param1):
#   print(f"Hello from a function {param1}")

# my_function('test')


# class Employee:
#     pass

# emp = Employee()
# emp.first_name = 'John'
# print(emp.first_name)


class Employee:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)


# emp = Employee('John')
# emp.print_name()


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name)
    
    def set_postion(self, value):
        self.position = value 

    def print_name(self):
        print(f"Name: {self.name} Position: {self.position}")

manager = Manager('Anna')
manager.set_postion('HR')
manager.print_name()
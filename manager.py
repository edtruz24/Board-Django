# from employee import Employee
import employee

class Manager(employee.Employee):
    def __init__(self, name):
        super().__init__(name)
    
    def set_postion(self, value):
        self.position = value 

    def print_name(self):
        print(self.position)

manager = Manager('Anna')
manager.set_postion('HR')
manager.print_name()
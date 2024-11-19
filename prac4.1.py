# Employee Record System
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        
    def display_info(self):
        print(f"Employee: {self.name}, Position: {self.position}, Salary: {self.salary}")

# Example usage
emp1 = Employee("John", "Manager", 50000)
emp2 = Employee("Sarah", "Developer", 60000)
emp1.display_info()
emp2.display_info()
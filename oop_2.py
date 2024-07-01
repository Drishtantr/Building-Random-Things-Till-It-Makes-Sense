class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_sal(self, increment):
        self.inc = increment
        self.salary = self.salary + increment

# Inheritance
class Tester(Employee):
    pass

class Dev(Employee):
    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework
    def increase_sal(self, increment, bonus = 0):
        # Getting parent's method
        super().increase_sal(increment)
        self.salary = self.salary + bonus
    
e1 = Tester("John", 23, 5000)
e2 = Dev("Ram", 23, 5000, "React")

e2.increase_sal(1000, 500)
print(e2.salary)

print(e2.framework)


# Polymorhpism
# print(isinstance(e1, Tester))
# print(issubclass(Employee, object))

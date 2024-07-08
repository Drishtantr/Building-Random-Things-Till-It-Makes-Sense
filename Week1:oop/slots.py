class Employee:
    __slots__ = ('name', 'age', 'salary')
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_sal(self, increment):
        self.inc = increment
        self.salary = self.salary + increment

class Developer(Employee):
    __slots__ = ('framework')
    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework
    
e2 = Developer("Ram", 23, 5000, "React")
# __dict__ doesn't work here
print(e2.__slots__)
print(e2.framework)

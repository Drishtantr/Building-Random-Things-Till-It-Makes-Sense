class Employee:
    pass
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.inc = 0
        self.newAge = age
        self.salary = salary
        self.ann_salary = None
        
    def increase_age(self, increment):
        self.inc = increment
        self.newAge = self.age + increment
    
    @property
    def salary(self):
        return self._salary
        
    @salary.setter
    def salary(self, salary):
        if (salary < 1000):
            raise ValueError('Too Little Salary')
        self._salary = salary

    def __str__(self):
        return (f"{self.name}'s salary is {self.salary}")
    
e1 = Employee("John", 23, 'Dev', 5000)
print(e1)


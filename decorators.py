class Employee:
    min_sal = 1000
    
    @classmethod
    def update_min_wage(cls, newVal):
        cls.min_sal = newVal
        
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age + Employee.min_sal
        self.position = position

    @property
    def salary(self):
        return self._salary
        
    @salary.setter
    def salary(self, salary):
        if (salary < Employee.min_sal):
            raise ValueError('Too Little Salary')
        self._salary = salary
    
e1 = Employee("John", 23, 'Dev', 5000)

print(e1.min_sal)
Employee.update_min_wage(5000)
print(Employee.min_sal)


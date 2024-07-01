class Employee:
    def __init__(self, name, age, position, project):
        self.name = name
        self.age = age
        self.position = position
        self.project = project
    
    def __str__(self):
        return (f"{self.project.title}, {self.project.tech}")
        
class Project:
    def __init__(self, title, tech):
        self.title = title
        self.tech = tech
    
    def __str__(self):
        return (f"{self.title} {self.tech}")
    

p1 = Project("Real Estate", "React")
e1 = Employee("John", 27, "Dev", p1)

print(e1)
print(p1)



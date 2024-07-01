from dataclasses import dataclass

@dataclass(slots=True)
class Project:
    title: str
    tech: str
    
@dataclass(slots=True)
class Employee:
    name: str
    age: int
    position: str
    project: Project
    
    def __str__(self):
        return f"{self.project.title}, {self.project.tech}"

p1 = Project("Apple", "React")
e1 = Employee("John", 27, 'Dev', p1)
print(e1)

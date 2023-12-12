class student:
    def __init__(self, name="John", age=20, cgpa=3.5):
        self.name = name
        self.age = age
        self.cgpa = cgpa

    @property
    def getName(self):
        return self.name
    
    @getName.setter
    def setName(self, newName):
        print("Setting name...")
        self.name = newName

    @property
    def getAge(self):
        return self.age
    
    @getAge.setter
    def setAge(self, newAge):
        print("Setting age...")
        self.age = newAge

    @property
    def getCgpa(self):
        return self.cgpa
    
    @getCgpa.setter
    def setCgpa(self, newCgpa):
        print("Setting cgpa...")
        self.cgpa = newCgpa

    def doSomething(self):
        print("Doing something...")

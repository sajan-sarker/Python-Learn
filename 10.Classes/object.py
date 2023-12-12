from student import student

stu = student()
print(stu.getName)
print(stu.getAge)
print(stu.getCgpa)

name= input("Enter new name: ")
stu.setName = name
age = int(input("Enter new age: "))
stu.setAge = age
cgpa = float(input("Enter new cgpa: "))
stu.setCgpa = cgpa

print(stu.getName)
print(stu.getAge)
print(stu.getCgpa)

stu.doSomething()
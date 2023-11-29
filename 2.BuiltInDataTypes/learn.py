student = ["Matteu", "John", "Mary", "Peter"]

print(student[0])
print(student[2])
print("All: "+str(student[0])+" "+str(student[1])+" "+str(student[2])+" "+str(student[3]))
print("Till 0 "+str(student[:0]))
print("Till 1 "+str(student[:1]))
print("Till 2 "+str(student[:2]))
print("Till 3 "+str(student[:3]))
print("Till 4 "+str(student[:4]))

print("From 0 "+str(student[0:]))
print("From 1 "+str(student[1:]))
print("From 2 "+str(student[2:]))
print("From 3 "+str(student[3:]))

print("From 0 to 2 "+str(student[0:2]))

student.append("Peter")
print(student[4])
print(student)
student.pop()
student.pop()
print(student)
student.insert(1, "Rachel")
print(student)
studentID= [1,2,3,4,5]
print(studentID)
studentWithId= dict(zip(studentID, student))
print(studentWithId)

print(studentWithId[2])


presidents = ("Obama", "Trump", "Bush")

print("President 0: "+str(presidents[0]))

myList = [1920, 1890, 1990, 2000, 1890, 2010]


a= "abcd"
print(len(a))
print(str(len(presidents[0])))

presidentWithYear= dict(zip(myList, presidents))
print(presidentWithYear)
print(presidentWithYear[1990])
print(myList)
myListSet= set(myList)
print(myListSet)
myListSet.add(3500)
print(myListSet)

print("Max Year "+ str(max(myListSet)))
print("Min Year "+ str(min(myListSet)))
print("President of Min Year "+ str(presidentWithYear[min(myListSet)]))
print(myListSet)
myListSet.remove(3500)
print(myListSet)
myList2= [1238, 1990, 1538]
myList2Set= set(myList2)
print(myListSet |myList2Set)
print(myListSet & myList2Set)
print(myListSet - myList2Set)
print(myListSet ^ myList2Set)


StudentDictionary= [{"Name": "John", "Age": 23, "CGPA": 3.5, "Dept":"CSE"},{"Name": "Snow", "Age": 23, "CGPA": 3.5, "Dept":"CSE"}]
print(StudentDictionary) 
print(StudentDictionary[0])
print(StudentDictionary[0]["Name"])
print(StudentDictionary[1].get("Name"))
StudentDictionary[1].pop("CGPA")
print(StudentDictionary[1])

studentDic= {111: "John", 222: "Matheu", 333: "Snow"}
print(studentDic)
print(studentDic[111])
studentCourses= {1 : 'CSE110', 2: ["CSE111", "MAT111"], 3: {"CSE425": "AI", "CSE372": "DBMS"}}
print(studentCourses)
print(studentCourses[2])
studentWithCourse= dict(zip(studentDic, studentCourses))
print(studentWithCourse)
print(studentCourses[2][1])
print(studentCourses[2][1])

print(studentCourses[3]["CSE425"])
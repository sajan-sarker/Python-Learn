try:
    print(1/0)
except:
    print("Error")

studentDic= {111: "John", 222: "Matheu"}       
try:
    print(studentDic[333])
except:
    print("Given Id is not found in the dictionary")

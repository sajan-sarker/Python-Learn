name = str(input("Enter your name: "))
city = str(input("Enter your city: "))

print("Hello, " + name + " from " + city + "!")

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[:5])

print('This is ',name,'\'s code')
print("This is {}\'s code".format(name[:5]))

print("This is {} from {}.".format(name, city))

print("h" in name)

name1 = name.split()
print(name1)
print("This is {}\'s code".format(name1[0]))
name2 = ' '.join(name1)
print(name2)

string = "     test    "
string1 = string.strip()
print(string1)
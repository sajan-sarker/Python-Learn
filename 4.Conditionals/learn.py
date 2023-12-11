boolean1 = 3 == 4
print("Boolean 1:"+ str(boolean1))

boolean2 = 3 != 4
print("Boolean 2: "+ str(boolean2))

boolean3 = 6 > 7
print("Boolean 3: "+ str(boolean3))

boolean4 = 8 >= 6
print("Boolean 4: "+ str(boolean4))

age = 25
money = 500
boolean5 = age > 18 and money < 100
print("Boolean 5: "+ str(boolean5))

boolean6 = age > 18 or money < 100
print("Boolean 6: "+ str(boolean6))

age1 = 24
tokenLimit = 10000
if(age1 > 18 and tokenLimit > 1000):
    print("You are eligible to buy tokens")
else: 
    print("Your are not eligiable for buying tokens")
age2 = 17
if(age2 > 18 and tokenLimit > 15000):
    print("You are eligible to buy tokens")
elif(age2 > 16 & age < 18):
    print("You are eligible to buy tokens as a child")
else: 
    print("Your are not eligiable for buying tokens")

a = 15
b = 10
c = 7
if(a > b):
    if(a > c):
        print("a is larger.")
    else:
        print("c is larger.")   
else:
    if(b > c):
        print("b is larger.")
    else:
        print("c is larger.")
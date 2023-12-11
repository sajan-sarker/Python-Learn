vegetables= ["carrot", "lettuce", "onion", "radish", "potato" , "tomatto"]

x = (len(vegetables))

buyVegatables = "tomatto"

for i in vegetables:
    if( buyVegatables == i):
        print(str(i) + " is available")
        break
    else:
        print(str(i) + " is not available")
print("end of loop")

for i in vegetables:
    if( buyVegatables == i):
        print(str(i) + " is available")
        continue

     
for x in range (1 , 10):
    print(x)
print("end of loop")

j = 1
while j <= 5:
    print(j)
    j+=1

for k in range (1 , 10):
    print(k)
    if k == 5:
        break
print("end")
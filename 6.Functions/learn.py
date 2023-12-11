def putTyersOnCar():
    screws = 0
    tyres = 0
    for k in range (1, 5):
        print("Putting tyres on....")
        for l in range (1, 5):
            print("putting the screws on")
            screws+=1
        if screws == 4:
            print("Tyres properly put on")
            screws= 0
            tyres+=1
        if tyres == 4:
            print("Car has Been properly Assemble")

putTyersOnCar()

def adder(a,b):
    c= a+b
    return c


d = adder(5,6)
print(d)
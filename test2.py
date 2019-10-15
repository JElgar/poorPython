inputstring = input("Please type in a number: " )
inputNumber = int(inputstring)

def f(x): 
    raf = x**2
    return raf

print(f(2))

a = f(2)
b = f(3)

print("Hello")

print((a + b)*inputNumber)

for x in range (1, 100):
    if(x < 20): 
        print("The number " + str(x) + " is small")
    if(x >= 20):
        print("The number " + str(x) + " is big")
    print (x)

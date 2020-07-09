n = int(input("Number: "))

if n > 0:
    print("n is positive")
elif  n < 0:
    print("n is negative")
else:
    print("n is zero")
    
loops in python
arr = range(12)
for i in arr:
    print(i)

names = ["Ira", "Danil", "Milandra", "Kolya", "Masha"]
for name in names:
    print(name)

name = "Danil-pidril"

for character in name:
    print(character)

# pythondictionary
houses ={"Irina":"Moscow", "Danil":"Krasnodar", "Mila": "Kurganinsk"}
houses["Ira"] = "Kurganinsk" #добавляем новое знач
print(houses["Ira"])

функции

def square(x): 
    return x * x

for i in range(10):
    print(f"The square of {i} is {square(i)}")

классы в питоне
class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2
p = Point(2, 9)      
print(p.x)
print(p.y) 

# name = "Harry"
# print(name[1])

# names = ["Harry", "Irina", "Pierre"]
# print(names[1])

# coordinateX = 10.0
# coordinateY = 20.0

# coordinate = (10.0, 20.0)

# list
# names = ["Harry", "Irina", "Pierre", "Uma"]
# names.append("Rim")
# names.sort()
# print(names)

# create set

s = set()

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(6)
s.add(7)
s.add(1)
s.remove(2)

print(f"The set has {len(s)} elements")


    #принимает функцию и возвращает другую
def announce(f):
    def wrapper():
        print("About to run a function")
        f()
        print("Done with the function")
    return wrapper
@announce
def hello():
    print("Hello, Ira")

hello()
people = [
    {"name":"Irina", "house":"Kurganinks" },
    {"name":"Peter", "house":"St-Peter" },
    {"name":"Yur", "house":"Moscow" }
]
# def f(person):
#     return person["house"]
#     lambda = этой функции


people.sort(key=lambda person: person["name"])
print(people)

import sys
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input")
    sys.exit(1)
try:
    result = x / y 
except ZeroDivisionError:
    print("Error: Cannot divide by 0")
    sys.exit(1)

print (f"The result is {result}")
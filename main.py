# identetation
if 5 > 2:
    print("five is greater than two")

# varibales
userage = 100
username = "jason kibet"
print(userage)
print(username)

# mysofvariabal
myVariableName = "Camel Case jason"
MyVariableName = "Pascal Case jason"
my_variable_name = "Snake Case jason"
print(myVariableName)
print(MyVariableName)
print(my_variable_name)

# printfunction
x = "My Name is Andrew, First of his Name, Ruler of Egypt, Leader of the universe"
print(x)

a = "John Snow"
b = "is"
c = "cool"
print(a + b + c)

# typefuction
digit = 5
print(digit)
print(type(digit))

digit2 = 1.5
print(digit2)
print(type(digit2))

digit3 = 2j
print(digit3)
print(type(digit3))

# random library
import random
print(random.randrange(1, 100))

# CASTING
# integers
y = int(1)
z = int(1.5)
t = int("1")
print(type(y))
print(type(z))
print(type(t))

# float
b = float(1)
c = float(2.0)
d = float("3")
e = float("4.0")
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# string
f = str(1)
g = str(1.0)
print(type(f))
print(type(g))

# strings
string1 = "i am the strongest and brightest the most awsome teacher in the wourld"
print(string1)
print(type(string1))

# conccatenation
string2 = " he is also a superhero - Spider Man"
string3 = string1 + string2
print(string3)

# python booleans
digit4 = 10
digit5 = 50
if digit5 > digit4:
    print("digit5 is more than digit4")
else:
    print("digit4 is more than digit5")

# arithimetic operaters
h = 20
i = 30

# sums
j = h + i
print(j)

# subtraction
k = i + h
print(k)

# multiplication
l = h * i
print(l)

# divishion
m = i / h
print(m)

# modulus
n = i % h
print(n)

# list
thislist = ["apple", "banana", "chery", "mangoes", "avocado"]
print(thislist)

# access list
print(thislist[0])

# negetive indexing
print(thislist[-1])

# range of indexes
print(thislist[1:4])

# while loop
o = 1
while o < 6:
    print(o)
    o += 1

# break statement
p = 1
while p < 6:
    print(p)
    if p == 3:
        break
    p += 1

# else statment
q = 1
while q < 6:
    print(q)
    q += 1
else:
    print("q is more than six")

# for loops
cars = ["toyota", "subaru", "volkswagon", "nissan", "mazda"]
for x in cars:
    print(x)


# fuctions
def myfunction():
    print("this is a fuction")
myfunction()

# INPUT
name = input("what is your name:")
print("your name is:"+name)

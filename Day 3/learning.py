#swapping two numbers in a line

a ,b= 1, 2
a,b= b,a
print(a,b)

#swapping tow numbers

x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))

print("Before swapping: ",x,y)
x = x+y
y = x-y
x = y-x
print("After swapping: ",x,y)

#write a py program elgible for casting vote.a

age=int(input("Enter your age: "))
if age>=18:
    print("You are eligible for casting vote")
else:
    print("You are not eligible for casting vote")

#kids , child , teenager, adult, senior citizen

myage = int(input("Enter your age: "))
if myage<=5:
    print("You are a kid")
elif myage<=11:
    print("You are a child")
elif myage<=19:
    print("You are a teenager")
elif myage<=40:
    print("You are an adult")
else:
    print("You are a senior citizen")

#sum of 10 natural numbers

sum= 0
for i in range(11):
    sum = sum+i
print("The sum of first 10 natural numbers is",sum)

# list 

l=[10 , 41, 232, 2112, 1, 2]

print(max(l))

l.append(100)
print(l)

l.remove(10)
print(l)

l.pop()
print(l)

l.insert(2,100)
print(l)

l.sort()
print(l)

l.reverse()
print(l)

l.count(10)
print(l)

l.index(10)
print(l)

l.copy()
print(l)

l.clear()
print(l)

dict = {"name" : "John", "age" : 30, "city" : "New York"}
print(dict)

#set
l= [1,1,2,41,1, 2 ,2 ]
s = set(l)
print(s)

#tuple
t = (1,2,3,4,5)
print(t)

t.count(1)
print(t)

t.index(1)
print(t)

t.copy()
print(t)

t.clear()
print(t)    

def add(x,y):
    return x+y

print(add(1,2))

def sub(x,y):
    return x-y

print(sub(1,2))

def mul(x,y):
    return x*y

print(mul(1,2))

def div(x,y):
    return x/y

print(div(1,2))
print("hello")
print('hello')

print(4+5)
print(8*3)
print(4/3)
print(4.0/3)
print(3+5*9)

print("abc" + "def")
print("hello"+" " "world")
("123"+"5")
first="helo"
second="world"
print("first"+ " " + "second")
print(type(first))
print(first)
print(second)

age=input("What is your age?")
print(type(age))
town=input("Where do you come from?")

name="marian"
print("I am " +name)

school="UCC"
if school=="UCC":
    print("I am a " +school +  " student")
    
rep="Sarah"
if rep=="Sarah":
    print("She is " +rep)

names=["Pearl" "Amanda" "Rita"]
for beatle in names:
    print(beatle)
    
import math
def deg_to_radian(degree):
    return degree * (math.pi/180)
print(deg_to_radian(23))

personal=input("type degree")
print (deg_to_radian(float(personal)))

evens=[2,4,6,8]
sum=2+4+6+8
print(sum)

def get_name(name,password):
    return (name,password)
    
name=input("What is your name?")
pp=input("Enter your password")
print(get_name(name,pp))

def get_age(age):
    return(age)
age_2=input("How old are you?")
print(get_age(age_2))

#adding two numbers
def calculate(num1, num2):
    add= num1 + num2
    return  add 
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
print(calculate(num1,num2))



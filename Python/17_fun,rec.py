'''
#  Functions
def percent(marks):
    p= ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p
marks1=[78,89,96,85]
percentage1=percent(marks1)  
marks2=[87,90,80,65]
percentage2=percent(marks2)    # calls the above function
print(percentage1,percentage2)

# Greet
def greet(name):
    return "hello "+ name # if , is used insted of + then it returns ('hello','name')
a=str(input("Enter your name:"))
greeting=greet(a)
print(greeting)
'''
# Functions with arguments
def sum(num1,num2):   # has two arguments
    return num1+num2
a=int(input())
b=int(input())
s=sum(a,b)
print(s)
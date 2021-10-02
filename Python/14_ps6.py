# Practice Sheet
 
# Greater number 
'''a=int(input())
b=int(input())
c=int(input())
d=int(input())
if(a>b and a>c and a>d):
    print("a is greater:",a)
elif(b>a and b>c and b>d):
    print("b is greater:",b)
elif(c>a and c>b and c>d):
    print("c is greater:",c)
elif(d>a and d>b and d>c):
    print("d is greater:",d)  '''

# Pass and Fail
'''a=int(input("Enter marks in maths:\n"))
b=int(input("Enter marks in physics:\n"))
c=int(input("Enter marks in chemistry:\n"))
percentage=((a+b+c)/3)
print("Total percentage:",percentage)
if(percentage>33 and a>40 and b>40 and c>40):
    print("Congrats,you are pass")
else:
    print("Sorry,better luck next time")
'''
# Detecting user name
''' name=str(input("Enter your name:"))
if(str.len()>+10):
    print("User name is valid")
else:
    print("User name is invalid")
'''
    # Finding in list
'''list=["chdgfdh","hdjehfw","hdjewhd","urrywetu"]
a=str(input("Enter name:"))
if(a==list):
    print("yes")
else:
    print("no") '''

# Spam
text=str(input("Enter : "))

if("make money"== text):
    print("spam")
elif("click this"in text):
    print("spam")
elif("subscribe this"in text):
    print("spam")
else:
    print("Not spam")
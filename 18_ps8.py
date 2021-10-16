#1 Greatest
def max(a,b,c):
    if(a>b and a>c):
        print(a)
    elif(b>a and b>c):
        print(b)
    else:
        print(c)
max(5,7,9)  # prints 9

#2 Celsius to farenhiet
def temp_con(t):
    f=(t*9/5)+32
    print(f)
temp_con(38)

# sum of first n natural numbers
def sum(n):
    if(n==0):
        return 0
    return n+sum(n-1)
a=sum(10)
print(a)

# patterns
def pattern(n):
    for i in range(n):
        for j in range(n-i):
            print("* ",end="")
        print("\n")
pattern(5)

# prime
def prime(n):
    count=0
    for i in range(2,n):
        if(n%i==0):
            count=0
            break
        else:
            count=1
    if(count==1):
        print("prime :",i+1)
num=int(input())
for i in range(2,num):
    prime(i)        # checks wether "i" is prime or not and prints "i" if it is prime


# end
print("hello",end=" ")      # out put is  hello hellohello
print("hello",end="")      #             hello
print("hello")
print("hello")

# Tables
def table(n):
    for i in range(1,11):
        print(n,"X",i,"=",n*i)
table(7)
'''
#1 Multipliction table
n=int(input("enter number:"))
for i in range(10):
  print(n,"X",i,"=",n*i)

#2 prime number
n=int(input())
temp=0
for i in range(2,n):
    if(n%i==0):
        temp=1
        break
if temp==0:
 print("prime")
else:
    print("not prime")
    #3
for i in range(0,5):
    for j in range(0,i):
        print("*",end="")
    print("\n")
n=int(input())
k=2*n-2
for i in range(0,n):
 for j in range(0,k):
        print(end=" ")
 k=k-2
 for j in range(0,i+1):
        print("* ",end="")
 print("\r")

n=int(input())
for i in range(n):
    for j in range((n-i)-1):
        print(end=" ")
    for j in range(i):
        print("* ",end="")
    print("\n")

num=int(input())
for i in range(num):
    for j in range((2*num)-(2*i)):
        print(end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print("\n")
'''
#n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print("\n")   
'''
#5
l=["jhgv","jhggguj","dszes","oiuuyf"]
for name in l:
    if name.startswith("j"):
        print("hello ",name)

#6
n=int(input())
sum=0
i=0
while i<n+1:
    sum=sum+i
    i=i+1
print("sum",sum)

#7 Factorial
a=int(input())
fact=1
if(a==0 or a==1):
    print(fact)
else:
 for i in range(1,a+1):
    fact=fact*i
print(fact)'''
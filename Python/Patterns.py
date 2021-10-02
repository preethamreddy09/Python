'''# Number triangle pattern
n=int(input())           #  1
for i in range(n+1):     #  22
    for j in range(i):   #  333
        print(i,end="")  #  4444
    print("\n")          #  55555     for n=5

# Inverted number pattern   
n=int(input())               # 55555   (n=5,i=0) >> n-i=5
for i in range(n):           # 4444    (n=5,i=1) >> n-1=4
    for j in range(n-i):     # 333
        print(n-i,end="")    # 22
    print("\n")              # 1        for n=5

n=int(input())               # 1 1 1 1 1
for i in range(n):           # 2 2 2 2
    for j in range(n-i):     # 3 3 3
        print(i+1,end=" ")   # 4 4
    print("\n")              # 5        

n=int(input())                   # 1           j=0 >> j+1=1
for i in range(n):               # 12          j=0 , j=1
    for j in range(i+1):         # 123         j=0 , j=1 , j=2
        print(j+1,end="")        # 1234       
    print("\n")                  # 12345       

# invetrd triangle of same number
n=int(input())                   # 55555
for i in range(n):               # 5555
    for j in range(n-i):         # 555
        print("5",end="")        # 55
    print("\n")                  # 5          

# reverse triangle               
n= int(input())                  # 1      i=1 , j=0 >> i-j =1
for i in range(n+1):             # 21     i=2 , j=0 & j=1  >> 2-0=2 , 2-1=1
    for j in range(i):           # 321
        print(i-j,end="")        # 4321
    print("\n")                  # 54321          

n=int(input())                   # 012345
for i in range(n):               # 01234
    for j in range(n-i+1):       # 0123
        print(j,end="")          # 012
    print("\n")                  # 01        
'''
# triange using natural numbers
n=1
a=int(input("enter no of rows:"))    # a=3
for i in range(a+1):                 # 1
    for j in range(2*i+1):               # 2 3 4
        print(n,end=" ")             # 5 6 7 8 9
        n=n+1
    print("\n")                               
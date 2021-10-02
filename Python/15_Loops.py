'''
i=9
while i<15:
    print("yes",i)   # prints yes until i=14 that is 6 times
    i=i+1  # increments i by 1
print("completed")

# to print first 50 natural numbers
i=1
while i<=50:
    print(i)
    i=i+1

# to print contents of a list
list=[7,"hg",98,9.8,"jhg"]
i=0
while i<len(list):
    print(list[i])
    i=i+1

# For Loop
l=[1,3,6]
for item in l:
    print(item)
#Range function
for i in range(10): # can also be written as (0,10)
    print(i)   # prints 0 to 9
for i in range(0,10,2):  # prints 2,4,6,8
    print(i)

# for else
a=[1,2,3]
for item in a:
    print(item)
else:            # else only gets printed if for loop is successfullu printed
    print("done")  # 

# break statement
for i in range(0,60):
    print(i)
    if(i==5):
        break  # break stops the loop at given condition
else:
    print("done") # this is not printed since for loop is not fully printed
'''
# continue statement
for i in range(10):
    if(i==5):
        continue  # skips 5 and prints remaining
    print(i)

# pass statement
for i in range(5):
    pass  # do nothing also known as null
print("hi")

'''#To read contents of the file
#f=open('sample.txt',"r") 
f=open("sample.txt")  # 'r' is default >>> "" and '' doesn't matter
data=f.read()
#data=f.read(2)  gives only 2 characters
print(data)
f.close()

# Read line fun
f=open("sample.txt")
data=f.readline() # reads only first line
print(data)
data=f.readline()    # reads  second line
print(data)  
f.close()

# Write function
f=open('another.txt','w')  # "another" file automatically gets created
f.write("hello  hi")
f.close()
# Append
f=open("another.txt",'a')   # if 'w' is used after this whole file gets cleared new data will be enterd
f.write("appending")   # foe each time we run the program the word "appending" gets added to the file at the end
f.close()'''

# With statement
with open("sample.txt",'r') as f:
    a=f.read()
    print(a)

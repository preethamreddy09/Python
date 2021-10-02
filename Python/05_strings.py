# Strings
a="harry"
b="bhai"
print(type(a))
print(a+ b) # combines two strings

# String Slicing
name = "Preethamreddy" # P=0,-8  r=1,-7 .... m=7,-8
print(name[-8]) # prints h
print(name[7])
 # name[4] = "r"  new character cannot be accessed
print(name[0:4]) # prints first 4 characters
print(name[:-4]) # prints -13 to -4
n = name[5:8]
print(n)
 
# Skip  Slicing
print(name[1:3:1]) # prints 1,2 (r e) and skips 3(e)  
print(name[1::2]) # prints rehmed skips alternate letters

# String Functions
name = "fghgfgfjkhkjh"
print(len(name)) # returns length
print(name.endswith("jhj")) # returns true or false based on condition
print(name.count("j"))  # counts n0'of j's and prints
print(name.capitalize()) # converts first letter into capital
print(name.find("f")) # prints position of f
print(name.replace("f","i"))
story = "once upon a time.\nthere lived a king" #prints in 2 lines
print(story)
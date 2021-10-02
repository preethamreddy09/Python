'''
a = {}
print(type(a))  # it represents an dictionary

b = set()
print (type(b))  # it represents a set   '''

# representing set
a = {2,4,6}  #represents a set
b= {2,4,6,2,'hbh',"uguy"}  
print(a) #prints 2,4,6,8
print(b)  #prints 2,4,6,8 but not the second 2 since set is irrepetitive

# METHODS
#Adding values
b.add(3)
b.add(5) # adds the numbers into set b
b.add(5)  # does not add  since set is irrepititive
# b.add([1,2,3]) # we cannot add List into set
# b.add({4:8}) # cannot add dict
print(b)  

#Length
print(len(b))
#Remove
b.remove(4)
#b.remove(10)  :  Throws error since 10 is not present
print(b)
#Pop
print(b.pop()) # removes random element and prints it
#Clear
# print(b.clear())  # empties set b and returns none
#Union and Intersection
print(b.union({2,6,8,9})) # performs union operation
print(b.intersection({4,6,0})) # performs intersection operation
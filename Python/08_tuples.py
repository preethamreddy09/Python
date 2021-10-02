
# Creating tuples
a = ()  # tuple with zero element

b = (2,)  # tuple with one element  >> b=(2) it is error

c = (2,3,4,5,'hjjhv') # tuple with more than 1 element
#c[0] = 5  # gives error since it cannot be changed or updated

print(c)
print(c[2]) # printing element at second index


# Tuple Methods
t = (1,2,3,4,5)

print(t.count(1))  # prints total number of 1's in the tuple
print(t.index(3))  # returns the index where 1 is present

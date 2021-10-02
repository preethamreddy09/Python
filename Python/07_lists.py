a = [6, "ggh", 78, "ftf" , 8, 0.9] # different data types can be used

# printing list
print(a)

#accessing list using index     
print(a[-2]) #returns 78
print(a[1])  #returns ggh

# changing the values of list
a[2] = 3.5
print(a[2]) # changes a[2]

# list slicing
print(a[-5:])
print(a[2:5])

'''LIST METHODS :
                  1: Sort : sorts the list 
                  2: Append : adds the given element at the end
                  3: Insert : adds element at given index
                  4: Reverse : reverses the list
                  5: Remove : removes the element
                  6: Pop : removes element at given index'''
L1 = [4,7,2,75,15,8,22,90,50]
print(L1.sort()) # returns none 
L1_sorted =L1.sort()
print(L1_sorted) # returns none
L1.sort() # returns sorted list
print(L1) 
L1.append(45) # appends at the end of the list (adds 45 at the end)
print(L1)
L1.insert(1,67) # insrts 67 at 1st index
print(L1) 
L1.reverse() # reverse list
print(L1)
L1.remove(67) # removes 67
print(L1)
L1.pop(3) # removes element ppresent at index 3
print(L1)








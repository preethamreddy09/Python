myDict = {
    "fruit" : "Banana",         # "fruit" is key and banana is value
    "vegetable": "Onion",         
    "number": [1,2,5,8],
    "adddict":{"Letter":"hello",  # sub dictionaries can be written inside a dictionary
    "list":[1,3,5]}
}
myDict["Number"] = [3,5,6] # a dictionary can be changed
print(myDict["Fruit"])
print(myDict["Number"])
print(myDict["adddict"]["list"]) # required sub dict can be acced from main

# dictionary Methods
print(myDict.keys())  # prints all the keys
print(myDict.values()) # prints all the values
print(myDict.items()) #prints keys+values
newDict ={
    "vehicles":["car","bus","bike"]
}
myDict.update(newDict) # adds the vehicles item
print(myDict) # prints mydict with vehicles being updated
print(myDict.get("vegetable")) # prints the value corresponding to key .. even vegetable is noy present it doesn't throw errorr
print(myDict["vegetable"]) # throws error if vegetable is not present

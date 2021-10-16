'''# searching in file
def poems(word):
    if word in data:   # data is read with the help of rad function
        print("yes")
    else:
        print("no")
w=str(input())
f=open("poems.txt","r")
data=f.read()
f.close()
poems(w)    # "w" goes into function in place of "word"

# Game score updation

score=int(input("Enter your score :"))            # takes input from user
with open("game.txt")as f:    # opens the file "game.txt"
    hi_score=int(f.read())    # assings the score present in file to hi_score
if score>hi_score:               
    with open("game.txt","w")as f:  # opens file
        f.write(str(score))    # updates if condition is true

# Multiplication tables & Files

for i in range(2,21):
    with open(f"tables of {i}",'w')as f:  # known as f_string    takes i value according to loop
        for j in range(1,11):
            f.write(f"{i}X{j}={i*j}")       # prints 2X2=4  for i=2 and j=2 and so on
            if j!=10:
                f.write('\n')          # prints in new line for each iteration of j ""(double quotes) is not valid
# creates a total of 19 tables for each value of i

# updating

f=open("donkey.txt")
content=f.read()
content=content.replace("donkey","####")
f=open("donkey.txt",'w')
f.write(content)
'''
# Find
w="python"
f=open("find.txt")
data=f.read()
if w in data:
    print("yes")
else:
    print('false')
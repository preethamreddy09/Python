# strings practice sheet

#1 to display
#name =str(input())
#print(name + " Good Afternoon")

#2 letter template
letter ='''Dear <|NAME|>
Greetings From Google:
You are selected
Date : <|Date|>'''

#name1 = input("enter name:\n")
#date = input("Enter date\n")
letter = letter.replace("<|NAME|>","preetham") # replace it with the name1
letter = letter.replace("<|Date|>","0887") # if 'letter =' is not written then the original letter is printed
print(letter)

# detect double spaces, replacng itt wiith single spaces
statement= "jbhgf  jhg  gfd jb  hgg jkhgf" # prints only first double space
ds = statement.find("  ")
rep = statement.replace("  "," ")
print(rep)

# Escape sequences
''' \n: for new line
    \t: for new tab
    \': for single quote
    \\: for single slash
    '''
sentence="Once upon a time,\nThere liv\\ed a king.\n\t He ha\'d 7sons."
print(sentence)
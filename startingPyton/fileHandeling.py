# open & close #

# ==== open ==== #
# Modes  
# 'r' => open & read as a text
# 'rb' => open & read as a binary
# 'r+' => open for read and writ
# 'w' => open for writ

# .read()  => read the all content
# .readlines() => retyrn the lines in array
# .readline() => read the fersth line of the file

# open('file name', mode)
file = open('index.py', mode='r')
print(file.read())
file.close()

with open('text.text', mode='r')as text:
    print(text.readline())

with open('newText.txt','w') as newFile:
   newFile.writelines(["This is a new file created! \n","new line to add \n","mor lins to add"])

# append text  "a" in the mode
for i in range(10):
    with open('newText.txt','a') as newFile:
        newFile.writelines(["\n appended text: " + str(i),"\n more append"])


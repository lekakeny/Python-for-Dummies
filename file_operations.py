"""
File operation involves

1. opening the file
2. read or write the file
3. close file

Here we are learning how to read and write files. I learnt how to read and write long time ago! How could I be
learning now? Anyway, kwani ni kesho?

"""

f = open('text.txt', 'w',
         encoding='utf8')  # open the file called text.txt if it does exist. If not the python will create one

"Read from standard input and write to the file"
"""
inputs = input('input: ')  # Define the input
f.write(inputs)  # write the input to the file using the write method
f.close()  # close the file so that the file object may not remain in memory. Data is only written when the file closes

"""

"Read from the file we have just created"
f = open('text.txt', 'r')  # r means read only
print(f.read(6))  # read 6 characters from the current position (default is 0)
print(f.read())  # read from current position to the end
f.close()

"Add more data to the file by using mode 'a'"
f = open('text.txt', 'a')
f.write(' I have just added this content to the file!')
f.close()

"Use 'with' statement to open file. File object will automatically close"
with open('text1.txt', 'w') as f:
    f.write('I have learnt a new technique\n I am not very masai anymore\n call me stupid at your own risk')
# use with statement to read the file
with open('text1.txt', 'r') as f:
    print("This is the file I have created: \n", f.read())

'Read the file line by line using the \'readline()\' method'

with open('text1.txt', 'r') as f:
    line = f.readline()
    print("read one line: %s" % line)
    # use readlines to get a list of lines
    lines = f.readlines()  # starts from the current position
    print(lines)

"Can I call this file management? I now know how to read and write in python!"

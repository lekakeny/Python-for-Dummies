"""
Regular expressions are a sequence of characters that define a search pattern

eg abc@abc.com matches a pattern of an email address

Embedded to python through the RE module
"""
# Import re module
import re

print(re.match('www', 'www.datactuary.com').span())  # Match from the start of the text
print(re.match('com', 'www.datactuary.com'))  # Cannot Match from the middle of the text
print(re.search('com', 'www.datactuary.com'))  # Search Matches from anywhere in the text

line = "The Goats are prettier than sheep"
searchobj = re.search(r'The (.*) are prettier than (.*)', line)
if searchobj:
    print("searchobj.group() : ", searchobj.group())
    print("searchobj.group(1) : ", searchobj.group(1))
    print("searchobj.group(2) : ", searchobj.group(2))
else:
    print("Nothing Found")

"re.compile(patter).search(text) is equivalent to re.search(pattern, text)"
pattern = re.compile(r'\d+')  # Match at least one digit
n = pattern.match('one12twothree24four')  # match from start. no match
print(n)

# search from start, found 12
m = pattern.search('one12twothree24four')
print(m)
print(m.group())

phone = "2020-0101-000-2124  #This is a phone number"
# remove the number sign (#) and everything behind it
num = re.sub(r'#.*', "", phone)
print("The phone number is: ", num)
# Remove everything that is not digit
num = re.sub(r'\D', '', phone)
print("The new phone number format is: ", num)

# Find all numbers in the text
text = "I went to University on the 26th/08/2013, but I graduated on the 02/11/2018. I studied actuarial science for " \
       "a whole 5 years! Either way, send me an email through lekakeny.karoi@gmail.com or view more about us on " \
       "www.datactuary.com "
num1 = re.findall(r'\d+', text)
num2 = re.findall(r'[0-9]{2,5}', text)  # the second braces imply the range of the length of digits

print("The first number is: ", num1)
print("The second number is: ", num2)

# Find all alphabets in the text
s = re.findall(r'[a-zA-z]+', text)
print(s)

"Find all symbols in the text"
# This excludes words and underscores
s = re.findall(r'\W+', text)
print("The symbols in the text are: ", s)

"Find all alphabets and digits"
s = re.findall(r'[A-Za-z0-9]+', text)
print("The alphabets and digits are: ", s)

"Find Email Address"

s = re.findall(r'[A-Za-z0-9]+\.[A-Za-z0-9]+@[A-Za-z0-9]+\.com', text)
print("My email address is: ", s)

"Find URL"
s = re.findall(r'www\..*', text)
print("Our website is: ", s)

"Find every div tag"
# find first match
html = "aa<div>test1</div>bb<div>test2</div>cc"
res = re.search("</div>.*</div>", html)
print(res.group())

# find last match
res = re.search("</div>.*?</div>", html)
print(res.group())

"Learning this was super fun!"

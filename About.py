import wikipedia
from googlesearch import search
import requests
from bs4 import BeautifulSoup

commands = "search about jarvis"

q = commands.replace("about ","")
qu = q.replace("search","")
query = qu.replace(" ","")
r = ""
c = 1
newq = ""
new = False
found = False
# C = 0

# file = open("SearchBytes.txt", "r")
# C = file.read()

# if C != "":
#     C = int(C)

# else:
#     C = 0

file = open("Search.txt","a+")
file = open("Search.txt", "w")
# speak(f"I am Searching for {query} on Wikipedia")

q = qu.upper()

for i in range(len(query)):
    
    newq+=q[i]+"."

# for i in range(len(newq)-1):
    
#     qnew+=newq[i]

try:
    r = wikipedia.summary(query, sentences = 16 )
    c = 0
except :
    pass

if len(r) != 0:
    
    found = True
    # print("\nAccording to Wikipedia................\n\n")
    # speak("According to wikipedia")
    # speak(r)
else:
    if found == False:
        r = wikipedia.summary(newq, sentences = 16 )
        c = 0
        found = True
        new = True
    # speak("I could not find any valuable information in wikipedia")

if found == True:
    
    # q = qu.capitalize()
    file.write(("*"*7)+f" {q} "+("*"*7))
    file.write("\nAccording to Wikipedia................\n")
    file.write(r+"\n")
    print("\nAccording to Wikipedia................\n",r,"\n")
else:
    print("\nI could not find any valuable information in wikipedia")
    print()
    

if new == True:
    
    qu = q


for i in search(qu,        # The query you want to run
                tld = 'com',  # The top level domain
                lang = 'en',  # The language
                num = 4,     # Number of results per page
                start = 0+c,    # First result to retrieve
                stop = 5+c,  # Last result to retrieve
                pause = 0,  # Lapse between HTTP requests
                ):
    
    if (("wikipedia" not in i) or c == 1) and ("image" not in i) :
        
        file.write("\nAccording To "+i)
        file.write("\n")
        print("\nAccording To "+i)
        firstresponse = ""
        
        try:
            firstresponse = requests.get(i)
        except:
            pass
        
        firstsoup = BeautifulSoup(firstresponse.text, features = "lxml")
        t = firstsoup.text
        l = t.split("\n")
        
        str = ""
        
        for i in l:
            if i != "\t":
                if len(i)>500:
                    str+=i
                    file.write(i)
                    file.write("\n")
                    print(i)
                    # speak(i)
                    print()

file.close()

file1 = open("Search.txt", "r")
# file2 = open("SearchBytes.txt", "w")

# if C != 0:
#     file1.seek(C)

c = file1.read()
l = c.split(". ")
# print(c)
l = set(l)

# for i in l:
#     if "\n\n" in i:
#         print(i+". ", end = "")
#     else:
#         print(i+". ")
# print()

# C = len(c)

# if C != "":
#     file2.write(f"{C}")

# file2.close()
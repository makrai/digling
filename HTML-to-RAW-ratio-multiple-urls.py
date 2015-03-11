#imredavidandras@gmailcom

print "HTML-to-NON-HTML ratio estimator, v1.1", "\n"

#the program takes a .txt file as input, which contains the urls
#the output is printed on the screen

import urllib2

#the following global variables are used

num = 0 #number of characters in the raw text (without whitespaces)
html = 0 #number of characters in html tags (including '<'s and '>'s)
escape_num = 0 #the number of escape sequences in the raw text
escape_html = 0 #the number of escape sequences in the html tags

#the following function loops through the given input, character by character, and removes every comment
#the removed parts count as html

def removeComments(listOfChars):
    i = 0
    state = 0
    index_list = []
    global html
    for c in listOfChars:
        if state == 0:
            if c == "<":
                index_list.append(i)
                state = 1
                i += 1
            else:
                i += 1
        elif state == 1:
            if c == "!":
                index_list.append(i)
                state = 2
                i += 1
            else:
                index_list.pop(len(index_list)-1)
                state = 0 #maybe you caught me cheating here. if you did, just trust me. from now on, this will be the case.
                i += 1
        elif state == 2:
            if c == "-":
                index_list.append(i)
                state = 3
                i += 1
            else:
                index_list.append(i)
                i += 1
        elif state == 3:
            if c == "-":
                index_list.append(i)
                state = 4
                i += 1
            else:
                index_list.append(i)
                state = 2
                i += 1
        elif state == 4:
            if c == ">":
                index_list.append(i)
                state = 0
                i += 1
            else:
                index_list.append(i)
                state = 2
                i += 1
        else:
            i += 1
    for n in index_list[::-1]:
        del listOfChars[n]
    html = html + len(index_list)

#the following function loops through the given input, character by character, and removes every script
#the removed parts count as html
    
def removeScripts(listOfChars):
    i = 0
    state = 0
    index_list = []
    global html
    for c in listOfChars:
        if state == 0:
            if c == "<":
                index_list.append(i)
                state = 1
                i += 1
            else:
                i += 1
        elif state == 1:
            if c == "s":
                index_list.append(i)
                state = 2
                i += 1
            else:
                index_list.pop(len(index_list)-1)
                state = 0
                i += 1
        elif state == 2:
            if c == "c":
                index_list.append(i)
                state = 3
                i += 1
            else:
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                state = 0
                i += 1
        elif state == 3:
            if c == "r":
                index_list.append(i)
                state = 4
                i += 1
            else:
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                state = 0
                i += 1
        elif state == 4:
            if c == "i":
                index_list.append(i)
                state = 5
                i += 1
            else:
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                state = 0
                i += 1
        elif state == 5:
            if c == "r":
                index_list.append(i)
                state = 6
                i += 1
            else:
                index_list.append(i)
                i += 1
        elif state == 6:
            if c == "i":
                index_list.append(i)
                state = 7
                i += 1
            else:
                index_list.append(i)
                state = 5
                i += 1
        elif state == 7:
            if c == "p":
                index_list.append(i)
                state = 8
                i += 1
            else:
                index_list.append(i)
                state = 5
                i += 1
        elif state == 8:
            if c == "t":
                index_list.append(i)
                state = 9
                i += 1
            else:
                index_list.append(i)
                state = 5
                i += 1
        elif state == 9:
            if c == ">":
                index_list.append(i)
                state = 0
                i += 1
            else:
                index_list.append(i)
                state = 5
                i += 1
        else:
            i += 1
    for n in index_list[::-1]:
        del listOfChars[n]
    html = html + len(index_list)

#the following function loops through the given input, character by character, and removes every style
#the removed parts count as html

def removeStyles(listOfChars):
    i = 0
    state = 0
    index_list = []
    global html
    for c in listOfChars:
        if state == 0:
            if c == "<":
                index_list.append(i)
                state = 1
                i += 1
            else:
                i += 1
        elif state == 1:
            if c == "s":
                index_list.append(i)
                state = 2
                i += 1
            else:
                index_list.pop(len(index_list)-1)
                state = 0
                i += 1
        elif state == 2:
            if c == "t":
                index_list.append(i)
                state = 3
                i += 1
            else:
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                state = 0
                i += 1
        elif state == 3:
            if c == "y":
                index_list.append(i)
                state = 4
                i += 1
            else:
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                state = 0
                i += 1
        elif state == 4:
            if c == "l":
                index_list.append(i)
                state = 5
                i += 1
            else:
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                state = 0
                i += 1
        elif state == 5:
            if c == "t":
                index_list.append(i)
                state = 6
                i += 1
            else:
                index_list.append(i)
                i += 1
        elif state == 6:
            if c == "y":
                index_list.append(i)
                state = 7
                i += 1
            else:
                index_list.append(i)
                state = 5
                i += 1
        elif state == 7:
            if c == "l":
                index_list.append(i)
                state = 8
                i += 1
            else:
                index_list.append(i)
                state = 5
                i += 1
        elif state == 8:
            if c == "e":
                index_list.append(i)
                state = 9
                i += 1
            else:
                index_list.append(i)
                state = 5
                i += 1
        elif state == 9:
            if c == ">":
                index_list.append(i)
                state = 0
                i += 1
            else:
                index_list.append(i)
                state = 5
                i += 1
        else:
            i += 1
    for n in index_list[::-1]:
        del listOfChars[n]
    html = html + len(index_list)

#the following 5 functions loop through the given input, character by character, and removes every escape sequence
#baceuse the format of the escape sequences are the following: "&...;" ("..." stands for 3, 4, 5, 6 characters),
#the functions return the total number of "&"s from the removed parts
#the returned number is addded to the corresponding part
#except for the first one, which is only used to remove non breaking spaces

def removeSpaces(listOfChars): #this is the function to remove non breaking spaces, i.e. &nbsp;
    i = 0
    state = 0
    index_list = []
    total = 0
    for c in listOfChars:
        if state == 0:
            if c == "&":
                index_list.append(i)
                state = 1
                i += 1
            else:
                i += 1
        elif state == 1:
            if c == "n":
                index_list.append(i)
                state = 2
                i += 1
            else:
                index_list.pop(len(index_list)-1)
                i += 1
                state = 0
        elif state == 2:
            if c == "b":
                index_list.append(i)
                state = 3
                i += 1
            else:
                i += 1
                state = 0
        elif state == 3:
            if c == "s":
                index_list.append(i)
                state = 4
                i += 1
            else:
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                i += 1
                state = 0
        elif state == 4:
            if c == "p":
                index_list.append(i)
                state = 5
                i += 1
            else:
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                i += 1
                state = 0
        elif state == 5:
            if c == ";":
                index_list.append(i)
                total += 1
                state = 0
                i += 1
            else:
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1) 
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                state = 0
                i += 1
        else:
            i += 1
    for n in index_list[::-1]:
        del listOfChars[n]
    return total

def removeEscapes5(listOfChars): #this is the function for 5 character long escape sequences
    i = 0
    state = 0
    index_list = []
    total = 0
    global num
    for c in listOfChars:
        if state == 0:
            if c == "&":
                index_list.append(i)
                state = 1
                i += 1
            else:
                i += 1
        elif state == 1:
                index_list.append(i)
                state = 2
                i += 1
        elif state == 2:
                index_list.append(i)
                state = 3
                i += 1
        elif state == 3:
                index_list.append(i)
                state = 4
                i += 1
        elif state == 4:
            if c == ";":
                index_list.append(i)
                total += 1
                state = 0
                i += 1
            else:
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                state = 0
                i += 1
        else:
            i += 1
    for n in index_list[::-1]:
        del listOfChars[n]
    return total

def removeEscapes6(listOfChars): #this is the function for 6 character long escape sequences
    i = 0
    state = 0
    index_list = []
    total = 0
    global num
    for c in listOfChars:
        if state == 0:
            if c == "&":
                index_list.append(i)
                state = 1
                i += 1
            else:
                i += 1
        elif state == 1:
                index_list.append(i)
                state = 2
                i += 1
        elif state == 2:
                index_list.append(i)
                state = 3
                i += 1
        elif state == 3:
                index_list.append(i)
                state = 4
                i += 1
        elif state == 4:
                index_list.append(i)
                state = 5
                i += 1
        elif state == 5:
            if c == ";":
                index_list.append(i)
                total += 1
                state = 0
                i += 1
            else:
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1) 
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                state = 0
                i += 1
        else:
            i += 1
    for n in index_list[::-1]:
        del listOfChars[n]
    return total

def removeEscapes7(listOfChars): #this is the function for 7 character long escape sequences
    i = 0
    state = 0
    index_list = []
    total = 0
    global num
    for c in listOfChars:
        if state == 0:
            if c == "&":
                index_list.append(i)
                state = 1
                i += 1
            else:
                i += 1
        elif state == 1:
                index_list.append(i)
                state = 2
                i += 1
        elif state == 2:
                index_list.append(i)
                state = 3
                i += 1
        elif state == 3:
                index_list.append(i)
                state = 4
                i += 1
        elif state == 4:
                index_list.append(i)
                state = 5
                i += 1
        elif state == 5:
                index_list.append(i)
                state = 6
                i += 1
        elif state == 6:
            if c == ";":
                index_list.append(i)
                total += 1
                state = 0
                i += 1
            else:
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1) 
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                state = 0
                i += 1
        else:
            i += 1
    for n in index_list[::-1]:
        del listOfChars[n]
    return total

def removeEscapes8(listOfChars): #this is the function for 8 character long escape sequences
    i = 0
    state = 0
    index_list = []
    total = 0
    global num
    for c in listOfChars:
        if state == 0:
            if c == "&":
                index_list.append(i)
                state = 1
                i += 1
            else:
                i += 1
        elif state == 1:
                index_list.append(i)
                state = 2
                i += 1
        elif state == 2:
                index_list.append(i)
                state = 3
                i += 1
        elif state == 3:
                index_list.append(i)
                state = 4
                i += 1
        elif state == 4:
                index_list.append(i)
                state = 5
                i += 1
        elif state == 5:
                index_list.append(i)
                state = 6
                i += 1
        elif state == 6:
                index_list.append(i)
                state = 7
                i += 1
        elif state == 7:
            if c == ";":
                index_list.append(i)
                total += 1
                state = 0
                i += 1
            else:
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1) 
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                state = 0
                i += 1
        else:
            i += 1
    for n in index_list[::-1]:
        del listOfChars[n]
    return total
    
#the following function loops through the source code, character by character
#in every step the corresponding list is is extended by one character, depending on the the value of inHtmlTag
#at the end, the length of those lists are measured
    
def charCount(listOfChars):
    inHtmlTag = False
    global html
    global num
    global escape_html
    global escape_num
    tag = []
    nontag = []
    for c in listOfChars:
        if inHtmlTag == False:
            if c == "<":
                inHtmlTag = True
            else:
                nontag.append(c)
        if inHtmlTag == True: #this is intentionally an if, not an elif
            if c == ">":
                tag.append(c)
                inHtmlTag = False
            else:
                tag.append(c)
    removeSpaces(tag)
    removeSpaces(nontag)
    escape_num = escape_num + removeEscapes5(nontag)
    escape_num = escape_num + removeEscapes6(nontag)
    escape_num = escape_num + removeEscapes7(nontag)
    escape_num = escape_num + removeEscapes8(nontag)
    escape_html = escape_html + removeEscapes5(tag)
    escape_html = escape_html + removeEscapes6(tag)
    escape_html = escape_html + removeEscapes7(tag)
    escape_html = escape_html + removeEscapes8(tag)
    num = num + len(nontag) + escape_num
    html = html + len(tag) + escape_html
    print "url:", urls[n].replace("\n", "")
    print "number of characters in the html tags", html
    print "number of characters outside html tags:", num
    print "total:", html+num
    print "HTML/text ratio", float(html)/num
    print "\n"
    html = 0
    num = 0
    escape_html = 0
    escape_num = 0

#the following cycle loops through the input list, and sends a request to the next url
#the source code of the given site will be the text in which we count the characters
#the header tells the site that this is an agent using mozilla
#this is necessary because some sites deny requests from random robots
    
with open("urls.txt") as f:
    urls = f.readlines()

for n in range(len(urls)):
    print "WAIT, THE MAGIC HAPPENS SOON!"
    req = urllib2.Request(urls[n], headers={ "User-Agent": "Mozilla/5.0" })
    target = urllib2.urlopen(req)
    inter = target.read()
    inter = inter.decode("utf-8")
    inter = inter.replace("<style type", "<s><style>")
    inter = inter.replace("<!DOCTYPE", "<DOCTYP><")
    inter = inter.replace("<!doctype", "<doctyp><")
    inter = inter.replace("<![", "<[[")
    inter = inter.replace("<]]", "<]]")
    inter = inter.replace("\n", "")
    inter = inter.replace("\r", "")
    inter = inter.replace("\t", "")
    inter = inter.replace(" ", "")
    text = list()
    for c in inter:
        text.append(c)

    removeComments(text)
    removeScripts(text)
    removeStyles(text)
    charCount(text)
    

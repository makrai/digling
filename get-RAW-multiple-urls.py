#imredavidandras@gmail.com

print "HTML from raw text separator minitool for multiple urls, v1.1", "\n"

#this program separates html formatting from the raw text
#the input is a .txt file, containing the urls
#the output is the raw text from each site
#please note, that some strings are replaced at the very beginning of the process
#you can find those at the end of the program, right after the request sending process

import urllib2

#the following functions are used in the process

def removeComments(listOfCharacters): #the input is really a list
    i = 0
    state = 0
    index_list = []
    for c in listOfCharacters:
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
                state = 0
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
        del listOfCharacters[n]

def removeScripts(listOfCharacters):
    i = 0
    state = 0
    index_list = []
    for c in listOfCharacters:
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
        del listOfCharacters[n]
        
def removeStyles(listOfCharacters):
    i = 0
    state = 0
    index_list = []
    for c in listOfCharacters:
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
        del listOfCharacters[n]

def removeEscapes5(listOfCharacters):
    i = 0
    state = 0
    index_list = []
    for c in listOfCharacters:
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
        del listOfCharacters[n]

def removeEscapes6(listOfCharacters):
    i = 0
    state = 0
    index_list = []
    for c in listOfCharacters:
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
        del listOfCharacters[n]

def removeEscapes7(listOfCharacters):
    i = 0
    state = 0
    index_list = []
    for c in listOfCharacters:
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
        del listOfCharacters[n]

def removeEscapes8(listOfCharacters):
    i = 0
    state = 0
    index_list = []
    for c in listOfCharacters:
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
        del listOfCharacters[n]

def htmlSeparate(listOfCharacters):
    state = 0
    tag = []
    nontag = []
    for c in listOfCharacters:
        if state == 0:
            if c == "<":
                state = 1
            else:
                nontag.append(c)
        if state == 1:
            if c == ">":
                tag.append(c)
                state = 0
            else:
                tag.append(c)
    removeEscapes5(nontag)
    removeEscapes6(nontag)
    removeEscapes7(nontag)
    removeEscapes8(nontag)
    for b in nontag:
        raw.write(b.encode("utf-8"))
    raw.close()
    
#the following is the main part of the program

with open("urls.txt") as f:
    urls = f.readlines()
for n in range(len(urls)):
    req = urllib2.Request(urls[n], headers={ "User-Agent": "Mozilla/5.0" })
    target = urllib2.urlopen(req)
    inter = target.read()
    inter = inter.decode("utf-8") #decode unicode entities
    inter = inter.replace("<style type", "<s><style>") #replace problematic tags
    inter = inter.replace("<!DOCTYPE", "<DOCTYP><")
    inter = inter.replace("<!doctype", "<doctyp><")
    inter = inter.replace("<![", "<[[")
    inter = inter.replace("<!]", "<]]")
    text = list() #make a list containing every character
    for c in inter:
        text.append(c)

    raw = open(urls[n].replace("http://", "")
               .replace("https://", "")
               .replace("/", "-")
               .replace("\n", "")
               + ".txt",
               "w")
    print "\n", "PLEASE WAIT"
    print "URL: ", urls[n].replace("\n", "")
    print "removing comments..."  
    removeComments(text) #comment removal
    print "removing scripts..."
    removeScripts(text) #script removal
    print "removing styles..."
    removeStyles(text) #style removal
    print "separating html and non-html characters..."
    htmlSeparate(text) #separating the remaining parts
    print "DONE!"
    print "Filename:", raw.name, "\n" 

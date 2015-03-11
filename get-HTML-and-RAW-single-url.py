#imredavidandras@gmail.com

print "HTML from raw text separator minitool for a single URL, v1.1", "\n"

#this program separates html formatting from the raw text
#the program takes a url as input, which is entered manually
#as output, the program creates or OVERWRITES the following text files

tag_ = open("html.txt", "w") #html.txt contains html formatting besides comments, scripts, styles
nontag_ = open("raw_text.txt", "w") #raw_text.txt contains non-html strings, without escape sequences
comments = open("comments.txt", "w") #comments.txt contains every comment
scripts = open("scripts.txt", "w") #scripts.txt contains every script 
styles = open("styles.txt", "w") #styles.txt contains every style
escapes = open("escapes.txt", "w") #escapes.txt cointans every escape sequence from the non-html part

#please note, that some strings are replaced at the very beginning of the process
#you can find those at the end of the program, right after the request sending process

import urllib2

#the following functions are used in the process

def removeComments(listOfCharacters): #the input is really a list
    i = 0
    state = 0
    comment = []
    index_list = []
    for c in listOfCharacters:
        if state == 0:
            if c == "<":
                comment.append(c)
                index_list.append(i)
                state = 1
                i += 1
            else:
                i += 1
        elif state == 1:
            if c == "!":
                comment.append(c)
                index_list.append(i)
                state = 2
                i += 1
            else:
                comment.pop(len(comment)-1)
                index_list.pop(len(index_list)-1)
                state = 0
                i += 1
        elif state == 2:
            if c == "-":
                comment.append(c)
                index_list.append(i)
                state = 3
                i += 1
            else:
                comment.append(c)
                index_list.append(i)
                i += 1
        elif state == 3:
            if c == "-":
                comment.append(c)
                index_list.append(i)
                state = 4
                i += 1
            else:
                comment.append(c)
                index_list.append(i)
                state = 2
                i += 1
        elif state == 4:
            if c == ">":
                comment.append(c)
                index_list.append(i)
                state = 0
                i += 1
            else:
                comment.append(c)
                index_list.append(i)
                state = 2
                i += 1
        else:
            i += 1
    for n in index_list[::-1]:
        del listOfCharacters[n]
    for a in comment:
        comments.write(a.encode("utf-8"))
    comments.close()

def removeScripts(listOfCharacters):
    i = 0
    state = 0
    script = []
    index_list = []
    for c in listOfCharacters:
        if state == 0:
            if c == "<":
                script.append(c)
                index_list.append(i)
                state = 1
                i += 1
            else:
                i += 1
        elif state == 1:
            if c == "s":
                script.append(c)
                index_list.append(i)
                state = 2
                i += 1
            else:
                script.pop(len(script)-1)
                index_list.pop(len(index_list)-1)
                state = 0
                i += 1
        elif state == 2:
            if c == "c":
                script.append(c)
                index_list.append(i)
                state = 3
                i += 1
            else:
                script.pop(len(script)-1)
                script.pop(len(script)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                state = 0
                i += 1
        elif state == 3:
            if c == "r":
                script.append(c)
                index_list.append(i)
                state = 4
                i += 1
            else:
                script.pop(len(script)-1)
                script.pop(len(script)-1)
                script.pop(len(script)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                state = 0
                i += 1
        elif state == 4:
            if c == "i":
                script.append(c)
                index_list.append(i)
                state = 5
                i += 1
            else:
                script.pop(len(script)-1)
                script.pop(len(script)-1)
                script.pop(len(script)-1)
                script.pop(len(script)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                state = 0
                i += 1
        elif state == 5:
            if c == "r":
                script.append(c)
                index_list.append(i)
                state = 6
                i += 1
            else:
                script.append(c)
                index_list.append(i)
                i += 1
        elif state == 6:
            if c == "i":
                script.append(c)
                index_list.append(i)
                state = 7
                i += 1
            else:
                script.append(c)
                index_list.append(i)
                state = 5
                i += 1
        elif state == 7:
            if c == "p":
                script.append(c)
                index_list.append(i)
                state = 8
                i += 1
            else:
                script.append(c)
                index_list.append(i)
                state = 5
                i += 1
        elif state == 8:
            if c == "t":
                script.append(c)
                index_list.append(i)
                state = 9
                i += 1
            else:
                script.append(c)
                index_list.append(i)
                state = 5
                i += 1
        elif state == 9:
            if c == ">":
                script.append(c)
                index_list.append(i)
                state = 0
                i += 1
            else:
                script.append(c)
                index_list.append(i)
                state = 5
                i += 1
        else:
            i += 1
    for n in index_list[::-1]:
        del listOfCharacters[n]
    global html
    for a in script:
        scripts.write(a.encode("utf-8"))
    scripts.close()
        
def removeStyles(listOfCharacters):
    i = 0
    state = 0
    style = []
    index_list = []
    for c in listOfCharacters:
        if state == 0:
            if c == "<":
                style.append(c)
                index_list.append(i)
                state = 1
                i += 1
            else:
                i += 1
        elif state == 1:
            if c == "s":
                style.append(c)
                index_list.append(i)
                state = 2
                i += 1
            else:
                style.pop(len(style)-1)
                index_list.pop(len(index_list)-1)
                state = 0
                i += 1
        elif state == 2:
            if c == "t":
                style.append(c)
                index_list.append(i)
                state = 3
                i += 1
            else:
                style.pop(len(style)-1)
                style.pop(len(style)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                state = 0
                i += 1
        elif state == 3:
            if c == "y":
                style.append(c)
                index_list.append(i)
                state = 4
                i += 1
            else:
                style.pop(len(style)-1)
                style.pop(len(style)-1)
                style.pop(len(style)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                state = 0
                i += 1
        elif state == 4:
            if c == "l":
                style.append(c)
                index_list.append(i)
                state = 5
                i += 1
            else:
                style.pop(len(style)-1)
                style.pop(len(style)-1)
                style.pop(len(style)-1)
                style.pop(len(style)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                state = 0
                i += 1
        elif state == 5:
            if c == "t":
                style.append(c)
                index_list.append(i)
                state = 6
                i += 1
            else:
                style.append(c)
                index_list.append(i)
                i += 1
        elif state == 6:
            if c == "y":
                style.append(c)
                index_list.append(i)
                state = 7
                i += 1
            else:
                style.append(c)
                index_list.append(i)
                state = 5
                i += 1
        elif state == 7:
            if c == "l":
                style.append(c)
                index_list.append(i)
                state = 8
                i += 1
            else:
                style.append(c)
                index_list.append(i)
                state = 5
                i += 1
        elif state == 8:
            if c == "e":
                style.append(c)
                index_list.append(i)
                state = 9
                i += 1
            else:
                style.append(c)
                index_list.append(i)
                state = 5
                i += 1
        elif state == 9:
            if c == ">":
                style.append(c)
                index_list.append(i)
                state = 0
                i += 1
            else:
                style.append(c)
                index_list.append(i)
                state = 5
                i += 1
        else:
            i += 1
    for n in index_list[::-1]:
        del listOfCharacters[n]
    for a in style:
        styles.write(a.encode("utf-8"))
    styles.close()

def removeEscapes5(listOfCharacters):
    i = 0
    state = 0
    escape5 = []
    index_list = []
    total = 0
    for c in listOfCharacters:
        if state == 0:
            if c == "&":
                escape5.append(c)
                index_list.append(i)
                state = 1
                i += 1
            else:
                i += 1
        elif state == 1:
                escape5.append(c)
                index_list.append(i)
                state = 2
                i += 1
        elif state == 2:
                escape5.append(c)
                index_list.append(i)
                state = 3
                i += 1
        elif state == 3:
                escape5.append(c)
                index_list.append(i)
                state = 4
                i += 1
        elif state == 4:
            if c == ";":
                escape5.append(c)
                index_list.append(i)
                state = 0
                i += 1
            else:
                escape5.pop(len(escape5)-1)
                escape5.pop(len(escape5)-1)
                escape5.pop(len(escape5)-1)
                escape5.pop(len(escape5)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                state = 0
                i += 1
        else:
            i += 1
    for s in escape5:
        if s == "&":
            total += 1
    for n in index_list[::-1]:
        del listOfCharacters[n]
    for a in escape5:
        escapes.write(a.encode("utf-8"))
    return total

def removeEscapes6(listOfCharacters):
    i = 0
    state = 0
    escape6 = []
    index_list = []
    total = 0
    for c in listOfCharacters:
        if state == 0:
            if c == "&":
                escape6.append(c)
                index_list.append(i)
                state = 1
                i += 1
            else:
                i += 1
        elif state == 1:
                escape6.append(c)
                index_list.append(i)
                state = 2
                i += 1
        elif state == 2:
                escape6.append(c)
                index_list.append(i)
                state = 3
                i += 1
        elif state == 3:
                escape6.append(c)
                index_list.append(i)
                state = 4
                i += 1
        elif state == 4:
                escape6.append(c)
                index_list.append(i)
                state = 5
                i += 1
        elif state == 5:
            if c == ";":
                escape6.append(c)
                index_list.append(i)
                state = 0
                i += 1
            else:
                escape6.pop(len(escape6)-1)
                escape6.pop(len(escape6)-1)
                escape6.pop(len(escape6)-1)
                escape6.pop(len(escape6)-1)
                escape6.pop(len(escape6)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1) 
                index_list.pop(len(index_list)-1)
                index_list.pop(len(index_list)-1)
                state = 0
                i += 1
        else:
            i += 1
    for s in escape6:
        if s == "&":
            total += 1
    for n in index_list[::-1]:
        del listOfCharacters[n]
    for a in escape6:
        escapes.write(a.encode("utf-8"))
    return total

def removeEscapes7(listOfCharacters):
    i = 0
    state = 0
    escape7 = []
    index_list = []
    total = 0
    for c in listOfCharacters:
        if state == 0:
            if c == "&":
                escape7.append(c)
                index_list.append(i)
                state = 1
                i += 1
            else:
                i += 1
        elif state == 1:
                escape7.append(c)
                index_list.append(i)
                state = 2
                i += 1
        elif state == 2:
                escape7.append(c)
                index_list.append(i)
                state = 3
                i += 1
        elif state == 3:
                escape7.append(c)
                index_list.append(i)
                state = 4
                i += 1
        elif state == 4:
                escape7.append(c)
                index_list.append(i)
                state = 5
                i += 1
        elif state == 5:
                escape7.append(c)
                index_list.append(i)
                state = 6
                i += 1
        elif state == 6:
            if c == ";":
                escape7.append(c)
                index_list.append(i)
                state = 0
                i += 1
            else:
                escape7.pop(len(escape7)-1)
                escape7.pop(len(escape7)-1)
                escape7.pop(len(escape7)-1)
                escape7.pop(len(escape7)-1)
                escape7.pop(len(escape7)-1)
                escape7.pop(len(escape7)-1)
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
    for s in escape7:
        if s == "&":
            total += 1
    for n in index_list[::-1]:
        del listOfCharacters[n]
    for a in escape7:
        escapes.write(a.encode("utf-8"))
    return total

def removeEscapes8(listOfCharacters):
    i = 0
    state = 0
    escape8 = []
    index_list = []
    total = 0
    global num
    for c in listOfCharacters:
        if state == 0:
            if c == "&":
                escape8.append(c)
                index_list.append(i)
                state = 1
                i += 1
            else:
                i += 1
        elif state == 1:
                escape8.append(c)
                index_list.append(i)
                state = 2
                i += 1
        elif state == 2:
                escape8.append(c)
                index_list.append(i)
                state = 3
                i += 1
        elif state == 3:
                escape8.append(c)
                index_list.append(i)
                state = 4
                i += 1
        elif state == 4:
                escape8.append(c)
                index_list.append(i)
                state = 5
                i += 1
        elif state == 5:
                escape8.append(c)
                index_list.append(i)
                state = 6
                i += 1
        elif state == 6:
                escape8.append(c)
                index_list.append(i)
                state = 7
                i += 1
        elif state == 7:
            if c == ";":
                escape8.append(c)
                index_list.append(i)
                state = 0
                i += 1
            else:
                escape8.pop(len(escape8)-1)
                escape8.pop(len(escape8)-1)
                escape8.pop(len(escape8)-1)
                escape8.pop(len(escape8)-1)
                escape8.pop(len(escape8)-1)
                escape8.pop(len(escape8)-1)
                escape8.pop(len(escape8)-1)
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
    for s in escape8:
        if s == "&":
            total += 1
    for n in index_list[::-1]:
        del listOfCharacters[n]
    for a in escape8:
        escapes.write(a.encode("utf-8"))
    return total

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
    escapes.close()
    for a in tag:
        tag_.write(a.encode("utf-8"))
    tag_.close()
    for b in nontag:
        nontag_.write(b.encode("utf-8"))
    nontag_.close()
    
#the following is the main part of the program

req = urllib2.Request(raw_input("Enter a URL! \n"), headers={ 'User-Agent': 'Mozilla/5.0' })
target = urllib2.urlopen(req) #getting the source code
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

print "\n", "PLEASE WAIT", "\n"
print "removing comments...", "\n"   
removeComments(text) #comment removal
print "removing scripts...", "\n"
removeScripts(text) #script removal
print "removing styles...", "\n"
removeStyles(text) #style removal
print "extracting html and non-html characters...", "\n" 
htmlSeparate(text) #separating the remaining parts
print "FINISHED! EVERY FILE IS IN THE SAME FOLDER AS THIS SCRIPT."

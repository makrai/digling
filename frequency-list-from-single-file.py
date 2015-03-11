import Tkinter, tkFileDialog

root = Tkinter.Tk()
root.withdraw()

file_path = tkFileDialog.askopenfilename()
text = open(file_path, "r")
text = text.read()
text = text.decode("utf-8")
text = text.replace("\n", " ")
text = text.replace("\r", " ")
text = text.replace("\t", " ")
text = text.split(" ")
words = []
for elem in text:
    if len(elem) > 0:
         words.append(elem.lower())
         
def makeFrequencyList(listOfWords):
    #if you remove this function and paste it into another script
    #please dont forget to decode utf-8 somewhere before this function
    clean = []
    num = []
    for elem in words:
        if elem not in clean:
            clean.append(elem)
            num.append(1)
        else:
            num[clean.index(elem)] += 1      
    frq = zip(clean, num)
    frq.sort(key = lambda x: x[1], reverse=True)
    frequency_list = open("frequency_list.txt", "w")
    for n in range(len(frq)-1):
        a = frq[n][0] + " " + str(frq[n][1]) + "\n"
        a = a.encode("utf-8")
        frequency_list.write(a)
    frequency_list.close()

makeFrequencyList(words)

from tkinter import *
import os
import re

def savetofile():
    text = textinput.get(0.0, END)
    document = titleinput.get(0.0, END)
    with open(os.path.join(re.sub('[^-a-zA-Z0-9_.() ]+', '', document)),"w") as savefile:
        savefile.write(text)

def openfromfile():
    document = openfile.get(0.0, END)
    with open(os.path.join(re.sub('[^-a-zA-Z0-9_.() ]+', '', document)),"r") as savefile:
        text = savefile.read()
    textinput.delete(0.0, END)
    textinput.insert(END, text)
    titleinput.delete(0.0, END)
    titleinput.insert(END, document)

def more():
    morewindow = Tk()
    morewindow.title("More...")


    
    morewindow.mainloop()

titlefont = ("Verdana", 15, "bold")


window = Tk()
window.geometry()
window.config(bg = "#005c5c")
window.title("T editor")
photo1 = PhotoImage(file = "Z:\\Python scripts\\tkinter\\T edit\\logo.png")
window.iconphoto(False, photo1)

title = Label(window, text = "T editor")
title.pack(expand = True)
title.config(font = titlefont, bg = "#005c5c")

textinput = Text(window, height = 50, width = 200, wrap = WORD)
textinput.pack()
textinput.config(bg = "#00a877")

titleinput = Text(window, height = 1, width = 15)
titleinput.pack(side = LEFT, padx = 15)
titleinput.config(bg = "#008585")

savebutton = Button(window, text = "Save", command = savetofile)
savebutton.pack(side = LEFT, padx = 15)
savebutton.config(bg = "#8fbc8f")

openfile = Text(window, height = 1, width = 15)
openfile.pack(side = RIGHT, padx = 15)
openfile.config(bg = "#008585")

openfilebutton = Button(window, text = "Open", command = openfromfile)
openfilebutton.pack(side = RIGHT, padx = 15)
openfilebutton.config(bg = "#8fbc8f")

morebutton = Button(window, text = "More...", command = more)
morebutton.pack(expand = True)
morebutton.config(bg = "#8fbc8f")


window.mainloop()
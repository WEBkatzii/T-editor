from tkinter import *
from tkinter import filedialog
import os
import re
import keyboard

color1 = "#005c5c"
color2 = "#008585"
color3 = "#8fbc8f"
color4 = "#00a877"
textcolor = "#000000"

textfont = ("System", 10)

fontnum = 0

def savetofile():
    text = textinput.get(0.0, END)
    print(filename)
    with open(filename,"w") as savefile:
        savefile.write(text)
    
def saveasfile():
    global filename
    browseFiles()
    print(filename)
    text = textinput.get(0.0, END)
    with open(filename,"w") as savefile:
        savefile.write(text)

def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Devin Text File", "*.dtf*"), ("Text files", "*.txt*"), ("all files", "*.*")))

def openfromfile():
    global filename
    browseFiles()
    print(filename)
    with open(filename,"r") as savefile:
        text = savefile.read()
    textinput.delete(0.0, END)
    textinput.insert(END, text)

def dark():
    global color1, color2, color3, color4, darkbutton, title, textinput, savebutton, themebutton, textcolor
    color1 = "#000000"
    color2 = "#242124"
    color3 = "#3b3c36"
    color4 = "#232b2b"
    textcolor = "#ffffff"
    colorconfig()
    themebutton.config(text = "Light", command = light)

def light():
    global color1, color2, color3, color4, darkbutton, title, textinput, savebutton, themebutton, textcolor
    color1 = "#005c5c"
    color2 = "#008585"
    color3 = "#8fbc8f"
    color4 = "#00a877"
    textcolor = "#000000"
    colorconfig()
    themebutton.config(text = "Dark", command = dark)

def hacker():
    global color1, color2, color3, color4, darkbutton, title, textinput, savebutton, themebutton, textcolor
    color1 = "#000000"
    color2 = "#000000"
    color3 = "#000000"
    color4 = "#000000"
    textcolor = "#00ff00"
    colorconfig()

def colorconfig():
    title.config(font = titlefont, bg = color1, foreground = textcolor)
    textinput.config(bg = color4, foreground = textcolor)
    savebutton.config(bg = color3, foreground = textcolor)
    openfilebutton.config(bg = color3, foreground = textcolor)
    themebutton.config(bg = color3, foreground = textcolor)
    window.config(bg = color1)
    themebutton.config(foreground = textcolor)
    secretbutton.configure(bg = color3, foreground = textcolor)
    saveasbutton.config(bg = color3, foreground = textcolor)
    brackettest.configure(bg = color3, foreground = textcolor)

def nextfont():
    global fontnum, textfont
    fontnum = fontnum + 1
    if fontnum == 1:
        textfont = ("Sylfaen", 10)
    if fontnum == 2:
        textfont = ("Comic Sans MS", 10)
    if fontnum == 3:
        textfont = ("Hanzel Extended", 10)
    if fontnum == 4:
        textfont = ("Roman", 10)
    if fontnum == 5:
        textfont = ("System", 10)
        fontnum = 0
    textinput.config(bg = color4, foreground = textcolor, font = textfont)

def secret():
    global secretwindow
    secretwindow = Tk()
    secretwindow.geometry("350x200")
    secretwindow.config(bg = "#000000")
    secretwindow.title("Secret Settings")

    hackertheme = Button(secretwindow, text = "HACKER", command = hacker, bg = "#000000", foreground = "#00ff00")
    hackertheme.pack(expand = True)

    fontbutton = Button(secretwindow, text = "FONT", command = nextfont, bg = "#000000", foreground = "#00ff00")
    fontbutton.pack(expand = True)

def exitkey():
    global secretwindow, window
    window.destroy()
    secretwindow.destroy()
    exit()

def disable_event():
   pass

def brackettester():
    text = textinput.get(0.0, END)
    brackets = -1
    bracket = "("
    #I don't know why, but also finds )
    for bracket in text:
        brackets = brackets + 1
    if (brackets % 2) == 0:
        print("All Brackets are closed")
        brackettest.configure(text = "All Brackets are closed!")
    else:
        print("Not all Brackets are closed")
        brackettest.configure(text = "Not all Brackets are closed!")
    print(brackets)


titlefont = ("Verdana", 15, "bold")


window = Tk()
window.geometry()
window.config(bg = color1)
window.title("T editor")
photo1 = PhotoImage(file = "Z:\\Python scripts\\tkinter\\T editor\\logo.dpf")
window.iconphoto(False, photo1)

title = Label(window, text = "T editor")
title.pack(expand = True)
title.config(font = titlefont, bg = color1)

textinput = Text(window, height = 50, width = 200, wrap = WORD)
textinput.pack(expand = True)
textinput.config(bg = color4, foreground = textcolor, font = textfont)

savebutton = Button(window, text = "Save", command = savetofile)
savebutton.pack(side = LEFT, padx = 15)
savebutton.config(bg = color3, foreground = textcolor)

saveasbutton = Button(window, text = "Save as", command = saveasfile)
saveasbutton.pack(side = LEFT, padx = 15)
saveasbutton.config(bg = color3, foreground = textcolor)              

openfilebutton = Button(window, text = "Open", command = openfromfile)
openfilebutton.pack(side = RIGHT, padx = 15)
openfilebutton.config(bg = color3, foreground = textcolor)

themebutton = Button(window, text = "Dark", command = dark)
themebutton.pack(expand = True, side = LEFT, pady = 10)
themebutton.config(bg = color3, foreground = textcolor)

secretbutton = Button(window, text = "Secret...", command = secret)
secretbutton.pack(expand = True, side = RIGHT, pady = 10)
secretbutton.configure(bg = color3, foreground = textcolor)

brackettest = Button(window, text = "Bracket Test", command = brackettester)
brackettest.pack(expand = True, side = RIGHT, pady = 10)
brackettest.configure(bg = color3, foreground = textcolor)

keyboard.add_hotkey('ctrl+c+.+w', lambda: savetofile())

keyboard.add_hotkey('ctrl+c+.+r', lambda: openfromfile())

keyboard.add_hotkey('ctrl+c+.+alt', lambda: exitkey())

keyboard.add_hotkey('ctrl+c+.+b', lambda: brackettester())

window.protocol("WM_DELETE_WINDOW", disable_event)

window.mainloop()
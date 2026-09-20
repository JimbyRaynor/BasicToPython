import os
from tkinter import *

# for loading files (.png, .txt), set current directory = location of this python script (needed for Linux)
current_script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_script_directory)

mainwin = Tk()
mainwin.geometry("1000x1000")
textbox1 = Text(mainwin,width=120,height=40)
textbox1.place(x=10,y=10)


InFile = "basketball.bas"

linenumlist = []
proglist = []

myfile = open(InFile)
for line in myfile:
    sp = line.find(' ')
    linenum = line[0:sp]
    linenumlist.append(linenum)
    proglist.append(line)
myfile.close()

for i,line in enumerate(proglist):
    linenum = linenumlist[i]
    line = proglist[i]
    if i < len(proglist)-1:
        nextlinenum = linenumlist[i+1]
    textbox1.insert(INSERT,"\n")
    textbox1.insert(INSERT,"def line_"+linenum+"(state)\n")
    textbox1.insert(INSERT,"    print('"+line[0:len(line)-2]+"')\n")
    textbox1.insert(INSERT,'return "'+nextlinenum+'"\n')
    textbox1.insert(INSERT,"\n")

textbox1.insert(INSERT,"program = {")
for num in linenumlist:
    textbox1.insert(INSERT,'"'+num+'": line_'+num+',\n')
textbox1.insert(INSERT,"}\n")


textbox1.insert(INSERT,'state = {"B": 0}\n')

textbox1.insert(INSERT,'line = "'+linenumlist[0]+'"\n')
textbox1.insert(INSERT,'while line:\n')
textbox1.insert(INSERT,'    line = program[line](state)')


def copyall():
    selectedtext = textbox1.get("1.0","end-1c")
    mainwin.clipboard_clear()
    mainwin.clipboard_append(selectedtext)

btnCopy = Button(mainwin,text = "Copy All", command = copyall)
btnCopy.place(x=10,y=700)    

mainwin.mainloop()
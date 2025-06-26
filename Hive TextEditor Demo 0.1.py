from tkinter import *
from tkinter import filedialog
from tkinter import Tk, Label



window = Tk()
root = Tk()
file = None
window.bind()

#Define
def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML file", ".html"),
                                        ("XML file",".xml"),
                                        ("BATCH file",".bat"),
                                        ("DOCS file",".docx"),
                                        ("All files", ".*"),
                                    ])
    if file is None:
        return
    filetext = str(text.get(1.0,END))
    #filetext = input("Enter some text I guess: ") //use this if you want to use console window
    file.write(filetext)
    file.close()
   
   
        
        
#main
text = Text(window, height=29, bg="#012456", bd=15, width=42)
text.pack()

button = Button(window, text="OFF", bg="red", bd=5.3, fg="white", command=quit).place(x=20, y=1500)

button = Button(window, text="SaveFile",command=saveFile, bg="#ada6a6", bd=4.44, fg="black").place(x=220, y=1500)

button = Button(window, text="Copy", bg="#ada6a6", bd=4.44, fg="black",).place(x=493, y=1500)



frame = Frame(window,bg="#012456",bd=5,relief=SUNKEN)
frame.place(x=100, y=2001)
    
Button(frame, text="1",bg="#ada6a6",fg="white").pack(side=LEFT)
Button(frame,text="2",bg="#ada6a6",fg="white").pack(side=LEFT)
Button(frame,text="3",bg="#ada6a6",fg="white").pack(side=LEFT)



label= Label(window, text="ver.0.1.0", fg="yellow", bg="#012456", font=("Roboto, 6")).place(x=70, y=1304)


menubar = Menu(window)
filemenu = Menu(menubar)







#configs
text.config(fg="white")
window.config(menu=menubar)

window.config(menu=menubar, bg="#b8b2b2")


#menubar
menubar = Menu(window)



# run
window.mainloop()
root.mainloop()

from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("MindBlowing")
root.iconbitmap("C:/tkinter testing/mindblown-mindblowing.ico")


pic0 = ImageTk.PhotoImage(Image.open("C:/tkinter testing/peguin.png"))
pic1 = ImageTk.PhotoImage(Image.open("C:/tkinter testing/grass-4149340_1920.png"))
mylabel = Label(image=pic0).pack()

Imagelist = (pic0 , pic1)

def myClick():
    mylabel = Label(root,text ="I TOLD YOU DO NOT CLICK IT!!",fg="red").pack()

def forward():
    return

def back():
    return
 
    
mylabel1 = Label(root,text = "MindBlowing").pack()
e = Entry(root,width=50).pack()
mybutton1 = Button(root,text = "Don't Click" , command = myClick , fg="cyan" , bg="red").pack()
Quitbutton = Button(root,text = "Quit this" , command=root.quit).pack()
buttonBack = Button(root,text = "<<" , command = back).pack()
buttonForward = Button(root,text = ">>" , command = forward).pack()


root.mainloop()


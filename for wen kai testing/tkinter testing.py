from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("MindBlowing")
root.iconbitmap("./mindblown-mindblowing.ico")
root.geometry("800x500")





pic0 = ImageTk.PhotoImage(Image.open("./peguin.png"))
pic1 = ImageTk.PhotoImage(Image.open("./grass-4149340_1920.png"))
bg = PhotoImage(file = "./grass-4149340_1920.png")
mylabel = Label(image=bg).pack()



Imagelist = (pic0 , pic1)

def myClick():
    mylabel = Label(root,text ="I TOLD YOU DO NOT CLICK IT!!",fg="red").place(x=500 , y=150)

def forward(image_number):
    global mylabel
    global buttonForward
    global buttonBack

    
    

def back():
    return
 
    
mylabel1 = Label(root,text = "MindBlowing").place(x=600 , y=0)
e = Entry(root,width=50).place(x=490 , y=30)
mybutton1 = Button(root,text = "Don't Click" , command = myClick , fg="cyan" , bg="red").place(x=0 , y=0)
Quitbutton = Button(root,text = "Quit this" , command=root.quit).place(x=1225 , y=0)
buttonBack = Button(root,text = "<<" , command = back).place(x=600 , y=100)
buttonForward = Button(root,text = ">>" , command = lambda : forward(2)).place(x=650 , y=99)

root.mainloop()


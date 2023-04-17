from tkinter import*
from tkinter.ttk import*
from time import strftime
root=Tk()
root.title("Digital Clock")
def clock():
    string=strftime('%I:%M:%S:%p')
    label.config(text=string)
    label.after(1000,clock)

label=Label(root, font = ("Digital-7",100),background='black', foreground='yellow')
label.pack(anchor='center')
clock()
root.mainloop()



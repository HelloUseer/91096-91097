import tkinter as tk #short cut#
from tkinter import * #importing everything from tkinter#
from tkinter import ttk #importing ttk from tkinter#

window = tk.Tk()
window.title("Book Inventory V1.0")
window.geometry("960x540")#640x360,*1.5#

#Creating frame#
frame=tk.Frame(window,bg="#dae8fc")
frame.pack(fill="both",expand=True)#using fill and expand to cover whole window#

#Title#
heading = tk.Label(frame,bg="#dae8fc",font=("Arial",36),text="Library Book Finder")
heading.place(x=280,y=100)

#Text introducing the user to program, need to add {username.get()} when login frame is created#
introtxt = tk.Label(frame,bg="#dae8fc",font=("Arial",22),text="Username, welcome to library!\nView what books are available today\nHappy Reading!",justify="left")#Justify is to make text align to the left#
introtxt.place(x=175,y=200)

#Log out button#
lgoutbtn = tk.Button(frame,fg="white",bg="#1ba1e2",font=("Arial",22),text="Log Out")
lgoutbtn.place(x=100,y=400)

#Close program button#
clsprgrmbtn = tk.Button(frame,fg="white",bg="#1ba1e2",font=("Arial",22),text="Close")
clsprgrmbtn.place(x=300,y=400)

#Continue button#
ctnbtn = tk.Button(frame,fg="white",bg="#1ba1e2",font=("Arial",22),text="Continue")
ctnbtn.place(x=700,y=400)

window.mainloop()

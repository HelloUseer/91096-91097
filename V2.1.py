import tkinter as tk #Short cut#
from tkinter import * #Importing everything from tkinter#
from tkinter import ttk #Importing ttk from tkinter#
from tkinter import messagebox as mb #Shortcut for messagebox#

window = tk.Tk()
window.title("Book Inventory V2.0")
window.geometry("960x540")#640x360,*1.5#

#Simple username and passwords#
username = ["Bookwormz","Bibliomania","bookery"]
password = ["abcd1234","pswdfgot1","bookz999"]

#Creating login frame#
lgnframe=tk.Frame(window,bg="#cae8fc")
lgnframe.pack(fill="both",expand=True)#fill mean colouring in, both meaning in both verticle and horizontal direction#
#expand take as much space as possible, but without fill will not be coloured in#

#Creating detail frame#
dtlframe=tk.Frame(window,bg="#dae8fc")
dtlframe.pack(fill="both",expand=True)#using fill and expand to cover whole window#

#Creating book type frame#
bktpframe=tk.Frame(window,bg="#dae8fc")
bktpframe.pack(fill="both",expand=True)

#Showing login frame#
def login_frame():
    lgnframe.pack(fill="both",expand=True)
    dtlframe.pack_forget()
    bktpframe.pack_forget()

#Showing detail frame#
def detail_frame():
    lgnframe.pack_forget()
    dtlframe.pack(fill="both",expand=True)
    bktpframe.pack_forget()

#Showing book type frame#
def bktp_frame():
    lgnframe.pack_forget()
    dtlframe.pack_forget()
    bktpframe.pack(fill="both",expand=True)
    
#Checking username and password#
def usrnm_chk():
    usrnm = usrnmentry.get()#Getting the username user has entered#
    if usrnm == "":#If username is empty#
        mb.showwarning("Username?","Username has been left empty")#Message box warning#
    elif usrnm in username:#If user's username exists in list#
        pswd = pswdentry.get()#Getting the password user has entered#
        if pswd == "":#If password is empty#
            mb.showwarning("Password?","Password has been left empty")#Message box warning#
        elif pswd in password:#If user's password exists in list#
            usr_usrnm = username.index(usrnm)#Finding index number of user's username#
            if pswd == password[usr_usrnm]:#When user given password match password of username's index number#
                detail_frame()#Go to detail frame#
            else:
                mb.showwarning("Password Incorrect","Please check your password")#Message box warning#
        else:
            mb.showwarning("Password Incorrect","Please check your password")#Message box warning#
    else:
        mb.showwarning("Username Incorrect","Please check your username")#Message box warning#
    
#Show login frame only at beginning of program#
login_frame()

#Widgets for login frame#

#Heading on login frame#
heading = tk.Label(lgnframe,bg="#dae8fc",font=("Arial",36),text="Library Book Finder")
heading.place(x=280,y=100)

#Username label#
usrnmlbl = tk.Label(lgnframe,bg="#dae8fc",font=("Arial",20),text="Username")
usrnmlbl.place(x=300,y=220)

#Username entry box#
usrnmentry = tk.Entry(lgnframe,bg="#dae8fc")
usrnmentry.place(x=525,y=220)

#Password label#
pswdlbl = tk.Label(lgnframe,bg="#dae8fc",font=("Arial",20),text="Password")
pswdlbl.place(x=300,y=280)

#Password entry box#
pswdentry = tk.Entry(lgnframe,bg="#dae8fc")
pswdentry.place(x=525,y=280)

#Close Button#
clsbtn = tk.Button(lgnframe,fg="white",bg="#1ba1e2",font=("Arial",22),text="Close")
clsbtn.place(x=100,y=400)

#Login button#
lgnbtn = tk.Button(lgnframe,fg="white",bg="#1ba1e2",font=("Arial",22),text="Log In",command=usrnm_chk)
lgnbtn.place(x=750,y=400)

#Widgets for detail frame#

#Title on detail frame#
heading = tk.Label(dtlframe,bg="#dae8fc",font=("Arial",36),text="Library Book Finder")
heading.place(x=280,y=100)

#Text introducing the user to program, need to add {username.get()} when login frame is created#
introtxt = tk.Label(dtlframe,bg="#dae8fc",font=("Arial",22),text=f"{usrnmentry.get()}, welcome to library!\nView what books are available today\nHappy Reading!",justify="left")#Justify is to make text align to the left#
introtxt.place(x=175,y=200)

#Log out button#
lgoutbtn = tk.Button(dtlframe,fg="white",bg="#1ba1e2",font=("Arial",22),text="Log Out",command=login_frame)
lgoutbtn.place(x=100,y=400)#Plan to make show username work when used with classes, now widgets are created earlier than username being inputed#

#Close program button#
clsprgrmbtn = tk.Button(dtlframe,fg="white",bg="#1ba1e2",font=("Arial",22),text="Close")
clsprgrmbtn.place(x=300,y=400)

#Continue button#
ctnbtn = tk.Button(dtlframe,fg="white",bg="#1ba1e2",font=("Arial",22),text="Continue",command=bktp_frame)
ctnbtn.place(x=700,y=400)

#Widgets for book type frame#

#Label types of books#
tpsofbkslbl = tk.Label(bktpframe,bg="#dae8fc",font=("Arial",36),text="Types of Books")
tpsofbkslbl.place(x=325,y=50)

#Fictions Button#
fctionbtn = tk.Button(bktpframe,fg="white",bg="#1ba1e2",font=("Arial",22),text="Fiction",width=15)
fctionbtn.place(x=200,y=150)

#Non Fiction Button#
nnfctionbtn = tk.Button(bktpframe,fg="white",bg="#1ba1e2",font=("Arial",22),text="Non Fictions",width=15)
nnfctionbtn.place(x=500,y=150)

#Childrens Button#
chldrnbtn = tk.Button(bktpframe,fg="white",bg="#1ba1e2",font=("Arial",22),text="Childrens",width=15)
chldrnbtn.place(x=200,y=250)

#Encyclopedia Button#
encyclpdabtn = tk.Button(bktpframe,fg="white",bg="#1ba1e2",font=("Arial",22),text="Encyclopedias",width=15)
encyclpdabtn.place(x=500,y=250)

#Historical Fiction Button#
hstriclbtn = tk.Button(bktpframe,fg="white",bg="#1ba1e2",font=("Arial",22),text="Historical",width=15)
hstriclbtn.place(x=200,y=350)

#Science Fiction Button#
scifcbtn = tk.Button(bktpframe,fg="white",bg="#1ba1e2",font=("Arial",22),text="Science Fiction",width=15)
scifcbtn.place(x=500,y=350)

window.mainloop()

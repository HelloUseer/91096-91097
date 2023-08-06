import tkinter as tk #Short cut#
from tkinter import * #Importing everything from tkinter#
from tkinter import ttk #Importing ttk from tkinter#
from tkinter import messagebox as mb #Shortcut for messagebox#
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Book Inventory V2.3")
window.geometry("960x540")#640x360,*1.5#

#Simple username and passwords, put in order so that each username and its password has#
username = ["Bookwormz","Bibliomania","bookery"]
password = ["abcd1234","pswdfgot1","bookz999"]

#Starting Number Of Available Books#
fb1 = 1
fb2 = 1
fb3 = 1
fb4 = 1
nb1 = 1
nb2 = 1
nb3 = 1
nb4 = 1
cb1 = 1
cb2 = 1
cb3 = 1
cb4 = 1
eb1 = 1
eb2 = 1
eb3 = 1
eb4 = 1
hb1 = 1
hb2 = 1
hb3 = 1
hb4 = 1
sb1 = 1
sb2 = 1
sb3 = 1
sb4 = 1

#Creating login frame#
lgnframe=tk.Frame(window,bg="#dae8fc")
lgnframe.pack(fill="both",expand=True)#fill mean colouring in, both meaning in both verticle and horizontal direction#
#expand take as much space as possible, but without fill will not be coloured in#

#Creating detail frame#
dtlframe=tk.Frame(window,bg="#dae8fc")
dtlframe.pack(fill="both",expand=True)#using fill and expand to cover whole window#

#Creating book type frame#
bktpframe=tk.Frame(window,bg="#dae8fc")
bktpframe.pack(fill="both",expand=True)

#Creating Fiction book frame#
fictionframe=tk.Frame(window,bg="#dae8fc")
fictionframe.pack(fill="both",expand=True)

#Creating Nonfiction bookframe#
nonfictionframe=tk.Frame(window,bg="#dae8fc")
nonfictionframe.pack(fill="both",expand=True)

#Creating Children book frame#
childrenframe=tk.Frame(window,bg="#dae8fc")
childrenframe.pack(fill="both",expand=True)

#Creating Encyclopedia book frame#
encyclopediaframe=tk.Frame(window,bg="#dae8fc")
encyclopediaframe.pack(fill="both",expand=True)

#Creating Historical fiction book frame#
historicalframe=tk.Frame(window,bg="#dae8fc")
historicalframe.pack(fill="both",expand=True)

#Creating Science Fiction book frame#
scififrame=tk.Frame(window,bg="#dae8fc")
scififrame.pack(fill="both",expand=True)

#Fiction books#

#Creating Fiction book 1 frame#
fframeb1=tk.Frame(window,bg="#dae8fc")
fframeb1.pack(fill="both",expand=True)

#Creating Fiction book 2 frame#
fframeb2=tk.Frame(window,bg="#dae8fc")
fframeb2.pack(fill="both",expand=True)

#Creating Fiction book 3 frame#
fframeb3=tk.Frame(window,bg="#dae8fc")
fframeb3.pack(fill="both",expand=True)

#Creating Fiction book 4 frame#
fframeb4=tk.Frame(window,bg="#dae8fc")
fframeb4.pack(fill="both",expand=True)

#Non Fiction books#

#Creating Non Fiction book 1 frame#
nframeb1=tk.Frame(window,bg="#dae8fc")
nframeb1.pack(fill="both",expand=True)

#Creating Non Fiction book 2 frame#
nframeb2=tk.Frame(window,bg="#dae8fc")
fframeb2.pack(fill="both",expand=True)

#Creating Non Fiction book 3 frame#
nframeb3=tk.Frame(window,bg="#dae8fc")
nframeb3.pack(fill="both",expand=True)

#Creating Non Fiction book 4 frame#
nframeb4=tk.Frame(window,bg="#dae8fc")
nframeb4.pack(fill="both",expand=True)

#Children books#

#Creating Children book 1 frame#
cframeb1=tk.Frame(window,bg="#dae8fc")
cframeb1.pack(fill="both",expand=True)

#Creating Children book 2 frame#
cframeb2=tk.Frame(window,bg="#dae8fc")
cframeb2.pack(fill="both",expand=True)

#Creating Children book 3 frame#
cframeb3=tk.Frame(window,bg="#dae8fc")
cframeb3.pack(fill="both",expand=True)

#Creating Children book 4 frame#
cframeb4=tk.Frame(window,bg="#dae8fc")
cframeb4.pack(fill="both",expand=True)

#Encyclopedias#

#Creating Encyclopedia book 1 frame#
eframeb1=tk.Frame(window,bg="#dae8fc")
eframeb1.pack(fill="both",expand=True)

#Creating Encyclopedia book 2 frame#
eframeb2=tk.Frame(window,bg="#dae8fc")
eframeb2.pack(fill="both",expand=True)

#Creating Encyclopedia book 3 frame#
eframeb3=tk.Frame(window,bg="#dae8fc")
eframeb3.pack(fill="both",expand=True)

#Creating Encyclopedia book 4 frame#
eframeb4=tk.Frame(window,bg="#dae8fc")
eframeb4.pack(fill="both",expand=True)

#Historical Fiction books#

#Creating Historical Fiction book 1 frame#
hframeb1=tk.Frame(window,bg="#dae8fc")
hframeb1.pack(fill="both",expand=True)

#Creating Historical Fiction book 2 frame#
hframeb2=tk.Frame(window,bg="#dae8fc")
hframeb2.pack(fill="both",expand=True)

#Creating Historical Fiction book 3 frame#
hframeb3=tk.Frame(window,bg="#dae8fc")
hframeb3.pack(fill="both",expand=True)

#Creating Historical Fiction book 4 frame#
hframeb4=tk.Frame(window,bg="#dae8fc")
hframeb4.pack(fill="both",expand=True)

#Science Fiction books#

#Creating Science Fiction book 1 frame#
sframeb1=tk.Frame(window,bg="#dae8fc")
sframeb1.pack(fill="both",expand=True)

#Creating Science Fiction book 2 frame#
sframeb2=tk.Frame(window,bg="#dae8fc")
sframeb2.pack(fill="both",expand=True)

#Creating Science Fiction book 3 frame#
sframeb3=tk.Frame(window,bg="#dae8fc")
sframeb3.pack(fill="both",expand=True)

#Creating Science Fiction book 4 frame#
sframeb4=tk.Frame(window,bg="#dae8fc")
sframeb4.pack(fill="both",expand=True)

#Editing number of books available#

#Creating Qty frame for Fiction book 1#
fic1dtl=tk.Frame(window,bg="#dae8fc")
fic1dtl.pack(fill="both",expand=True)

#Creating Qty frame for Fiction book 2#
fic2dtl=tk.Frame(window,bg="#dae8fc")
fic2dtl.pack(fill="both",expand=True)

#Creating Qty frame for Fiction book 3#
fic3dtl=tk.Frame(window,bg="#dae8fc")
fic3dtl.pack(fill="both",expand=True)

#Creating Qty frame for Fiction book 4#
fic4dtl=tk.Frame(window,bg="#dae8fc")
fic4dtl.pack(fill="both",expand=True)

#Creating Qty frame for Non Fiction book 1#
non1dtl=tk.Frame(window,bg="#dae8fc")
non1dtl.pack(fill="both",expand=True)

#Creating Qty frame for Non Fiction book 2#
non2dtl=tk.Frame(window,bg="#dae8fc")
non2dtl.pack(fill="both",expand=True)

#Creating Qty frame for Non Fiction book 3#
non3dtl=tk.Frame(window,bg="#dae8fc")
non3dtl.pack(fill="both",expand=True)

#Creating Qty frame for Non Fiction book 4#
non4dtl=tk.Frame(window,bg="#dae8fc")
non4dtl.pack(fill="both",expand=True)

#Creating Qty frame for Children book 1#
chi1dtl=tk.Frame(window,bg="#dae8fc")
chi1dtl.pack(fill="both",expand=True)

#Creating Qty frame for Children book 2#
chi2dtl=tk.Frame(window,bg="#dae8fc")
chi2dtl.pack(fill="both",expand=True)

#Creating Qty frame for Children book 3#
chi3dtl=tk.Frame(window,bg="#dae8fc")
chi3dtl.pack(fill="both",expand=True)

#Creating Qty frame for Children book 4#
chi4dtl=tk.Frame(window,bg="#dae8fc")
chi4dtl.pack(fill="both",expand=True)

#Creating Qty frame for Encyclopedia book 1#
enc1dtl=tk.Frame(window,bg="#dae8fc")
enc1dtl.pack(fill="both",expand=True)

#Creating Qty frame for Encyclopedia book 2#
enc2dtl=tk.Frame(window,bg="#dae8fc")
enc2dtl.pack(fill="both",expand=True)

#Creating Qty frame for Encyclopedia book 3#
enc3dtl=tk.Frame(window,bg="#dae8fc")
enc3dtl.pack(fill="both",expand=True)

#Creating Qty frame for Encyclopedia book 4#
enc4dtl=tk.Frame(window,bg="#dae8fc")
enc4dtl.pack(fill="both",expand=True)

#Creating Qty frame for Historical Fiction book 1#
his1dtl=tk.Frame(window,bg="#dae8fc")
his1dtl.pack(fill="both",expand=True)

#Creating Qty frame for Historical Fiction book 2#
his2dtl=tk.Frame(window,bg="#dae8fc")
his2dtl.pack(fill="both",expand=True)

#Creating Qty frame for Historical Fiction book 3#
his3dtl=tk.Frame(window,bg="#dae8fc")
his3dtl.pack(fill="both",expand=True)

#Creating Qty frame for Historical Fiction book 4#
his4dtl=tk.Frame(window,bg="#dae8fc")
his4dtl.pack(fill="both",expand=True)

#Creating Qty frame for Science Fiction book 1#
sci1dtl=tk.Frame(window,bg="#dae8fc")
sci1dtl.pack(fill="both",expand=True)

#Creating Qty frame for Science Fiction book 2#
sci2dtl=tk.Frame(window,bg="#dae8fc")
sci2dtl.pack(fill="both",expand=True)

#Creating Qty frame for Science Fiction book 3#
sci3dtl=tk.Frame(window,bg="#dae8fc")
sci3dtl.pack(fill="both",expand=True)

#Creating Qty frame for Science Fiction book 4#
sci4dtl=tk.Frame(window,bg="#dae8fc")
sci4dtl.pack(fill="both",expand=True)

def no_frame():
    lgnframe.pack_forget()
    dtlframe.pack_forget()
    bktpframe.pack_forget()
    fictionframe.pack_forget()
    nonfictionframe.pack_forget()
    childrenframe.pack_forget()
    encyclopediaframe.pack_forget()
    historicalframe.pack_forget()
    scififrame.pack_forget()
    fframeb1.pack_forget()
    fframeb2.pack_forget()
    fframeb3.pack_forget()
    fframeb4.pack_forget()
    nframeb1.pack_forget()
    nframeb2.pack_forget()
    nframeb3.pack_forget()
    nframeb4.pack_forget()
    cframeb1.pack_forget()
    cframeb2.pack_forget()
    cframeb3.pack_forget()
    cframeb4.pack_forget()
    eframeb1.pack_forget()
    eframeb2.pack_forget()
    eframeb3.pack_forget()
    eframeb4.pack_forget()
    hframeb1.pack_forget()
    hframeb2.pack_forget()
    hframeb3.pack_forget()
    hframeb4.pack_forget()
    sframeb1.pack_forget()
    sframeb2.pack_forget()
    sframeb3.pack_forget()
    sframeb4.pack_forget()
    fic1dtl.pack_forget()
    fic2dtl.pack_forget()
    fic3dtl.pack_forget()
    fic4dtl.pack_forget()
    non1dtl.pack_forget()
    non2dtl.pack_forget()
    non3dtl.pack_forget()
    non4dtl.pack_forget()
    chi1dtl.pack_forget()
    chi2dtl.pack_forget()
    chi3dtl.pack_forget()
    chi4dtl.pack_forget()
    enc1dtl.pack_forget()
    enc2dtl.pack_forget()
    enc3dtl.pack_forget()
    enc4dtl.pack_forget()
    his1dtl.pack_forget()
    his2dtl.pack_forget()
    his3dtl.pack_forget()
    his4dtl.pack_forget()
    sci1dtl.pack_forget()
    sci2dtl.pack_forget()
    sci3dtl.pack_forget()
    sci4dtl.pack_forget()

#Showing login frame#
def login_frame():
    no_frame()
    lgnframe.pack(fill="both",expand=True)

#Showing detail frame#
def detail_frame():
    no_frame()
    dtlframe.pack(fill="both",expand=True)

#Showing book type frame#
def bktp_frame():
    no_frame()
    bktpframe.pack(fill="both",expand=True)

#Books in Fiction frame#
def fiction_frame():
    no_frame()
    fictionframe.pack(fill="both",expand=True)

#Books in Nonfiction frame#
def nonfiction_frame():
    no_frame()
    nonfictionframe.pack(fill="both",expand=True)

#Books in Childrens frame#
def children_frame():
    no_frame()
    childrenframe.pack(fill="both",expand=True)
    
#Books in Encyclopedia frame#
def encyclopedia_frame():
    no_frame()
    encyclopediaframe.pack(fill="both",expand=True)
    
#Books in Historical frame#
def historical_frame():
    no_frame()
    historicalframe.pack(fill="both",expand=True)
    
#Books in Science Fiction frame#
def scifi_frame():
    no_frame()
    scififrame.pack(fill="both",expand=True)

#Books Detail Of Fiction frame#
def fbook1_frame():
    no_frame()
    fframeb1.pack(fill="both",expand=True)

def fbook2_frame():
    no_frame()
    fframeb2.pack(fill="both",expand=True)

def fbook3_frame():
    no_frame()
    fframeb3.pack(fill="both",expand=True)

def fbook4_frame():
    no_frame()
    fframeb4.pack(fill="both",expand=True)

#Books Detail of Non Fiction frame#
def nbook1_frame():
    no_frame()
    nframeb1.pack(fill="both",expand=True)

def nbook2_frame():
    no_frame()
    nframeb2.pack(fill="both",expand=True)

def nbook3_frame():
    no_frame()
    nframeb3.pack(fill="both",expand=True)

def nbook4_frame():
    no_frame()
    nframeb4.pack(fill="both",expand=True)

#Books Detail of Children frame#
def cbook1_frame():
    no_frame()
    cframeb1.pack(fill="both",expand=True)

def cbook2_frame():
    no_frame()
    cframeb2.pack(fill="both",expand=True)

def cbook3_frame():
    no_frame()
    cframeb3.pack(fill="both",expand=True)

def cbook4_frame():
    no_frame()
    cframeb4.pack(fill="both",expand=True)

#Books Detail of Encyclopediaa frame#
def ebook1_frame():
    no_frame()
    eframeb1.pack(fill="both",expand=True)

def ebook2_frame():
    no_frame()
    eframeb2.pack(fill="both",expand=True)

def ebook3_frame():
    no_frame()
    eframeb3.pack(fill="both",expand=True)

def ebook4_frame():
    no_frame()
    eframeb4.pack(fill="both",expand=True)

#Books Detail of Historical Fiction frame#
def hbook1_frame():
    no_frame()
    hframeb1.pack(fill="both",expand=True)

def hbook2_frame():
    no_frame()
    hframeb2.pack(fill="both",expand=True)

def hbook3_frame():
    no_frame()
    hframeb3.pack(fill="both",expand=True)

def hbook4_frame():
    no_frame()
    hframeb4.pack(fill="both",expand=True)

#Books Detail of Science Fiction frame#
def sbook1_frame():
    no_frame()
    sframeb1.pack(fill="both",expand=True)

def sbook2_frame():
    no_frame()
    sframeb2.pack(fill="both",expand=True)

def sbook3_frame():
    no_frame()
    sframeb3.pack(fill="both",expand=True)

def sbook4_frame():
    no_frame()
    sframeb4.pack(fill="both",expand=True)

def f1dtl_frame():
    no_frame()
    fic1dtl.pack(fill="both",expand=True)

def f2dtl_frame():
    no_frame()
    fic2dtl.pack(fill="both",expand=True)

def f3dtl_frame():
    no_frame()
    fic3dtl.pack(fill="both",expand=True)

def f4dtl_frame():
    no_frame()
    fic4dtl.pack(fill="both",expand=True)

#Show login frame only at beginning of program#
no_frame()
login_frame()
    
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

#Widgets for login frame#

#Heading on login frame#
heading = tk.Label(lgnframe,bg="#dae8fc",font=("Arial",36),text="Library Book Finder")
heading.place(x=280,y=100)

#Username label#
usrnmlbl = tk.Label(lgnframe,bg="#dae8fc",font=("Arial",20),text="Username")
usrnmlbl.place(x=300,y=220)

#Username entry box#
usrnmentry = tk.Entry(lgnframe,bg="white")
usrnmentry.place(x=525,y=220)

#Password label#
pswdlbl = tk.Label(lgnframe,bg="#dae8fc",font=("Arial",20),text="Password")
pswdlbl.place(x=300,y=280)

#Password entry box#
pswdentry = tk.Entry(lgnframe,bg="white")
pswdentry.place(x=525,y=280)

#Close Button#
clsbtn = tk.Button(lgnframe,fg="white",bg="#1ba1e2",font=("Arial",22),text="Close")
clsbtn.place(x=100,y=400)

#Login button#
lgnbtn = tk.Button(lgnframe,fg="white",bg="#1ba1e2",font=("Arial",22),text="Log In",command=usrnm_chk)
lgnbtn.place(x=750,y=400)

#Widgets for detail frame#

#Title on detail frame#
ttle = tk.Label(dtlframe,bg="#dae8fc",font=("Arial",36),text="Library Book Finder")
ttle.place(x=280,y=100)

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
fctionbtn = tk.Button(bktpframe,fg="white",bg="#1ba1e2",font=("Arial",22),text="Fiction",width=15,command=fiction_frame)
fctionbtn.place(x=200,y=150)

#Non Fiction Button#
nnfctionbtn = tk.Button(bktpframe,fg="white",bg="#1ba1e2",font=("Arial",22),text="Non Fictions",width=15,command=nonfiction_frame)
nnfctionbtn.place(x=500,y=150)

#Childrens Button#
chldrnbtn = tk.Button(bktpframe,fg="white",bg="#1ba1e2",font=("Arial",22),text="Childrens",width=15,command=children_frame)
chldrnbtn.place(x=200,y=250)

#Encyclopedia Button#
encyclpdabtn = tk.Button(bktpframe,fg="white",bg="#1ba1e2",font=("Arial",22),text="Encyclopedias",width=15,command=encyclopedia_frame)
encyclpdabtn.place(x=500,y=250)

#Historical Fiction Button#
hstriclbtn = tk.Button(bktpframe,fg="white",bg="#1ba1e2",font=("Arial",22),text="Historical Fiction",width=15,command=historical_frame)
hstriclbtn.place(x=200,y=350)

#Science Fiction Button#
scifcbtn = tk.Button(bktpframe,fg="white",bg="#1ba1e2",font=("Arial",22),text="Science Fiction",width=15,command=scifi_frame)
scifcbtn.place(x=500,y=350)

#Widgets for Fiction books and many other books frame#

#Fiction frame name#
bksinfiction = tk.Label(fictionframe,bg="#dae8fc",font=("Arial",32),text="Types Of Books In Fiction")
bksinfiction.place(x=225,y=25)

#Book title 1#
titlelbl1 = tk.Label(fictionframe,bg="#dae8fc",font=("Arial",18),text="The Broken Raven")
titlelbl1.place(x=220,y=100)

#Book title 2#
titlelbl2 = tk.Label(fictionframe,bg="#dae8fc",font=("Arial",18),text="The War Hero")
titlelbl2.place(x=620,y=100)

#Book title 3#
titlelbl3 = tk.Label(fictionframe,bg="#dae8fc",font=("Arial",18),text="Unspeakable Things")
titlelbl3.place(x=220,y=320)

#Book title 4#
titlelbl4 = tk.Label(fictionframe,bg="#dae8fc",font=("Arial",18),text="The Buried Book")
titlelbl4.place(x=620,y=320)

#Description book 1#
descrptlbl1 = tk.Label(fictionframe,bg="#dae8fc",font=("Arial",12),text="A superlative middle volume,\nadding depth and scope without\nsacrificing clarity or theme.",justify="left")
descrptlbl1.place(x=220,y=150)

#Description book 2#
descrptlbl2 = tk.Label(fictionframe,bg="#dae8fc",font=("Arial",12),text="Truly deserving of the accolade\nModern Classic, Michael Lieber's\ncult bestseller The War Hero is\na remarkable achievement - both\ninsightful and elegant, comedic and\ndark.",justify="left")
descrptlbl2.place(x=620,y=150)

#Description book 3#
descrptlbl1 = tk.Label(fictionframe,bg="#dae8fc",font=("Arial",12),text="Vivid, atmospheric, and genuinely\nunsettling, UNSPEAKABLE THINGS\nis a coming-of-age story as you’ve\nnever read it before.",justify="left")
descrptlbl1.place(x=220,y=370)

#Description book 4#
descrptlbl1 = tk.Label(fictionframe,bg="#dae8fc",font=("Arial",12),text="A vivid look at 1950’s farm life\nfrom the political climate,\nprejudice and their daily survival.",justify="left")
descrptlbl1.place(x=620,y=370)

#Image 1 on page#
image1 = Image.open("fiction_TheBrokenRaven.png")#Opening the Image#
resize_image1 = image1.resize((108,162))#Resizing the image using resize()#
img1 = ImageTk.PhotoImage(resize_image1)
#Create label for resized image#
label1 = tk.Label(fictionframe,image=img1)
label1.image = img1
label1.place(x=100,y=100)

#Image 2 on page#
image2 = Image.open("fiction_TheWarHero.png")
resize_image2 = image2.resize((108,162))
img2 = ImageTk.PhotoImage(resize_image2)
#Create label for resized image#
label2 = tk.Label(fictionframe,image=img2)
label2.image = img2
label2.place(x=500,y=100)

#Image 3 on page#
image3 = Image.open("fiction_UnspeakableThings.png")
resize_image3 = image3.resize((108,162))
img3 = ImageTk.PhotoImage(resize_image3)
#Create label for resized image#
label3 = tk.Label(fictionframe,image=img3)
label3.image = img3
label3.place(x=100,y=320)

#Image 4 on page#
image4 = Image.open("fiction_TheBuriedBook.png")
resize_image4 = image4.resize((108,162))
img4 = ImageTk.PhotoImage(resize_image4)
#Create label for resized image#
label4 = tk.Label(fictionframe,image=img4)
label4.image = img4
label4.place(x=500,y=320)

#Detail button for book 1#
detlbtn1 = tk.Button(fictionframe,fg="white",bg="#1ba1e2",text="See Details",command=fbook1_frame)
detlbtn1.place(x=100,y=270)

#Detail button for book 2#
detlbtn2 = tk.Button(fictionframe,fg="white",bg="#1ba1e2",text="See Details",command=fbook2_frame)
detlbtn2.place(x=500,y=270)

#Detail button for book 3#
detlbtn3 = tk.Button(fictionframe,fg="white",bg="#1ba1e2",text="See Details",command=fbook3_frame)
detlbtn3.place(x=100,y=490)

#Detail button for book 4#
detlbtn4 = tk.Button(fictionframe,fg="white",bg="#1ba1e2",text="See Details",command=fbook4_frame)
detlbtn4.place(x=500,y=490)

#Button to go back to types of book page#
bkbtn = tk.Button(fictionframe,fg="white",bg="#1ba1e2",text="Back",width=10,command=bktp_frame)
bkbtn.place(x=850,y=490)

#Widgets for Non Fiction books frame#

#Non Fiction frame name#
bksinnnfiction = tk.Label(nonfictionframe,bg="#dae8fc",font=("Arial",32),text="Types Of Books In Non Fiction")
bksinnnfiction.place(x=225,y=25)

#Book title 1#
titlelbl1 = tk.Label(nonfictionframe,bg="#dae8fc",font=("Arial",18),text="Anne Frank: The Diary\nOf A Young Girl",justify="left")
titlelbl1.place(x=220,y=100)

#Book title 2#
titlelbl2 = tk.Label(nonfictionframe,bg="#dae8fc",font=("Arial",18),text="Bloodlands: Europe Between\nHitler And Stalin",justify="left")
titlelbl2.place(x=620,y=100)

#Book title 3#
titlelbl3 = tk.Label(nonfictionframe,bg="#dae8fc",font=("Arial",18),text="A History Of Pictures",justify="left")
titlelbl3.place(x=220,y=320)

#Book title 4#
titlelbl4 = tk.Label(nonfictionframe,bg="#dae8fc",font=("Arial",18),text="The Soviet Union: The Fifty\nYears",justify="left")
titlelbl4.place(x=620,y=320)

#Description book 1#
descrptlbl1 = tk.Label(nonfictionframe,bg="#dae8fc",font=("Arial",12),text="A Jewish teenager, wrote a diary of\nher family's two years in hiding\n(1942-1944) during the German\noccupation of the Netherlands in\nWorld War II.",justify="left")
descrptlbl1.place(x=220,y=160)

#Description book 2#
descrptlbl2 = tk.Label(nonfictionframe,bg="#dae8fc",font=("Arial",12),text="At war’s end, both the German and the\nSoviet killing sites fell behind the iron\ncurtain, leaving the history of mass\nkilling in darkness.",justify="left")
descrptlbl2.place(x=620,y=160)

#Description book 3#
descrptlbl1 = tk.Label(nonfictionframe,bg="#dae8fc",font=("Arial",12),text="Informed and energized by a\nlifetime of painting, drawing and\nmaking images with cameras. What\nmakes marks on a flat surface\ninteresting?",justify="left")
descrptlbl1.place(x=220,y=380)

#Description book 4#
descrptlbl1 = tk.Label(nonfictionframe,bg="#dae8fc",font=("Arial",12),text="This is an authoritative and comprehensive\nhistory of the Fifty Years' war and the\nrelationship that dominated world politics in\nthe second half of the twentieth century.",justify="left")
descrptlbl1.place(x=620,y=380)

#Image 1 on page#
image1 = Image.open("nonfic_AnneFrank.png")#Opening the Image#
resize_image1 = image1.resize((108,162))#Resizing the image using resize()#
img1 = ImageTk.PhotoImage(resize_image1)
#Create label for resized image#
label1 = tk.Label(nonfictionframe,image=img1)
label1.image = img1
label1.place(x=100,y=100)

#Image 2 on page#
image2 = Image.open("nonfic_BloodLands.png")
resize_image2 = image2.resize((108,162))
img2 = ImageTk.PhotoImage(resize_image2)
#Create label for resized image#
label2 = tk.Label(nonfictionframe,image=img2)
label2.image = img2
label2.place(x=500,y=100)

#Image 3 on page#
image3 = Image.open("nonfic_HistoryOfPictures.png")
resize_image3 = image3.resize((108,162))
img3 = ImageTk.PhotoImage(resize_image3)
#Create label for resized image#
label3 = tk.Label(nonfictionframe,image=img3)
label3.image = img3
label3.place(x=100,y=320)

#Image 4 on page#
image4 = Image.open("nonfic_SovietUnion.png")
resize_image4 = image4.resize((108,162))
img4 = ImageTk.PhotoImage(resize_image4)
#Create label for resized image#
label4 = tk.Label(nonfictionframe,image=img4)
label4.image = img4
label4.place(x=500,y=320)

#Detail button for book 1#
detlbtn1 = tk.Button(nonfictionframe,fg="white",bg="#1ba1e2",text="See Details",command=nbook1_frame)
detlbtn1.place(x=100,y=270)

#Detail button for book 2#
detlbtn2 = tk.Button(nonfictionframe,fg="white",bg="#1ba1e2",text="See Details",command=fbook2_frame)
detlbtn2.place(x=500,y=270)

#Detail button for book 3#
detlbtn3 = tk.Button(nonfictionframe,fg="white",bg="#1ba1e2",text="See Details",command=fbook3_frame)
detlbtn3.place(x=100,y=490)

#Detail button for book 4#
detlbtn4 = tk.Button(nonfictionframe,fg="white",bg="#1ba1e2",text="See Details",command=fbook4_frame)
detlbtn4.place(x=500,y=490)

#Button to go back to types of book page#
bkbtn = tk.Button(nonfictionframe,fg="white",bg="#1ba1e2",text="Back",width=10,command=bktp_frame)
bkbtn.place(x=850,y=490)

#Widgets for Children books frame#

#Children frame name#
bksinchildren = tk.Label(childrenframe,bg="#dae8fc",font=("Arial",32),text="Types Of Books For Children")
bksinchildren.place(x=225,y=25)

#Book title 1#
titlelbl1 = tk.Label(childrenframe,bg="#dae8fc",font=("Arial",18),text="Help Around The House",justify="left")
titlelbl1.place(x=220,y=100)

#Book title 2#
titlelbl2 = tk.Label(childrenframe,bg="#dae8fc",font=("Arial",18),text="Maya & Filippo Make\nFriends In Auckland",justify="left")
titlelbl2.place(x=620,y=100)

#Book title 3#
titlelbl3 = tk.Label(childrenframe,bg="#dae8fc",font=("Arial",18),text="Paul's Horse Herman")
titlelbl3.place(x=220,y=320)

#Book title 4#
titlelbl4 = tk.Label(childrenframe,bg="#dae8fc",font=("Arial",18),text="The Rocket Book")
titlelbl4.place(x=620,y=320)

#Description book 1#
descrptlbl1 = tk.Label(childrenframe,bg="#dae8fc",font=("Arial",12),text="The funny and moving story of a\nboy and his friends never losing\nheart in a sometimes heartless\nworld.",justify="left")
descrptlbl1.place(x=220,y=160)

#Description book 2#
descrptlbl2 = tk.Label(childrenframe,bg="#dae8fc",font=("Arial",12),text="Embark on a one-of-a-kind,\nunprecedented, breathtaking\nadventure with Maya and Filippo\nas they travel around the globe on board\nthe 'Fun Princes' - a cruise ship full of\nsurprises.",justify="left")
descrptlbl2.place(x=620,y=160)

#Description book 3#
descrptlbl3 = tk.Label(childrenframe,bg="#dae8fc",font=("Arial",12),text="Few children can own a horse,\nbut they go right on wishing that\nthey could -- and reading about\nluckier children who do.",justify="left")
descrptlbl3.place(x=220,y=370)

#Description book 4#
descrptlbl4 = tk.Label(childrenframe,bg="#dae8fc",font=("Arial",12),text="The upward progress of a rocket,\nlit in the basement by the janitor's\nson, causes some strange situations\nas it passes through twenty floors of\napartments.",justify="left")
descrptlbl4.place(x=620,y=370)

#Image 1 on page#
image1 = Image.open("childr_HelpAroundTheHouse.png")#Opening the Image#
resize_image1 = image1.resize((108,162))#Resizing the image using resize()#
img1 = ImageTk.PhotoImage(resize_image1)
#Create label for resized image#
label1 = tk.Label(childrenframe,image=img1)
label1.image = img1
label1.place(x=100,y=100)

#Image 2 on page#
image2 = Image.open("childr_MayaAndFilippo.png")
resize_image2 = image2.resize((108,162))
img2 = ImageTk.PhotoImage(resize_image2)
#Create label for resized image#
label2 = tk.Label(childrenframe,image=img2)
label2.image = img2
label2.place(x=500,y=100)

#Image 3 on page#
image3 = Image.open("childr_PaulsHorseHerman.png")
resize_image3 = image3.resize((108,162))
img3 = ImageTk.PhotoImage(resize_image3)
#Create label for resized image#
label3 = tk.Label(childrenframe,image=img3)
label3.image = img3
label3.place(x=100,y=320)

#Image 4 on page#
image4 = Image.open("childr_TheRocketBook.png")
resize_image4 = image4.resize((108,162))
img4 = ImageTk.PhotoImage(resize_image4)
#Create label for resized image#
label4 = tk.Label(childrenframe,image=img4)
label4.image = img4
label4.place(x=500,y=320)

#Detail button for book 1#
detlbtn1 = tk.Button(childrenframe,fg="white",bg="#1ba1e2",text="See Details",command=fbook1_frame)
detlbtn1.place(x=100,y=270)

#Detail button for book 2#
detlbtn2 = tk.Button(childrenframe,fg="white",bg="#1ba1e2",text="See Details",command=fbook2_frame)
detlbtn2.place(x=500,y=270)

#Detail button for book 3#
detlbtn3 = tk.Button(childrenframe,fg="white",bg="#1ba1e2",text="See Details",command=fbook3_frame)
detlbtn3.place(x=100,y=490)

#Detail button for book 4#
detlbtn4 = tk.Button(childrenframe,fg="white",bg="#1ba1e2",text="See Details",command=fbook4_frame)
detlbtn4.place(x=500,y=490)

#Button to go back to types of book page#
bkbtn = tk.Button(childrenframe,fg="white",bg="#1ba1e2",text="Back",width=10,command=bktp_frame)
bkbtn.place(x=850,y=490)

#Widgets for Encyclopedias frame#

#Fiction frame name#
bksinencyclopedia = tk.Label(encyclopediaframe,bg="#dae8fc",font=("Arial",32),text="Types Of Encyclopedia")
bksinencyclopedia.place(x=225,y=25)

#Book title 1#
titlelbl1 = tk.Label(encyclopediaframe,bg="#dae8fc",font=("Arial",18),text="Historiche Encyclopedie\nMaastricht",justify="left")
titlelbl1.place(x=180,y=100)

#Book title 2#
titlelbl2 = tk.Label(encyclopediaframe,bg="#dae8fc",font=("Arial",18),text="The Encyclopedia Of Science\nFiction",justify="left")
titlelbl2.place(x=620,y=100)

#Book title 3#
titlelbl3 = tk.Label(encyclopediaframe,bg="#dae8fc",font=("Arial",18),text="Brittanica All New Children's\nencyclopedia: What We\nKnow And What We Don't",justify="left")
titlelbl3.place(x=180,y=310)

#Book title 4#
titlelbl4 = tk.Label(encyclopediaframe,bg="#dae8fc",font=("Arial",18),text="Encyclopedia Of Dinosaurs:\nThe Theropids",justify="left")
titlelbl4.place(x=620,y=310)

#Description book 1#
descrptlbl1 = tk.Label(encyclopediaframe,bg="#dae8fc",font=("Arial",12),text="The Historical Encyclopedia\nMaastricht,abbreviated as HEM,\nis a Dutch-language encyclopedia\nabout the history of Maastricht.",justify="left")
descrptlbl1.place(x=180,y=160)

#Description book 2#
descrptlbl2 = tk.Label(encyclopediaframe,bg="#dae8fc",font=("Arial",12),text="A good extensive reference book\nfor the science fiction fan who\nis looking for in depth information\non the history of science fiction",justify="left")
descrptlbl2.place(x=620,y=160)

#Description book 3#
descrptlbl1 = tk.Label(encyclopediaframe,bg="#dae8fc",font=("Arial",12),text="This book of amazing facts you can\ntrust will provide hundreds of\nhours of fun learning for curious\nchildren and their families.",justify="left")
descrptlbl1.place(x=180,y=400)

#Description book 4#
descrptlbl1 = tk.Label(encyclopediaframe,bg="#dae8fc",font=("Arial",12),text="This one-of-a-kind compendium\nfeatures more than 3,000 records,\ncovers some 750 theropod species,\nand includes a wealth of\nillustrations ranging from diagrams\nand technical drawings to full-colour\nreconstructions of specimens.",justify="left")
descrptlbl1.place(x=620,y=370)

#Image 1 on page#
image1 = Image.open("encycl_Historische.png")#Opening the Image#
resize_image1 = image1.resize((108,162))#Resizing the image using resize()#
img1 = ImageTk.PhotoImage(resize_image1)
#Create label for resized image#
label1 = tk.Label(encyclopediaframe,image=img1)
label1.image = img1
label1.place(x=60,y=100)

#Image 2 on page#
image2 = Image.open("encycl_SciFi.png")
resize_image2 = image2.resize((108,162))
img2 = ImageTk.PhotoImage(resize_image2)
#Create label for resized image#
label2 = tk.Label(encyclopediaframe,image=img2)
label2.image = img2
label2.place(x=500,y=100)

#Image 3 on page#
image3 = Image.open("encycl_Childrens.png")
resize_image3 = image3.resize((108,162))
img3 = ImageTk.PhotoImage(resize_image3)
#Create label for resized image#
label3 = tk.Label(encyclopediaframe,image=img3)
label3.image = img3
label3.place(x=60,y=310)

#Image 4 on page#
image4 = Image.open("encycl_Dinos.png")
resize_image4 = image4.resize((108,162))
img4 = ImageTk.PhotoImage(resize_image4)
#Create label for resized image#
label4 = tk.Label(encyclopediaframe,image=img4)
label4.image = img4
label4.place(x=500,y=310)

#Detail button for book 1#
detlbtn1 = tk.Button(encyclopediaframe,fg="white",bg="#1ba1e2",text="See Details",command=fbook1_frame)
detlbtn1.place(x=60,y=270)

#Detail button for book 2#
detlbtn2 = tk.Button(encyclopediaframe,fg="white",bg="#1ba1e2",text="See Details",command=fbook2_frame)
detlbtn2.place(x=500,y=270)

#Detail button for book 3#
detlbtn3 = tk.Button(encyclopediaframe,fg="white",bg="#1ba1e2",text="See Details",command=fbook3_frame)
detlbtn3.place(x=60,y=480)

#Detail button for book 4#
detlbtn4 = tk.Button(encyclopediaframe,fg="white",bg="#1ba1e2",text="See Details",command=fbook4_frame)
detlbtn4.place(x=500,y=480)

#Button to go back to types of book page#
bkbtn = tk.Button(encyclopediaframe,fg="white",bg="#1ba1e2",text="Back",width=10,command=bktp_frame)
bkbtn.place(x=850,y=490)

#Widgets for Historical Fiction books frame#

#Historical Fiction frame name#
bksinhisfic = tk.Label(historicalframe,bg="#dae8fc",font=("Arial",32),text="Types Of Books In Historical Fiction")
bksinhisfic.place(x=225,y=25)

#Book title 1#
titlelbl1 = tk.Label(historicalframe,bg="#dae8fc",font=("Arial",18),text="Autumn In Oxford")
titlelbl1.place(x=220,y=100)

#Book title 2#
titlelbl2 = tk.Label(historicalframe,bg="#dae8fc",font=("Arial",18),text="The Road Beyond Ruin")
titlelbl2.place(x=620,y=100)

#Book title 3#
titlelbl3 = tk.Label(historicalframe,bg="#dae8fc",font=("Arial",18),text="The Unbroken Line Of\nThe Moon",justify="left")
titlelbl3.place(x=220,y=320)

#Book title 4#
titlelbl4 = tk.Label(historicalframe,bg="#dae8fc",font=("Arial",18),text="The Valley")
titlelbl4.place(x=620,y=320)

#Description book 1#
descrptlbl1 = tk.Label(historicalframe,bg="#dae8fc",font=("Arial",12),text="A conspiracy theorist's dream of a\nnovel, set during the period of one of\nthe craziest conspiracies of all – the\nRed Scare of the late 1950s.",justify="left")
descrptlbl1.place(x=220,y=150)

#Description book 2#
descrptlbl2 = tk.Label(historicalframe,bg="#dae8fc",font=("Arial",12),text="As Stefano, an Italian POW, heads toward\nhome across war-ravaged Germany, he\nencounters a young child beside his dead\nmother. Unable to leave him to an unknown\nfate, Stefano takes the boy with him, finding\nrefuge in a seemingly abandoned house in\na secluded woodland.",justify="left")
descrptlbl2.place(x=620,y=150)

#Description book 3#
descrptlbl1 = tk.Label(historicalframe,bg="#dae8fc",font=("Arial",12),text="An intense tale of the vikings, focusing\non three main characters: Sigrid,\nSweyn, and Emma.",justify="left")
descrptlbl1.place(x=220,y=380)

#Description book 4#
descrptlbl1 = tk.Label(historicalframe,bg="#dae8fc",font=("Arial",12),text="The story of Sophie Grafton, the orphaned\ndaughter of an English viscount.\nWhen she discovers that she has lost her\nhome and is penniless, she is forced to travel\nto America to start a new life in colonial\nVirginia",justify="left")
descrptlbl1.place(x=620,y=380)

#Image 1 on page#
image1 = Image.open("hisfic_AutumnInOxford.png")#Opening the Image#
resize_image1 = image1.resize((108,162))#Resizing the image using resize()#
img1 = ImageTk.PhotoImage(resize_image1)
#Create label for resized image#
label1 = tk.Label(historicalframe,image=img1)
label1.image = img1
label1.place(x=100,y=100)

#Image 2 on page#
image2 = Image.open("hisfic_TheRoadBeyondRuin.png")
resize_image2 = image2.resize((108,162))
img2 = ImageTk.PhotoImage(resize_image2)
#Create label for resized image#
label2 = tk.Label(historicalframe,image=img2)
label2.image = img2
label2.place(x=500,y=100)

#Image 3 on page#
image3 = Image.open("hisfic_TheUnbrokenLineOfTheMoon.png")
resize_image3 = image3.resize((108,162))
img3 = ImageTk.PhotoImage(resize_image3)
#Create label for resized image#
label3 = tk.Label(historicalframe,image=img3)
label3.image = img3
label3.place(x=100,y=320)

#Image 4 on page#
image4 = Image.open("hisfic_TheValley.png")
resize_image4 = image4.resize((108,162))
img4 = ImageTk.PhotoImage(resize_image4)
#Create label for resized image#
label4 = tk.Label(historicalframe,image=img4)
label4.image = img4
label4.place(x=500,y=320)

#Detail button for book 1#
detlbtn1 = tk.Button(historicalframe,fg="white",bg="#1ba1e2",text="See Details",command=fbook1_frame)
detlbtn1.place(x=100,y=270)

#Detail button for book 2#
detlbtn2 = tk.Button(historicalframe,fg="white",bg="#1ba1e2",text="See Details",command=fbook2_frame)
detlbtn2.place(x=500,y=270)

#Detail button for book 3#
detlbtn3 = tk.Button(historicalframe,fg="white",bg="#1ba1e2",text="See Details",command=fbook3_frame)
detlbtn3.place(x=100,y=490)

#Detail button for book 4#
detlbtn4 = tk.Button(historicalframe,fg="white",bg="#1ba1e2",text="See Details",command=fbook4_frame)
detlbtn4.place(x=500,y=490)

#Button to go back to types of book page#
bkbtn = tk.Button(historicalframe,fg="white",bg="#1ba1e2",text="Back",width=10,command=bktp_frame)
bkbtn.place(x=850,y=490)

#Widgets for Science Fiction books frame#

#Fiction frame name#
bksinscifi = tk.Label(scififrame,bg="#dae8fc",font=("Arial",32),text="Types Of Books In Science Fiction")
bksinscifi.place(x=225,y=25)

#Book title 1#
titlelbl1 = tk.Label(scififrame,bg="#dae8fc",font=("Arial",18),text="A World Of Secrets")
titlelbl1.place(x=220,y=100)

#Book title 2#
titlelbl2 = tk.Label(scififrame,bg="#dae8fc",font=("Arial",18),text="Stillhouse Lake")
titlelbl2.place(x=620,y=100)

#Book title 3#
titlelbl3 = tk.Label(scififrame,bg="#dae8fc",font=("Arial",18),text="The Winter Over")
titlelbl3.place(x=220,y=320)

#Book title 4#
titlelbl4 = tk.Label(scififrame,bg="#dae8fc",font=("Arial",18),text="The Wise Man's Fear")
titlelbl4.place(x=620,y=320)

#Description book 1#
descrptlbl1 = tk.Label(scififrame,bg="#dae8fc",font=("Arial",12),text="Taimin and Selena are desperate for\nanswers. They need to discover\nthe truth about their origins and the\nfirewall that borders the wasteland.",justify="left")
descrptlbl1.place(x=220,y=150)

#Description book 2#
descrptlbl2 = tk.Label(scififrame,bg="#dae8fc",font=("Arial",12),text="Gina Royal is the definition of average—a\nshy Midwestern housewife with a happy\nmarriage and two adorable children.\nBut when a car accident reveals her husband's\nsecret life as a serial killer, she must remake\nherself as Gwen Proctor—the ultimate warrior\nmom.",justify="left")
descrptlbl2.place(x=620,y=150)

#Description book 3#
descrptlbl1 = tk.Label(scififrame,bg="#dae8fc",font=("Arial",12),text="An entertaining novel which takes\nplace in a research center in Antarctica.\nForty four scientists and crew members\nmust work together to survive nine\nmonths of total darkness in winter and\nin isolation from the outside world.",justify="left")
descrptlbl1.place(x=220,y=370)

#Description book 4#
descrptlbl1 = tk.Label(scififrame,bg="#dae8fc",font=("Arial",12),text="An escalating rivalry with a powerful\nmember of the nobility forces Kvothe to leave\nthe University and seek his fortune abroad.\nAdrift, penniless, and alone, he travels to\nVintas, where he quickly becomes entangled\nin the politics of courtly society.",justify="left")
descrptlbl1.place(x=620,y=370)

#Image 1 on page#
image1 = Image.open("scific_AWorldOfSecrets.png")#Opening the Image#
resize_image1 = image1.resize((108,162))#Resizing the image using resize()#
img1 = ImageTk.PhotoImage(resize_image1)
#Create label for resized image#
label1 = tk.Label(scififrame,image=img1)
label1.image = img1
label1.place(x=100,y=100)

#Image 2 on page#
image2 = Image.open("scific_StillhouseLake.png")
resize_image2 = image2.resize((108,162))
img2 = ImageTk.PhotoImage(resize_image2)
#Create label for resized image#
label2 = tk.Label(scififrame,image=img2)
label2.image = img2
label2.place(x=500,y=100)

#Image 3 on page#
image3 = Image.open("scific_TheWinterOver.png")
resize_image3 = image3.resize((108,162))
img3 = ImageTk.PhotoImage(resize_image3)
#Create label for resized image#
label3 = tk.Label(scififrame,image=img3)
label3.image = img3
label3.place(x=100,y=320)

#Image 4 on page#
image4 = Image.open("scific_TheWiseMansFear.png")
resize_image4 = image4.resize((108,162))
img4 = ImageTk.PhotoImage(resize_image4)
#Create label for resized image#
label4 = tk.Label(scififrame,image=img4)
label4.image = img4
label4.place(x=500,y=320)

#Detail button for book 1#
detlbtn1 = tk.Button(scififrame,fg="white",bg="#1ba1e2",text="See Details",command=fbook1_frame)
detlbtn1.place(x=100,y=270)

#Detail button for book 2#
detlbtn2 = tk.Button(scififrame,fg="white",bg="#1ba1e2",text="See Details",command=fbook2_frame)
detlbtn2.place(x=500,y=270)

#Detail button for book 3#
detlbtn3 = tk.Button(scififrame,fg="white",bg="#1ba1e2",text="See Details",command=fbook3_frame)
detlbtn3.place(x=100,y=490)

#Detail button for book 4#
detlbtn4 = tk.Button(scififrame,fg="white",bg="#1ba1e2",text="See Details",command=fbook4_frame)
detlbtn4.place(x=500,y=490)

#Button to go back to types of book page#
bkbtn = tk.Button(scififrame,fg="white",bg="#1ba1e2",text="Back",width=10,command=bktp_frame)
bkbtn.place(x=850,y=490)

#Detail Frame Of Fiction Book 1#

#Large Image#
image = Image.open("fiction_TheBrokenRaven.png")
resize_image = image.resize((270,400))#108*2.5=270,162*2.5=405,take whole number#
img = ImageTk.PhotoImage(resize_image)
largeimg = tk.Label(fframeb1,image=img)
largeimg.image = img
largeimg.place(x=50,y=70)#(540-400)/2=70#

#Title Label#
authlbl = tk.Label(fframeb1,bg="#dae8fc",font=("Arial",22),text="The Broken Raven",justify="left")
authlbl.place(x=370,y=70)

#Author Label#
authlbl = tk.Label(fframeb1,bg="#dae8fc",font=("Arial",16),text="Author: Joseph Elliott",justify="left")
authlbl.place(x=370,y=110)

#Genre Label#
genlbl = tk.Label(fframeb1,bg="#dae8fc",font=("Arial",16),text="Genre: Fiction",justify="left")
genlbl.place(x=370,y=140)

#Publisher Label#
publbl = tk.Label(fframeb1,bg="#dae8fc",font=("Arial",16),text="Publisher: Walker Books Us",justify="left")
publbl.place(x=370,y=170)

#Description#
deslbl = tk.Label(fframeb1,bg="#dae8fc",font=("Arial",14),text="After their escape from Norveg, Agatha and Jaime return\nwith their clan to the Isle of Skye to find that their enclave\nis now in the hands of the treacherous people of Raasay.\nThey find tenuous shelter with another clan, but disaster\nsoon strikes when the terrifying shadow creatures known\nas sgàilean escape their magical prison and wreak havoc\nacross the island. Now Agatha and Jaime must call on old\nand new allies to fight this threat. In the meantime, a ship\nfrom Norveg sails for the court of King Edmund of Ingland,\nwhere a dangerous alliance is forming, and Sigrid, a girl with\nan extraordinary memory, works to free herself from the\nclutches of a cruel king.",justify="left")
deslbl.place(x=370,y=200)

#Back button#
bkbtn = tk.Button(fframeb1,fg="white",bg="#1ba1e2",text="Back",command=fiction_frame)
bkbtn.place(x=370,y=490)

#Change availability button#
availbtn = tk.Button(fframeb1,fg="white",bg="#1ba1e2",text="Check Availability",command=f1dtl_frame)
availbtn.place(x=820,y=490)

#Fiction Book 1 Availaility Page#

#Large Image#
image = Image.open("fiction_TheBrokenRaven.png")
resize_image = image.resize((270,400))#108*2.5=270,162*2.5=405,take whole number#
img = ImageTk.PhotoImage(resize_image)
largeimg = tk.Label(fic1dtl,image=img)
largeimg.image = img
largeimg.place(x=50,y=70)#(540-400)/2=70#

#Title Current Available Copies#
cac = tk.Label(fic1dtl,bg="#dae8fc",font=("Arial",32),text="Current Available Copies")
cac.place(x=425,y=100)

#Qty of Fiction Book 1#
f1avalbl = tk.Label(fic1dtl,bg="#dae8fc",font=("Arial",32),text="Digit")
f1avalbl.place(x=600,y=300)

#Add Button#
addbtn = tk.Button(fic1dtl,fg="white",bg="#1ba1e2",width=4,font=("Arial",32),text="+")
addbtn.place(x=800,y=300)

#Minus Button#
minbtn = tk.Button(fic1dtl,fg="white",bg="#1ba1e2",width=4,font=("Arial",32),text="-")
minbtn.place(x=400,y=300)

#Back button#
bkbtn = tk.Button(fic1dtl,fg="white",bg="#1ba1e2",text="Back",command=fbook1_frame)
bkbtn.place(x=370,y=490)

#Change availability button#
savebtn = tk.Button(fic1dtl,fg="white",bg="#1ba1e2",text="Save")
savebtn.place(x=820,y=490)

window.mainloop()

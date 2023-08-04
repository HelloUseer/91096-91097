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
bkbtn = tk.Button(fictionframe,fg="white",bg="#1ba1e2",text="Back",command=bktp_frame)
bkbtn.place(x=900,y=490)

#Widgets for Non Fiction books frame#

#Non Fiction frame name#
bksinnnfiction = tk.Label(nonfictionframe,bg="#dae8fc",font=("Arial",32),text="Types Of Books In Non Fiction")
bksinnnfiction.place(x=225,y=25)

#Book title 1#
titlelbl1 = tk.Label(nonfictionframe,bg="#dae8fc",font=("Arial",18),text="The Broken Raven")
titlelbl1.place(x=220,y=100)

#Book title 2#
titlelbl2 = tk.Label(nonfictionframe,bg="#dae8fc",font=("Arial",18),text="The War Hero")
titlelbl2.place(x=620,y=100)

#Book title 3#
titlelbl3 = tk.Label(nonfictionframe,bg="#dae8fc",font=("Arial",18),text="Unspeakable Things")
titlelbl3.place(x=220,y=320)

#Book title 4#
titlelbl4 = tk.Label(nonfictionframe,bg="#dae8fc",font=("Arial",18),text="The Buried Book")
titlelbl4.place(x=620,y=320)

#Description book 1#
descrptlbl1 = tk.Label(nonfictionframe,bg="#dae8fc",font=("Arial",12),text="A superlative middle volume,\nadding depth and scope without\nsacrificing clarity or theme.",justify="left")
descrptlbl1.place(x=220,y=150)

#Description book 2#
descrptlbl2 = tk.Label(nonfictionframe,bg="#dae8fc",font=("Arial",12),text="Truly deserving of the accolade\nModern Classic, Michael Lieber's\ncult bestseller The War Hero is\na remarkable achievement - both\ninsightful and elegant, comedic and\ndark.",justify="left")
descrptlbl2.place(x=620,y=150)

#Description book 3#
descrptlbl1 = tk.Label(nonfictionframe,bg="#dae8fc",font=("Arial",12),text="Vivid, atmospheric, and genuinely\nunsettling, UNSPEAKABLE THINGS\nis a coming-of-age story as you’ve\nnever read it before.",justify="left")
descrptlbl1.place(x=220,y=370)

#Description book 4#
descrptlbl1 = tk.Label(nonfictionframe,bg="#dae8fc",font=("Arial",12),text="A vivid look at 1950’s farm life\nfrom the political climate,\nprejudice and their daily survival.",justify="left")
descrptlbl1.place(x=620,y=370)

#Image 1 on page#
image1 = Image.open("fiction_TheBrokenRaven.png")#Opening the Image#
resize_image1 = image1.resize((108,162))#Resizing the image using resize()#
img1 = ImageTk.PhotoImage(resize_image1)
#Create label for resized image#
label1 = tk.Label(nonfictionframe,image=img1)
label1.image = img1
label1.place(x=100,y=100)

#Image 2 on page#
image2 = Image.open("fiction_TheWarHero.png")
resize_image2 = image2.resize((108,162))
img2 = ImageTk.PhotoImage(resize_image2)
#Create label for resized image#
label2 = tk.Label(nonfictionframe,image=img2)
label2.image = img2
label2.place(x=500,y=100)

#Image 3 on page#
image3 = Image.open("fiction_UnspeakableThings.png")
resize_image3 = image3.resize((108,162))
img3 = ImageTk.PhotoImage(resize_image3)
#Create label for resized image#
label3 = tk.Label(nonfictionframe,image=img3)
label3.image = img3
label3.place(x=100,y=320)

#Image 4 on page#
image4 = Image.open("fiction_TheBuriedBook.png")
resize_image4 = image4.resize((108,162))
img4 = ImageTk.PhotoImage(resize_image4)
#Create label for resized image#
label4 = tk.Label(nonfictionframe,image=img4)
label4.image = img4
label4.place(x=500,y=320)

#Detail button for book 1#
detlbtn1 = tk.Button(nonfictionframe,fg="white",bg="#1ba1e2",text="See Details",command=fbook1_frame)
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
bkbtn = tk.Button(nonfictionframe,fg="white",bg="#1ba1e2",text="Back",command=bktp_frame)
bkbtn.place(x=900,y=490)

#Widgets for Children books frame#

#Children frame name#
bksinchildren = tk.Label(childrenframe,bg="#dae8fc",font=("Arial",32),text="Types Of Books For Children")
bksinchildren.place(x=225,y=25)

#Book title 1#
titlelbl1 = tk.Label(childrenframe,bg="#dae8fc",font=("Arial",18),text="The Broken Raven")
titlelbl1.place(x=220,y=100)

#Book title 2#
titlelbl2 = tk.Label(childrenframe,bg="#dae8fc",font=("Arial",18),text="The War Hero")
titlelbl2.place(x=620,y=100)

#Book title 3#
titlelbl3 = tk.Label(childrenframe,bg="#dae8fc",font=("Arial",18),text="Unspeakable Things")
titlelbl3.place(x=220,y=320)

#Book title 4#
titlelbl4 = tk.Label(childrenframe,bg="#dae8fc",font=("Arial",18),text="The Buried Book")
titlelbl4.place(x=620,y=320)

#Description book 1#
descrptlbl1 = tk.Label(childrenframe,bg="#dae8fc",font=("Arial",12),text="A superlative middle volume,\nadding depth and scope without\nsacrificing clarity or theme.",justify="left")
descrptlbl1.place(x=220,y=150)

#Description book 2#
descrptlbl2 = tk.Label(childrenframe,bg="#dae8fc",font=("Arial",12),text="Truly deserving of the accolade\nModern Classic, Michael Lieber's\ncult bestseller The War Hero is\na remarkable achievement - both\ninsightful and elegant, comedic and\ndark.",justify="left")
descrptlbl2.place(x=620,y=150)

#Description book 3#
descrptlbl1 = tk.Label(childrenframe,bg="#dae8fc",font=("Arial",12),text="Vivid, atmospheric, and genuinely\nunsettling, UNSPEAKABLE THINGS\nis a coming-of-age story as you’ve\nnever read it before.",justify="left")
descrptlbl1.place(x=220,y=370)

#Description book 4#
descrptlbl1 = tk.Label(childrenframe,bg="#dae8fc",font=("Arial",12),text="A vivid look at 1950’s farm life\nfrom the political climate,\nprejudice and their daily survival.",justify="left")
descrptlbl1.place(x=620,y=370)

#Image 1 on page#
image1 = Image.open("fiction_TheBrokenRaven.png")#Opening the Image#
resize_image1 = image1.resize((108,162))#Resizing the image using resize()#
img1 = ImageTk.PhotoImage(resize_image1)
#Create label for resized image#
label1 = tk.Label(childrenframe,image=img1)
label1.image = img1
label1.place(x=100,y=100)

#Image 2 on page#
image2 = Image.open("fiction_TheWarHero.png")
resize_image2 = image2.resize((108,162))
img2 = ImageTk.PhotoImage(resize_image2)
#Create label for resized image#
label2 = tk.Label(childrenframe,image=img2)
label2.image = img2
label2.place(x=500,y=100)

#Image 3 on page#
image3 = Image.open("fiction_UnspeakableThings.png")
resize_image3 = image3.resize((108,162))
img3 = ImageTk.PhotoImage(resize_image3)
#Create label for resized image#
label3 = tk.Label(childrenframe,image=img3)
label3.image = img3
label3.place(x=100,y=320)

#Image 4 on page#
image4 = Image.open("fiction_TheBuriedBook.png")
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
bkbtn = tk.Button(childrenframe,fg="white",bg="#1ba1e2",text="Back",command=bktp_frame)
bkbtn.place(x=900,y=490)

#Widgets for Encyclopedias frame#

#Fiction frame name#
bksinencyclopedia = tk.Label(encyclopediaframe,bg="#dae8fc",font=("Arial",32),text="Types Of Encyclopedia")
bksinencyclopedia.place(x=225,y=25)

#Book title 1#
titlelbl1 = tk.Label(encyclopediaframe,bg="#dae8fc",font=("Arial",18),text="The Broken Raven")
titlelbl1.place(x=220,y=100)

#Book title 2#
titlelbl2 = tk.Label(encyclopediaframe,bg="#dae8fc",font=("Arial",18),text="The War Hero")
titlelbl2.place(x=620,y=100)

#Book title 3#
titlelbl3 = tk.Label(encyclopediaframe,bg="#dae8fc",font=("Arial",18),text="Unspeakable Things")
titlelbl3.place(x=220,y=320)

#Book title 4#
titlelbl4 = tk.Label(encyclopediaframe,bg="#dae8fc",font=("Arial",18),text="The Buried Book")
titlelbl4.place(x=620,y=320)

#Description book 1#
descrptlbl1 = tk.Label(encyclopediaframe,bg="#dae8fc",font=("Arial",12),text="A superlative middle volume,\nadding depth and scope without\nsacrificing clarity or theme.",justify="left")
descrptlbl1.place(x=220,y=150)

#Description book 2#
descrptlbl2 = tk.Label(encyclopediaframe,bg="#dae8fc",font=("Arial",12),text="Truly deserving of the accolade\nModern Classic, Michael Lieber's\ncult bestseller The War Hero is\na remarkable achievement - both\ninsightful and elegant, comedic and\ndark.",justify="left")
descrptlbl2.place(x=620,y=150)

#Description book 3#
descrptlbl1 = tk.Label(encyclopediaframe,bg="#dae8fc",font=("Arial",12),text="Vivid, atmospheric, and genuinely\nunsettling, UNSPEAKABLE THINGS\nis a coming-of-age story as you’ve\nnever read it before.",justify="left")
descrptlbl1.place(x=220,y=370)

#Description book 4#
descrptlbl1 = tk.Label(encyclopediaframe,bg="#dae8fc",font=("Arial",12),text="A vivid look at 1950’s farm life\nfrom the political climate,\nprejudice and their daily survival.",justify="left")
descrptlbl1.place(x=620,y=370)

#Image 1 on page#
image1 = Image.open("fiction_TheBrokenRaven.png")#Opening the Image#
resize_image1 = image1.resize((108,162))#Resizing the image using resize()#
img1 = ImageTk.PhotoImage(resize_image1)
#Create label for resized image#
label1 = tk.Label(encyclopediaframe,image=img1)
label1.image = img1
label1.place(x=100,y=100)

#Image 2 on page#
image2 = Image.open("fiction_TheWarHero.png")
resize_image2 = image2.resize((108,162))
img2 = ImageTk.PhotoImage(resize_image2)
#Create label for resized image#
label2 = tk.Label(encyclopediaframe,image=img2)
label2.image = img2
label2.place(x=500,y=100)

#Image 3 on page#
image3 = Image.open("fiction_UnspeakableThings.png")
resize_image3 = image3.resize((108,162))
img3 = ImageTk.PhotoImage(resize_image3)
#Create label for resized image#
label3 = tk.Label(encyclopediaframe,image=img3)
label3.image = img3
label3.place(x=100,y=320)

#Image 4 on page#
image4 = Image.open("fiction_TheBuriedBook.png")
resize_image4 = image4.resize((108,162))
img4 = ImageTk.PhotoImage(resize_image4)
#Create label for resized image#
label4 = tk.Label(encyclopediaframe,image=img4)
label4.image = img4
label4.place(x=500,y=320)

#Detail button for book 1#
detlbtn1 = tk.Button(encyclopediaframe,fg="white",bg="#1ba1e2",text="See Details",command=fbook1_frame)
detlbtn1.place(x=100,y=270)

#Detail button for book 2#
detlbtn2 = tk.Button(encyclopediaframe,fg="white",bg="#1ba1e2",text="See Details",command=fbook2_frame)
detlbtn2.place(x=500,y=270)

#Detail button for book 3#
detlbtn3 = tk.Button(encyclopediaframe,fg="white",bg="#1ba1e2",text="See Details",command=fbook3_frame)
detlbtn3.place(x=100,y=490)

#Detail button for book 4#
detlbtn4 = tk.Button(encyclopediaframe,fg="white",bg="#1ba1e2",text="See Details",command=fbook4_frame)
detlbtn4.place(x=500,y=490)

#Button to go back to types of book page#
bkbtn = tk.Button(encyclopediaframe,fg="white",bg="#1ba1e2",text="Back",command=bktp_frame)
bkbtn.place(x=900,y=490)

#Widgets for Historical Fiction books frame#

#Historical Fiction frame name#
bksinhisfic = tk.Label(historicalframe,bg="#dae8fc",font=("Arial",32),text="Types Of Books In Historical Fiction")
bksinhisfic.place(x=225,y=25)

#Book title 1#
titlelbl1 = tk.Label(historicalframe,bg="#dae8fc",font=("Arial",18),text="The Broken Raven")
titlelbl1.place(x=220,y=100)

#Book title 2#
titlelbl2 = tk.Label(historicalframe,bg="#dae8fc",font=("Arial",18),text="The War Hero")
titlelbl2.place(x=620,y=100)

#Book title 3#
titlelbl3 = tk.Label(historicalframe,bg="#dae8fc",font=("Arial",18),text="Unspeakable Things")
titlelbl3.place(x=220,y=320)

#Book title 4#
titlelbl4 = tk.Label(historicalframe,bg="#dae8fc",font=("Arial",18),text="The Buried Book")
titlelbl4.place(x=620,y=320)

#Description book 1#
descrptlbl1 = tk.Label(historicalframe,bg="#dae8fc",font=("Arial",12),text="A superlative middle volume,\nadding depth and scope without\nsacrificing clarity or theme.",justify="left")
descrptlbl1.place(x=220,y=150)

#Description book 2#
descrptlbl2 = tk.Label(historicalframe,bg="#dae8fc",font=("Arial",12),text="Truly deserving of the accolade\nModern Classic, Michael Lieber's\ncult bestseller The War Hero is\na remarkable achievement - both\ninsightful and elegant, comedic and\ndark.",justify="left")
descrptlbl2.place(x=620,y=150)

#Description book 3#
descrptlbl1 = tk.Label(historicalframe,bg="#dae8fc",font=("Arial",12),text="Vivid, atmospheric, and genuinely\nunsettling, UNSPEAKABLE THINGS\nis a coming-of-age story as you’ve\nnever read it before.",justify="left")
descrptlbl1.place(x=220,y=370)

#Description book 4#
descrptlbl1 = tk.Label(historicalframe,bg="#dae8fc",font=("Arial",12),text="A vivid look at 1950’s farm life\nfrom the political climate,\nprejudice and their daily survival.",justify="left")
descrptlbl1.place(x=620,y=370)

#Image 1 on page#
image1 = Image.open("fiction_TheBrokenRaven.png")#Opening the Image#
resize_image1 = image1.resize((108,162))#Resizing the image using resize()#
img1 = ImageTk.PhotoImage(resize_image1)
#Create label for resized image#
label1 = tk.Label(historicalframe,image=img1)
label1.image = img1
label1.place(x=100,y=100)

#Image 2 on page#
image2 = Image.open("fiction_TheWarHero.png")
resize_image2 = image2.resize((108,162))
img2 = ImageTk.PhotoImage(resize_image2)
#Create label for resized image#
label2 = tk.Label(historicalframe,image=img2)
label2.image = img2
label2.place(x=500,y=100)

#Image 3 on page#
image3 = Image.open("fiction_UnspeakableThings.png")
resize_image3 = image3.resize((108,162))
img3 = ImageTk.PhotoImage(resize_image3)
#Create label for resized image#
label3 = tk.Label(historicalframe,image=img3)
label3.image = img3
label3.place(x=100,y=320)

#Image 4 on page#
image4 = Image.open("fiction_TheBuriedBook.png")
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
bkbtn = tk.Button(historicalframe,fg="white",bg="#1ba1e2",text="Back",command=bktp_frame)
bkbtn.place(x=900,y=490)

#Widgets for Science Fiction books frame#

#Fiction frame name#
bksinscifi = tk.Label(scififrame,bg="#dae8fc",font=("Arial",32),text="Types Of Books In Science Fiction")
bksinscifi.place(x=225,y=25)

#Book title 1#
titlelbl1 = tk.Label(scififrame,bg="#dae8fc",font=("Arial",18),text="The Broken Raven")
titlelbl1.place(x=220,y=100)

#Book title 2#
titlelbl2 = tk.Label(scififrame,bg="#dae8fc",font=("Arial",18),text="The War Hero")
titlelbl2.place(x=620,y=100)

#Book title 3#
titlelbl3 = tk.Label(scififrame,bg="#dae8fc",font=("Arial",18),text="Unspeakable Things")
titlelbl3.place(x=220,y=320)

#Book title 4#
titlelbl4 = tk.Label(scififrame,bg="#dae8fc",font=("Arial",18),text="The Buried Book")
titlelbl4.place(x=620,y=320)

#Description book 1#
descrptlbl1 = tk.Label(scififrame,bg="#dae8fc",font=("Arial",12),text="A superlative middle volume,\nadding depth and scope without\nsacrificing clarity or theme.",justify="left")
descrptlbl1.place(x=220,y=150)

#Description book 2#
descrptlbl2 = tk.Label(scififrame,bg="#dae8fc",font=("Arial",12),text="Truly deserving of the accolade\nModern Classic, Michael Lieber's\ncult bestseller The War Hero is\na remarkable achievement - both\ninsightful and elegant, comedic and\ndark.",justify="left")
descrptlbl2.place(x=620,y=150)

#Description book 3#
descrptlbl1 = tk.Label(scififrame,bg="#dae8fc",font=("Arial",12),text="Vivid, atmospheric, and genuinely\nunsettling, UNSPEAKABLE THINGS\nis a coming-of-age story as you’ve\nnever read it before.",justify="left")
descrptlbl1.place(x=220,y=370)

#Description book 4#
descrptlbl1 = tk.Label(scififrame,bg="#dae8fc",font=("Arial",12),text="A vivid look at 1950’s farm life\nfrom the political climate,\nprejudice and their daily survival.",justify="left")
descrptlbl1.place(x=620,y=370)

#Image 1 on page#
image1 = Image.open("fiction_TheBrokenRaven.png")#Opening the Image#
resize_image1 = image1.resize((108,162))#Resizing the image using resize()#
img1 = ImageTk.PhotoImage(resize_image1)
#Create label for resized image#
label1 = tk.Label(scififrame,image=img1)
label1.image = img1
label1.place(x=100,y=100)

#Image 2 on page#
image2 = Image.open("fiction_TheWarHero.png")
resize_image2 = image2.resize((108,162))
img2 = ImageTk.PhotoImage(resize_image2)
#Create label for resized image#
label2 = tk.Label(scififrame,image=img2)
label2.image = img2
label2.place(x=500,y=100)

#Image 3 on page#
image3 = Image.open("fiction_UnspeakableThings.png")
resize_image3 = image3.resize((108,162))
img3 = ImageTk.PhotoImage(resize_image3)
#Create label for resized image#
label3 = tk.Label(scififrame,image=img3)
label3.image = img3
label3.place(x=100,y=320)

#Image 4 on page#
image4 = Image.open("fiction_TheBuriedBook.png")
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
bkbtn = tk.Button(scififrame,fg="white",bg="#1ba1e2",text="Back",command=bktp_frame)
bkbtn.place(x=900,y=490)

window.mainloop()

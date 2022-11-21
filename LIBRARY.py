from tkinter import *
import tkinter.messagebox as tkMessageBox
import winsound
import tkinter.filedialog

def Books():
   filewin = Toplevel(root)
   label = Label(filewin, text="All books will be shown here")
   label.pack(side = TOP)
def Action():
   filewin = Toplevel(root)
   label = Label(filewin, text="Action books will be shown here")
   label.pack(side = TOP)
def Adventure():
   filewin = Toplevel(root)
   label = Label(filewin, text="Adventure books will be shown here")
   label.pack(side = TOP)
def Fantasy():
   filewin = Toplevel(root)
   label = Label(filewin, text="Fantasy books will be shown here")
   label.pack(side = TOP)
def Sci_Fi():
   filewin = Toplevel(root)
   label = Label(filewin, text="Sci-Fi books will be shown here")
   label.pack(side = TOP)
def Edu():
   filewin = Toplevel(root)
   label = Label(filewin, text="Educataional books will be shown here")
   label.pack(side = TOP)
def About():
   filewin = Toplevel(root)
   label = Label(filewin, text="Information will be shown here")
   label.pack(side = TOP)
def Help():
   filewin = Toplevel(root)
   label = Label(filewin, text="Username is your school e-mail, Password is sent to your Orchlon school e-mail")
   label.pack(side = TOP)
def Und():
   filewin = Toplevel(root)
   label = Label(filewin, text="This program will let you see your rented books from the library. You can also see available books for rent")
   label.pack(side = TOP)
def Search():
    filewin = Toplevel(root)
    label = Label(filewin, text="Enter Book Name")
    label.pack(side = TOP)
    E1=Entry(filewin,bd =5)
    E1.pack(padx=25)
    def book1():
       poi=0
       a=list()
       b=list()
       c=list()
       k=E1.get()
       a.append("Hunger Games")
       a.append("Hobbit")
       a.append("LOTR")
       a.append("Sciecnce")
       a.append("Maths")
       b.append("Action")
       b.append("Adventure")
       b.append("Fantasy")
       b.append("Educational")
       b.append("Educational")
       c.append(12)
       c.append(7)
       c.append(8)
       c.append(3)
       c.append(20)
       a.reverse()
       b.reverse()
       c.reverse()
       for x in range(5):
          if k==a[x]:
             w=Toplevel()
             l1=Label(w, text=(a[x]))
             l1.pack()
             l2=Label(w, text=("Genre:",b[x]))
             l2.pack()
             l3=Label(w, text=("Left:",c[x]))
             l3.pack()
             poi=1
       if poi==0:
             tkMessageBox.showinfo("No book","Not found")
                   
    b67=Button(filewin, text="Search", width=10, command=book1)
    b67.pack(side=BOTTOM)
root = Tk()
menubar = Menu(root)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About Us", command=About)
helpmenu.add_command(label="Help with Login", command=Help)
helpmenu.add_command(label="Understand",command=Und)

helpmenu.add_separator()

helpmenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="Help", menu=helpmenu)
bookmenu = Menu(menubar, tearoff=0)
bookmenu.add_command(label="All Books", command=Books)

bookmenu.add_separator()

bookmenu.add_command(label="Action", command=Action)
bookmenu.add_command(label="Adventure", command=Adventure)
bookmenu.add_command(label="Fantasy", command=Fantasy)
bookmenu.add_command(label="Sci-Fi", command=Sci_Fi)
bookmenu.add_command(label="Educational", command=Edu)
bookmenu.add_command(label="Search by Book Name", command=Search)

menubar.add_cascade(label="Available Books", menu=bookmenu)

v = Label(root, text="LIBRARY", fg ="white", font=("Arial", 50), bg = "light blue")
v.pack()

logo = PhotoImage(file="GIOF1.gif")
i = Label(root, width=100,height=100, image=logo).pack(fill = X)
root.io=3
def meeg():
   root.io=int(var.get())
var = IntVar()
R1 = Radiobutton(root, text="Student", variable=var, value=1, command=meeg)
R2 = Radiobutton(root, text="Teacher", variable=var, value=2, command=meeg)
R1.pack()
R1.pack(pady=10)
R2.pack()
R2.pack(pady=10)

L = Label(root, text="Username", font=("Arial",20))
L.pack(side =LEFT)
L.pack(side = TOP)
u = Entry(root, bd = 5,bg = "light blue")
u.pack(padx = 20)
u.pack(side = TOP)
                            
L1 = Label(root,text="Password", font=("Arial",20))
L1.pack(side = TOP)
p = Entry(root, bd = 5,  show = "*",bg = "light blue")
p.pack(padx = 20)

def login():
    a=u.get()
    b=p.get()
    n=list()
    m=list()
    n.append("mergen")
    n.append("tamir")
    n.append("ami")
    n.append("bilguun")
    m.append("1")
    m.append("2")
    m.append("3")
    m.append("4")
    n.reverse()
    m.reverse()
    l=len(n)
    q=0
    ot=0
    for x in range(l):
       if a==n[x]:
             if b==m[x]:
                   winsound.PlaySound("SystemExit", winsound.SND_ASYNC)
                   q=1
                   if root.io==1:
                         tkMessageBox.showinfo("Student ","Hello, Student kiki emoticon")
                   if root.io==2:
                         tkMessageBox.showinfo("Teacher","Hello, Teacher squint emoticon")
    if root.io==3:
       tkMessageBox.showinfo("Invalid","Please choose one of the options above")
                        
    if q==0:
       if root.io!=3:
          winsound.PlaySound("SystemExit", winsound.SND_ASYNC)
          tkMessageBox.showinfo("Invalid","Wrong Username or Password")
b = Button(root, text="Login", bd= 3,command=login,cursor="circle" )
b.bind('<Return>')
b.pack(pady = 5)

def openInstruktion():
    x = Entry.get(entry)
    tkMessageBox.showinfo("Student",x)
def forgot():
   filewin1 = Toplevel(root)
   label = Label(filewin1, text="Enter your e-mail.")
   label.pack(side=TOP)
   label1 = Label(filewin1, text="E-Mail:")
   label1.pack(side = LEFT)
   entry = Entry(filewin1, bd = 5,bg = "light blue",width=40)
   entry.pack(side = LEFT)
   def openInstruktion():
      x = Entry.get(entry)
      y = str(x)
      f = open('HI.txt', 'a')
      f.write(y)
      if x == "":
         winsound.PlaySound("SystemExit", winsound.SND_ASYNC)
         tkMessageBox.showinfo("Invalid","Please enter your e-mail")
      else:
         tkMessageBox.showinfo("Sent","Your new password has been sent to your e-mail address")
         f.close()
         filewin1.destroy()
   button = Button(filewin1,text="OK", bd =3,command=openInstruktion)
   button.pack(side = LEFT)

FF = Button(root,text="Forgot Password",bd = 3, command = forgot)
FF.pack(side = BOTTOM)
FF.pack(pady=10)

def student():
   tkMessageBox.showinfo("Student", "Hi, Student")
def teacher():
   tkMessageBox.showinfo("Teacher","Hi, Teacher")

root.config(menu=menubar)
root.mainloop()

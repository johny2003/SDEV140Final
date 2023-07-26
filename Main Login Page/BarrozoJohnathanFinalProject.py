#Johnathan Barrozo 7/13/23 SDEV 140 Final Project
#This program is a login page that uses data from signing up for a username and password, and allows user to login via whatever username and password they create when signing up.
from tkinter import *
from tkinter import messagebox
import ast

#main login page when program starts
root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

#defines getting username and password // opens datasheet for username and password entered
def login():
    username=user.get()
    password=code.get()

    file=open('datasheet.txt', 'r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    #print(r.keys())
    #print(r.values())

    #if statement that allows you to see welcome screen once logged in // if user and password is incorrect, screen will prompt the else statement
    if username in r.keys() and password==r[username]:
        screen=Toplevel(root)
        screen.title("Welcome!")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")

        Label(screen,text='Welcome!',bg='#fff',font=('Calibri(Body)',50,'bold')).pack(expand=True)

        screen.mainloop()

    else:
        messagebox.showerror('Invalid', 'invalid username or password')

#defines the signup command for window to appear on screen
def signup_command():
    window=Toplevel(root)
    window.title("Sign up!")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False,False)

    #defines the signup window that allows a user to create an account (obtain their username and password)
    def signup():
        username=user.get()
        password=code.get()
        confirm_password=confirm_code.get()

        if password==confirm_password:
            try:
                file=open('datasheet.txt','r+')
                d=file.read()
                r=ast.literal_eval(d)

                dict2={username:password}
                r.update(dict2)
                file.truncate(0)
                file.close

                file=open('datasheet.txt', 'w')
                w=file.write(str(r))

                messagebox.showinfo('Sign up','Successfully Signed Up!')
                window.destroy()
            except:
                file=open('datasheet.txt', 'w')
                pp=str({'username':'password'})
                file.write(pp)
                file.close()

        else:
            messagebox.showerror('Invalid', "Both Passwords should match.")

    def sign():
        window.destroy()

    #image of sign up page
    img= PhotoImage(file='signup.jpg')
    Label(window,image=img,border=0,bg='white').place(x=50,y=90)

    frame=Frame(window,width=350,height=390,bg='#fff')
    frame.place(x=480,y=50)

    heading=Label(frame,text='Sign up',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
    heading.place(x=100,y=5)

    #this creates the box that says username and allows user to enter a username when signing up
    def on_enter(e):
        user.delete(0, 'end')
    def on_leave(e):
        if user.get()=='':
            user.insert(0, 'Username')

    user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0, 'Username')
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

    #this creates the box that says password, and allows user to enter password when signing up
    def on_enter(e):
        code.delete(0, 'end')
    def on_leave(e):
        if code.get()=='':
            code.insert(0, 'Password')

    code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0, 'Password')
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

    #this creates the confirm password box for signup
    def on_enter(e):
        confirm_code.delete(0, 'end')
    def on_leave(e):
        if confirm_code.get()=='':
            confirm_code.insert(0, 'Confirm Password')

    confirm_code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    confirm_code.place(x=30,y=220)
    confirm_code.insert(0, 'Confirm Password')
    confirm_code.bind("<FocusIn>", on_enter)
    confirm_code.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

    #button to sign up
    Button(frame,width=39,pady=7,text='Sign up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=280)
    label=Label(frame,text='I have an account',fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
    label.place(x=90,y=340)

    #button to sign in
    signin=Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=sign)
    signin.place(x=200,y=340)

    window.mainloop()

#image for login screen
img = PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Log in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

#this allows user to enter their username to login
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0, 'Username')



user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#this allows user to enter password to login
def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0, 'Password')



code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

Button(frame,width=39,pady=7,text='Log in',bg='#57a1f8',fg='white',border=0,command=login).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

sign_up= Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup_command)
sign_up.place(x=215,y=270)


root.mainloop()
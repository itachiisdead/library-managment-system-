from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


login =Tk()
login.title("login")
login.resizable(False,False)

w=1200
h=650
screenwidth=login.winfo_screenwidth()
screenhiget=login.winfo_screenheight()
x=int((screenwidth-w)/2)
y=int((screenhiget-h)/2)
#root.geometry("600x400")
#root.configure(bg='#696969')
  
img=Image.open('pics/back_ground.jpg')
img=img.resize((1200,650))   
test=ImageTk.PhotoImage(img)
login.geometry(f'{w}x{h}+{x}+{y}')
lb1=Label(login,ima=test)
lb1.place(x=0,y=0)

def go_to_home_page():
    login.destroy()
    import home

    

def login_fun():
    username = "admin"
    password = "123456"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        go_to_home_page()
    else:
        messagebox.showerror(title="Error", message="Invalid login.")


username_lbl=Label(login,text='  Username',fg='beige',font=("georgia",18,'bold'),bg='tan4',pady=30)   
username_lbl.place(relx=0.25, rely=0.4, relwidth=0.2, relheight=0.08)

password_lbl=Label(login,text='  Password',fg='beige',font=("georgia",18,'bold'),bg='tan4',pady=30)
password_lbl.place(relx=0.25, rely=0.5, relwidth=0.2, relheight=0.08)
    
username_entry=Entry(login,font=("Arial,44"),fg='black')
username_entry.place(relx=0.5, rely=0.412, relwidth=0.2, relheight=0.05)
    
password_entry=Entry(login,show='*')
password_entry.place(relx=0.5, rely=0.512, relwidth=0.2, relheight=0.05)
    
btn_login=Button(login,text='Login',fg='beige',bg='darkslategrey',
                 font=("Arial",14,'bold'),relief='ridge',borderwidth=4,command=login_fun)
btn_login.place(relx=0.4, rely=0.65, relwidth=0.2, relheight=0.08)
    

button = Button(login)
img = PhotoImage(file="pics/login.png")
button.config(image=img)
button.place(relx=0.45, rely=0.2, relwidth=0.06, relheight=0.11)
    
#update
#login_frame.pack()
            


#create_login_frame()
login.mainloop()      







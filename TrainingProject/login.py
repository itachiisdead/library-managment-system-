from tkinter import*
from PIL import ImageTk, Image
from tkinter import ttk
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
  
img=Image.open('images/back.png')
print(img.size) 
img=img.resize((1200,650))   
test=ImageTk.PhotoImage(img)
login.geometry(f'{w}x{h}+{x}+{y}')
lb1=Label(login,ima=test)
lb1.place(x=0,y=0)

def go_to_home_page():
    login.destroy()
    import home
    

def create_login_frame():
    login_frame=Frame(login)

    login_frame.configure(bg='#808080')
    print(login_frame.size)

    lb1=Label(login_frame,text='Username',font=("Arial,30"),bg='#808080',pady=30)
    
    lb1.grid(row=0,column=0)

    lb2=Label(login_frame,text='Password',font=("Arial,30"),bg='#808080',pady=30)
    lb2.grid(row=1,column=0)
    txt_user=Entry(login_frame,font=("Arial,44"),fg='black')
    txt_user.grid(row=0,column=1,padx=30)
    txt_pass=Entry(login_frame,show='*',font=("Arial,44"))
    txt_pass.grid(row=1,column=1,padx=30)
    btn_login=Button(login_frame,text='Login',font=("Arial,30"),command=go_to_home_page)
    btn_login.grid(row=3,column=0,columnspan=2,pady=30)
    login_frame.place(anchor='center',relx=0.5,rely=0.5)

#login_frame.pack()
            
create_login_frame()


#create_login_frame()
login.mainloop()



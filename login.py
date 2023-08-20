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
  
img=Image.open('pics/back_ground.jpg')
img=img.resize((1200,650))   
test=ImageTk.PhotoImage(img)
login.geometry(f'{w}x{h}+{x}+{y}')
lb1=Label(login,ima=test)
lb1.place(x=0,y=0)

def go_to_home_page():
    login.destroy()
    import home
    

lb1=Label(login,text='  Username',fg='beige',font=("georgia",18,'bold'),bg='tan4',pady=30)   
lb1.place(relx=0.25, rely=0.4, relwidth=0.2, relheight=0.08)

lb2=Label(login,text='  Password',fg='beige',font=("georgia",18,'bold'),bg='tan4',pady=30)
lb2.place(relx=0.25, rely=0.5, relwidth=0.2, relheight=0.08)
    
txt_user=Entry(login,font=("Arial,44"),fg='black')
txt_user.place(relx=0.5, rely=0.412, relwidth=0.2, relheight=0.05)
    
txt_pass=Entry(login,show='*')
txt_pass.place(relx=0.5, rely=0.512, relwidth=0.2, relheight=0.05)
    
btn_login=Button(login,text='Login',fg='beige',bg='darkslategrey',font=("Arial",14,'bold'),relief='ridge',borderwidth=4,command=go_to_home_page)
btn_login.place(relx=0.4, rely=0.65, relwidth=0.2, relheight=0.08)
    

button = Button(login)
img = PhotoImage(file="pics/login.png")
button.config(image=img)
button.place(relx=0.45, rely=0.2, relwidth=0.06, relheight=0.11)
    
#update
#login_frame.pack()
            


#create_login_frame()
login.mainloop()



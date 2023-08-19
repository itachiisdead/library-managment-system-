
from tkinter import*
from PIL import ImageTk, Image
from tkinter import ttk
home =Tk()
home.title("Home Page")
home.resizable(False,False)
font=("Arial,30")
w=1200
h=650
screenwidth=home.winfo_screenwidth()
screenhiget=home.winfo_screenheight()
x=int((screenwidth-w)/2)
y=int((screenhiget-h)/2)
#root.geometry("600x400")
#root.configure(bg='#696969')
  
img=Image.open('images/back.png')
print(img.size) 
img=img.resize((1200,650))   
test=ImageTk.PhotoImage(img)
home.geometry(f'{w}x{h}+{x}+{y}')
lb1=Label(home,ima=test)
lb1.place(x=0,y=0)

def create_home_frame():
    home_frame=Frame(home)
    home_frame.configure(bg='black')
    btn1=Button(home_frame,text="issue Books",font=font,bg='#808080')
    btn1.grid(row=0,column=0,columnspan=2,pady=5,sticky="news")
    btn2=Button(home_frame,text="Return Books",font=font,bg='#808080')
    btn2.grid(row=1,column=0,columnspan=2,pady=5,sticky="news")
    btn3=Button(home_frame,text="List of Books",font=font,bg='#808080')
    btn3.grid(row=2,column=0,columnspan=2,pady=5,sticky="news")
    btn4=Button(home_frame,text="Borrowed Books",font=font,bg='#808080')
    btn4.grid(row=3,column=0,columnspan=2,pady=5,sticky="news")
    home_frame.place(anchor='center',relx=0.5,rely=0.5)
create_home_frame()



home.mainloop()
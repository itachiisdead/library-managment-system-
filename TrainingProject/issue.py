from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image  
IssueWin = Tk()
IssueWin.title("Issue Book")
IssueWin.resizable(False,False)

def set_background():
    img=Image.open('images/back.png')
    bag=ImageTk.PhotoImage(img)
    lab=Label(IssueWin,ima=bag)
    img=img.resize((1200,650))
    lab.image=bag
    lab.place(x=0,y=0)
def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth() 
    screen_height = window.winfo_screenheight()
    height = window.winfo_height()
    width = window.winfo_width()
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    window.geometry(f"{width}x{height}+{x}+{y}")
def submit_issue():
    book_id = txt_Id.get()
    title = txt_title.get()
    author = txt_Author.get()
    genre = txt_dueme.get()

    if book_id and title and author and genre:
        messagebox.showinfo("Success", "Issue submitted successfully!")        
    else:
        messagebox.showerror("Error", "Please fill in all fields.")
        
def back():
      IssueWin.destroy()
      import home
def backButton():
   backbtn=Button(IssueWin,text='back',bg='blue',fg='white',font=(20),command=back) 
   backbtn.place(relx=0.4, rely=0.05, relwidth=0.2, relheight=0.1)
def createIssueFrame():
    frame = Frame(IssueWin,bg='black')
   # frame.configure(bg='#696969')
    frame.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.7)

    # Book ID
    lb1 = Label(frame, text="Book ID:", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.05, relheight=0.08)

    txt_Id = Entry(frame)
    txt_Id.place(relx=0.3, rely=0.05, relwidth=0.62, relheight=0.06)

    # Title
    lb2 = Label(frame, text="Book Title:", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.15, relheight=0.08)

    txt_title = Entry(frame)
    txt_title.place(relx=0.3, rely=0.15, relwidth=0.62, relheight=0.06)

    # Book Author
    lb3 = Label(frame, text="Author:", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.25, relheight=0.08)

    txt_Author = Entry(frame)
    txt_Author.place(relx=0.3, rely=0.25, relwidth=0.62, relheight=0.06)

    # student name
    lb4 = Label(frame, text="Student Name :", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.35, relheight=0.08)

    txt_name= Entry(frame)
    txt_name.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.06)
    # phone
    lb5 = Label(frame, text="phone :", bg='black', fg='white')
    lb5.place(relx=0.05, rely=0.45, relheight=0.08)

    txt_phone = Entry(frame)
    txt_phone.place(relx=0.3, rely=0.45, relwidth=0.62, relheight=0.06)
    # Date borrow
    lb6 = Label(frame, text="Date Borrowed ", bg='black', fg='white')
    lb6.place(relx=0.05, rely=0.55, relheight=0.08)

    txt_date= Entry(frame)
    txt_date.place(relx=0.3, rely=0.55, relwidth=0.62, relheight=0.06)

    # Date Due
    lb7 = Label(frame, text="Date Due :", bg='black', fg='white')
    lb7.place(relx=0.05, rely=0.65, relheight=0.08)

    txt_due= Entry(frame)
    txt_due.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.06)
    
    
    # Submit Button
    submitBtn = Button(frame, text="Submit", bg='green', fg='white')
    submitBtn.place(relx=0.4, rely=0.8, relwidth=0.2, relheight=0.1)

   # frame.pack()
set_background()
IssueWin.geometry("1200x650")

set_background()

createIssueFrame()
backButton()
center_window(IssueWin)

IssueWin.mainloop()
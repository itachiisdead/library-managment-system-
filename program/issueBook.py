from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from connection import ListOfBorrowedBook

from importlib import reload

width=1200
height=650
Issue = Tk()
Issue .title("Issue book")
Issue.resizable(False,False)
#Issue .geometry(f"{width}x{height}")

#background image
img_bg=Image.open('pics/back_ground.jpg')
bck_bg=ImageTk.PhotoImage(img_bg)    
pic_label=Label(Issue,image=bck_bg)
pic_label.place(x=0,y=0 )

def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth() 
    screen_height = window.winfo_screenheight()
    width=1200
    height=650
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    window.geometry(f"{width}x{height}+{x}+{y}")
center_window(Issue)
connection = ListOfBorrowedBook("library.db")

"""   Variables   """
book_id= IntVar()
book_title=StringVar()
author=StringVar()
reader_name=StringVar()
date_borrow=StringVar()
date_due=StringVar()
phone=StringVar()

def back():
      Issue.destroy()
      import home
      reload(home)

   
def display_book_added():
    messagebox.showinfo("Success" ,"Issue submitted successfully!")
   
def display_book_updated():
    messagebox.showinfo('System','record sucessfully updated')

def clear():
    book_id.set("")
    book_title.set("")
    author.set("")
    reader_name.set("")
    date_borrow.set("")
    date_due.set("")
    phone.set("")

         
      
def getdata(event):
    selected_row=tree.focus()
    data=tree.item(selected_row)
    global row
    row=data["values"]
    book_id.set(row[0])
    book_title.set(row[1])
    author.set(row[2])
    reader_name.set(row[3])
    date_borrow.set(row[4])
    date_due.set(row[5])
    phone.set(row[6])

def display():
    tree.delete(*tree.get_children())
    for row in connection.fetch():
        tree.insert("",END,values=row)

def submit_book():
    if txt_Id.get()=="" or txt_title.get()=="" or txt_Author.get()=="" or txt_name.get()=="" or txt_phone.get()=="" or txt_bDate.get()=="" or txt_DDate.get()=="":
        messagebox.showerror("Error! please fill all entries.")
    else:
        connection.submit_borrowed(txt_Id.get(),txt_title.get(),txt_Author.get(),txt_name.get(),txt_bDate.get(), txt_DDate.get(),txt_phone.get())
        display_book_added()
    clear()
    display()
    
    

        
def Update():
    if txt_Id.get() == "" or txt_title.get() == "" or txt_Author.get() == "" or txt_name.get()=="" or txt_phone.get()=="" or txt_bDate.get()=="" or txt_DDate.get()=="" :
        messagebox.showerror("Error", "Please fill all entries.")
    else:
        connection.update_borroweded(row[0], txt_title.get(), txt_Author.get(),txt_name.get(),txt_bDate.get(), txt_DDate.get(),txt_phone.get())
        display_book_updated()
    clear()
    display()


def display_book_returned():
    messagebox.showinfo('success','book returned!')

    
def return_book_fun():
    connection.returnBook(row[0])
    display_book_returned()
    clear()
    display()

#back button
backbtn=Button(Issue,text='back',bg='indianred4',fg='white',font=('purisa',18),command=back) 
backbtn.place(relx=0.75, rely=0.93, relwidth=0.14, relheight=0.06)

#create frame 
frame = Frame(Issue,bg='slategrey')
frame.place(relx=0.1,rely=0.06,relwidth=0.8,relheight=0.85)

#create title 
title_lbl= Label(frame, text="list of borrowed books: ", bg='slategrey', fg='beige',font=('georgia',16,'bold'))
title_lbl.place(relx=0.02, rely=0.01, relheight=0.08)
  
# Book ID
lb1 = Label(frame, text="Book ID:", bg='slategrey', fg='white',font=('georgia',10,'bold'))
lb1.place(relx=0.05, rely=0.74, relheight=0.08)
   #entry
txt_Id = Entry(frame,textvariable=book_id)
txt_Id.place(relx=0.02, rely=0.8, relwidth=0.15, relheight=0.06)


# Title 
lb2 = Label(frame, text="Book Title:", bg='slategrey', fg='white',font=('georgia',10,'bold'))
lb2.place(relx=0.25, rely=0.74, relheight=0.08)
    #entry
txt_title = Entry(frame,textvariable=book_title)
txt_title.place(relx=0.23, rely=0.8, relwidth=0.15, relheight=0.06)

# Book Author
lb3 = Label(frame, text="Author:", bg='slategrey', fg='white',font=('georgia',10,'bold'))
lb3.place(relx=0.45, rely=0.74, relheight=0.08)
txt_Author = Entry(frame,textvariable=author)
txt_Author.place(relx=0.43, rely=0.8, relwidth=0.15, relheight=0.06)

 # Name
lb4 = Label(frame, text="reader Name :", bg='slategrey', fg='white',font=('georgia',10,'bold'))
lb4.place(relx=0.65, rely=0.74, relheight=0.08)
    #entry
txt_name= Entry(frame,textvariable=reader_name)
txt_name.place(relx=0.63, rely=0.8, relwidth=0.15, relheight=0.06)
 
 # phone
lb5 = Label(frame, text="phone:", bg='slategrey', fg='white',font=('georgia',10,'bold'))
lb5.place(relx=0.18, rely=0.86, relheight=0.08)
   #entry
txt_phone = Entry(frame,textvariable=phone)
txt_phone.place(relx=0.13, rely=0.93, relwidth=0.15, relheight=0.06)


 # Date borrow
lb6 = Label(frame, text="Date borrowed:", bg='slategrey', fg='white',font=('georgia',10,'bold'))
lb6.place(relx=0.34, rely=0.86, relheight=0.08)
    #entry
txt_bDate= Entry(frame,textvariable=date_borrow)
txt_bDate.place(relx=0.33, rely=0.93, relwidth=0.15, relheight=0.06)
 
 
# Date Due
lb7 = Label(frame, text="Date Due:", bg='slategrey', fg='white',font=('georgia',10,'bold'))
lb7.place(relx=0.58, rely=0.86, relheight=0.08)
    #entry
txt_DDate= Entry(frame,textvariable=date_due)
txt_DDate.place(relx=0.56, rely=0.93, relwidth=0.15, relheight=0.06)
 

#buttons

#add button
add_button=Button(frame,text='Issue',bg='seagreen',fg='white',font=('georgia',12),command=submit_book)
add_button.place(relx=0.85, rely=0.795, relwidth=0.1, relheight=0.05)

#update button
update_button=Button(frame,text='Update',bg='brown',fg='white',font=('georgia',12),command=Update)
update_button.place(relx=0.85, rely=0.855, relwidth=0.1, relheight=0.05)

#return botton
return_but=Button(frame,text="return book",bg='brown',fg='white',font=('georgia',12),command=return_book_fun)
return_but.place(relx=0.85, rely=0.915, relwidth=0.1, relheight=0.05)


 # Create the Treeview widget
tree = ttk.Treeview(frame, columns=("Book ID", "Book Title", "Book Author", "Name","Date borrowed","Date Due","phone"), 
                    show="headings",height=1)
tree.pack(fill=BOTH, expand=True,pady=80)

   # Define column headings
tree.heading("Book ID", text="Book ID")
tree.heading("Book Title", text="Book Title")
tree.heading("Book Author", text="Book Author")
tree.heading("Name", text="Name")
tree.heading("Date borrowed", text="Date borrowed")
tree.heading("Date Due", text="Date Due")
tree.heading("phone", text="Phone")

   # Set column widths

 
tree.column('Book ID',width=70)
tree.column('Book Title',width=100)
tree.column('Book Author',width=100)
tree.column('Name',width=70)
tree.column('Date borrowed',width=150)
tree.column('Date Due',width=120)
tree.column('phone',width=70)
tree.bind("<ButtonRelease-1>",getdata)


 # Create scrollbar
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
display()



Issue .mainloop()
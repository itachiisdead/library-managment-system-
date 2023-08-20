from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
width=1200
height=650
Issue = Tk()
Issue .title("Issue book")
Issue.resizable(False,False)
#Issue .geometry(f"{width}x{height}")

def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth() 
    screen_height = window.winfo_screenheight()
    width=1200
    height=650
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    window.geometry(f"{width}x{height}+{x}+{y}")
   
def display_book_added():
    messagebox.showinfo("Success" ,"Issue submitted successfully!")
   
def display_book_updated():
    tkinter.messagebox.showinfo('System','record sucessfully updated')


def back():
      Issue.destroy()
      import home    
      
def backButton():
   backbtn=Button(Issue,text='back',bg='indianred4',fg='white',font=('purisa',18),command=back) 
   backbtn.place(relx=0.75, rely=0.93, relwidth=0.14, relheight=0.06)    
  
def Issue_frame():
    
    def add_book_details():
       book_name=txt_title.get()
       print(book_name) 
    
    frame = Frame(Issue,bg='slategrey')
    frame.place(relx=0.1,rely=0.06,relwidth=0.8,relheight=0.85)
  
    title_lbl= Label(frame, text="list of borrowed books: ", bg='slategrey', fg='beige',font=('georgia',16,'bold'))
    title_lbl.place(relx=0.02, rely=0.01, relheight=0.08)
  
    # Book ID
    lb1 = Label(frame, text="Book ID:", bg='slategrey', fg='white',font=('georgia',10,'bold'))
    lb1.place(relx=0.05, rely=0.74, relheight=0.08)

    txt_Id = Entry(frame)
    txt_Id.place(relx=0.02, rely=0.8, relwidth=0.15, relheight=0.06)


    # Title
    lb2 = Label(frame, text="Book Title:", bg='slategrey', fg='white',font=('georgia',10,'bold'))
    lb2.place(relx=0.25, rely=0.74, relheight=0.08)

    txt_title = Entry(frame)
    txt_title.place(relx=0.23, rely=0.8, relwidth=0.15, relheight=0.06)

    # Book Author
    lb3 = Label(frame, text="Author:", bg='slategrey', fg='white',font=('georgia',10,'bold'))
    lb3.place(relx=0.45, rely=0.74, relheight=0.08)

    txt_Author = Entry(frame)
    txt_Author.place(relx=0.43, rely=0.8, relwidth=0.15, relheight=0.06)

    # Name
    lb4 = Label(frame, text="Name :", bg='slategrey', fg='white',font=('georgia',10,'bold'))
    lb4.place(relx=0.65, rely=0.74, relheight=0.08)

    txt_name= Entry(frame)
    txt_name.place(relx=0.63, rely=0.8, relwidth=0.15, relheight=0.06)
    
    # phone
    lb5 = Label(frame, text="phone:", bg='slategrey', fg='white',font=('georgia',10,'bold'))
    lb5.place(relx=0.18, rely=0.86, relheight=0.08)

    txt_phone = Entry(frame)
    txt_phone.place(relx=0.13, rely=0.93, relwidth=0.15, relheight=0.06)


    # Date borrow
    lb6 = Label(frame, text="Date borrowed:", bg='slategrey', fg='white',font=('georgia',10,'bold'))
    lb6.place(relx=0.34, rely=0.86, relheight=0.08)

    txt_bDate= Entry(frame)
    txt_bDate.place(relx=0.33, rely=0.93, relwidth=0.15, relheight=0.06)
    
    
   # Date Due
    lb7 = Label(frame, text="Date Due:", bg='slategrey', fg='white',font=('georgia',10,'bold'))
    lb7.place(relx=0.58, rely=0.86, relheight=0.08)

    txt_DDate= Entry(frame)
    txt_DDate.place(relx=0.56, rely=0.93, relwidth=0.15, relheight=0.06)
    #add button
    add_button=Button(frame,text='Sumbit',command=lambda:[add_book_details(),display_book_added()],bg='seagreen',fg='white',font=('georgia',10))
    add_button.place(relx=0.85, rely=0.8, relwidth=0.1, relheight=0.08)

    #remove button
    remove_button=Button(frame,text='Update',command=display_book_updated,bg='brown',fg='white',font=('georgia',10))
    remove_button.place(relx=0.85, rely=0.9, relwidth=0.1, relheight=0.08)


    # Create the Treeview widget
    tree = ttk.Treeview(frame, columns=("Book ID", "Book Title", "Book Author", "Name","phone","Date borrowed","Date Due"), show="headings",height=1)
    tree.pack(fill=BOTH, expand=True,pady=80)

      # Define column headings
    tree.heading("Book ID", text="Book ID")
    tree.heading("Book Title", text="Book Title")
    tree.heading("Book Author", text="Book Author")
    tree.heading("Name", text="Name")
    tree.heading("phone", text="Phone")
    tree.heading("Date borrowed", text="Date borrowed")
    tree.heading("Date Due", text="Date Due")

      # Set column widths

    
    tree.column('Book ID',width=70)
    tree.column('Book Title',width=100)
    tree.column('Book Author',width=100)
    tree.column('Name',width=70)
    tree.column('phone',width=70)
    tree.column('Date borrowed',width=150)
    tree.column('Date Due',width=120)
    # Create scrollbar
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)



#background image
img_bg=Image.open('pics/back_ground.jpg')
bck_bg=ImageTk.PhotoImage(img_bg)    
pic_label=Label(Issue,image=bck_bg)
pic_label.place(x=0,y=0 )

center_window(Issue)  

backButton()
Issue_frame()


Issue .mainloop()
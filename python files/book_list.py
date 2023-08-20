from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk

book_list = Tk()
book_list .title("List of books")
book_list.resizable(False,False)

#center widow in the screen
def booklist_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth() 
    screen_height = window.winfo_screenheight()
    width=1200
    height=650
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    window.geometry(f"{width}x{height}+{x}+{y}")
#display message box for the added book   
def display_book_added():
  messagebox.showinfo('success','the book has been added!')
#display message box for the removed book
def display_book_removed():
    messagebox.showinfo('success','the book has been removed!')
#display message box for the updated book    
def display_book_updated():
    messagebox.showinfo('success','the book has been updated!')    
#function for the back to home button
def back():
      book_list.destroy()
      import home    
      
def backButton():
   backbtn=Button(book_list,text='back',bg='indianred4',fg='white',font=('purisa',20),command=back) 
   backbtn.place(relx=0.75, rely=0.87, relwidth=0.17, relheight=0.09)    
 
#create the main frame
def create_book_list_Frame():
    
    def add_book_details():
       book_name=txt_title.get()
       print(book_name) 

    
    frame = Frame(book_list,bg='slategrey')
    frame.place(relx=0.1,rely=0.15,relwidth=0.8,relheight=0.7)
  
    title_lbl= Label(frame, text="list of books available: ", bg='slategrey', fg='beige',font=('georgia',16,'bold'))
    title_lbl.place(relx=0.02, rely=0.01, relheight=0.08)
  
    # Book ID
    lb1 = Label(frame, text="Book ID:", bg='slategrey', fg='ivory',font=('georgia',10,'bold'))
    lb1.place(relx=0.05, rely=0.8, relheight=0.08)

    txt_Id = Entry(frame)
    txt_Id.place(relx=0.02, rely=0.88, relwidth=0.15, relheight=0.06)


    # Title
    lb2 = Label(frame, text="Book Title:", bg='slategrey', fg='ivory',font=('georgia',10,'bold'))
    lb2.place(relx=0.25, rely=0.8, relheight=0.08)

    txt_title = Entry(frame)
    txt_title.place(relx=0.23, rely=0.88, relwidth=0.15, relheight=0.06)



    # Book Author
    lb3 = Label(frame, text="Author:", bg='slategrey', fg='ivory',font=('georgia',10,'bold'))
    lb3.place(relx=0.45, rely=0.8, relheight=0.08)

    txt_Author = Entry(frame)
    txt_Author.place(relx=0.43, rely=0.88, relwidth=0.15, relheight=0.06)

    # genre
    lb4 = Label(frame, text="genre :", bg='slategrey', fg='ivory',font=('georgia',10,'bold'))
    lb4.place(relx=0.65, rely=0.8, relheight=0.08)

    txt_name= Entry(frame)
    txt_name.place(relx=0.63, rely=0.88, relwidth=0.15, relheight=0.06)
    
    #add button
    add_button=Button(frame,text='add',command=lambda:[add_book_details(),display_book_added()],bg='brown',fg='white',font=('georgia',10))
    add_button.place(relx=0.85, rely=0.79, relwidth=0.09, relheight=0.05)

    #update button
    update_button=Button(frame,text='update',command=display_book_updated,bg='brown',fg='white',font=('georgia',10))
    update_button.place(relx=0.85, rely=0.85, relwidth=0.09, relheight=0.05)
    
    #remove button
    remove_button=Button(frame,text='remove',command=display_book_removed,bg='brown',fg='white',font=('georgia',10))
    remove_button.place(relx=0.85, rely=0.912, relwidth=0.09, relheight=0.05)


    # Create the Treeview widget
    tree = ttk.Treeview(frame, columns=("Book ID", "Book Title", "Book Author", "Genre"), show="headings",height=1)
    tree.pack(fill=BOTH, expand=True,pady=50)

    # Define column headings
    tree.heading("Book ID", text="Book ID")
    tree.heading("Book Title", text="Book Title")
    tree.heading("Book Author", text="Book Author")
    tree.heading("Genre", text="Genre")

    # Set column widths
    tree.column("Book ID", width=100, anchor=CENTER)
    tree.column("Book Title", width=200, anchor=W)
    tree.column("Book Author", width=150, anchor=W)
    tree.column("Genre", width=100, anchor=W)


    # Create scrollbar
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)
    

#background image
img_bg=Image.open('pics/back_ground.jpg')
bck_bg=ImageTk.PhotoImage(img_bg)    
pic_label=Label(book_list,image=bck_bg)
pic_label.place(x=0,y=0 )

#function calls
booklist_window(book_list)  
backButton()
create_book_list_Frame()

book_list .mainloop()



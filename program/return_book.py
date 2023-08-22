from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from connection import ListOfBorrowedBook

return_book=Tk()
return_book.title("Return Book")

def returnbook_window(root):
    root.update_idletasks()
    screen_width = root.winfo_screenwidth() 
    screen_height = root.winfo_screenheight()
    width=1200
    height=650
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

return_book.resizable('false','false')
img_bg=Image.open('pics/back_ground.jpg')
bck_bg=ImageTk.PhotoImage(img_bg)    
pic_label=Label(return_book,image=bck_bg)
pic_label.place(x=0,y=0 )

returnbook_window(return_book)
connection = ListOfBorrowedBook("library.db")

def back():
      return_book.destroy()
      import home

def go_to_borrowbook_page():
    return_book.destroy()
    import issueBook

def display_book_retured():
    messagebox.showinfo('System','book has been sucessfully returned')

def display_book_returned():
    messagebox.showinfo('success','book returned!')

def clear():
    book_id.set("")
    book_title.set("")
    author.set("")
    student_name.set("")
    date_borrowed.set("")
    date_due.set("")
    phone.set("")
    
def return_book_fun():
    connection.returnBook(row[0])
    display_book_returned()
    clear()

    
#create frame
frame = Frame(return_book,bg='slategrey')
frame.place(relx=0.1,rely=0.2,relwidth=0.7,relheight=0.6)

#retur book title label
title_lbl= Label(frame, text="return book ", bg='slategrey', fg='beige',font=('georgia',18,'bold'))
title_lbl.place(relx=0.02, rely=0.03, relheight=0.08)

#book id label
B_idl=Label(return_book,text="Book Id:",font='8',bg='slategrey', fg='ivory').place(x=300,y=200)
B_idE=Entry(font='10').place(x=450,y=200)

#book name label
B_namel=Label(return_book,text="Book Name:",font='8',bg='slategrey', fg='ivory').place(x=300,y=250)
B_nameE=Entry(font='10').place(x=450,y=250)

#book author label
B_authorl=Label(return_book,text="Author:",font='8',bg='slategrey', fg='ivory').place(x=300,y=300)
B_authorE=Entry(font='10').place(x=450,y=300)

#student name label
Std_namel=Label(return_book,text="Student Name:",font='8',bg='slategrey', fg='ivory').place(x=300,y=350)
Std_nameE=Entry(font='10').place(x=450,y=350)

#return book button
return_but=Button(return_book,text="return book",bg='brown',fg='white',
                  font=('georgia',12),command=return_book_fun).place(x=770,y=230,relwidth=0.12, relheight=0.05 )
#borrowed books button
list_frame_but=Button(return_book,text="Borrowed Books",bg='brown',fg='white',
                      font=('georgia',12),command=go_to_borrowbook_page).place(x=770,y=270 ,relwidth=0.12, relheight=0.05)
#back button
back_but=Button(return_book,text='Back',bg='indianred4',fg='white',font=('georgia',19)
                ,relief='ridge',borderwidth=4,command=back)
back_but.place(x=500,y=450,relwidth=0.12, relheight=0.08)


if __name__ == '__main__':
    return_book
return_book.mainloop()

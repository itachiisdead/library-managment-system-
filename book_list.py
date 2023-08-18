from tkinter import *
from PIL import ImageTk,Image
width=1200
height=650
book_list = Tk()
book_list .title("List of books")
#book_list .geometry(f"{width}x{height}")

def booklist_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth() 
    screen_height = window.winfo_screenheight()
    width=1200
    height=650
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    window.geometry(f"{width}x{height}+{x}+{y}")
   
def display_book_added():
  messagebox.showinfo('success','the book has been added!')
   
def display_book_removed():
    messagebox.showinfo('success','the book has been removed!')
 
def add_book_details():
    book_name=txt_bookname.get()
    print(book_name)
    
booklist_window(book_list)  
  
#background image
img_bg=Image.open('pics/back_ground.jpg')
bck_bg=ImageTk.PhotoImage(img_bg)    
pic_label=Label(book_list,image=bck_bg)
pic_label.place(x=0,y=0 )
    

#labels
lbl=Label(book_list,text="list of books",bg='black',fg='brown',font=('Arial',16,'bold'))
lbl.pack()


#buttons
back_botton=Button(book_list,text ='back to home',bg='brown',fg='white',font=('Arial',10))
back_botton.pack()

add_button=Button(book_list,text='add book',command=lambda:[add_book_details(),display_book_added()],bg='brown',fg='white',font=('Arial',10))
add_button.pack()

remove_button=Button(book_list,text='remove book',command=display_book_removed,bg='brown',fg='white',font=('Arial',10))
remove_button.pack()

#entries
txt_bookname=Entry(book_list)
txt_bookname.pack()


book_list .mainloop()



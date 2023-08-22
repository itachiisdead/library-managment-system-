from tkinter import*
from PIL import ImageTk, Image
from tkinter import ttk
from importlib import reload


home =Tk()
home.title("Home Page")
home.resizable(False,False)
font=("verdana",18)
w=1200
h=650
screenwidth=home.winfo_screenwidth()
screenhiget=home.winfo_screenheight()
x=int((screenwidth-w)/2)
y=int((screenhiget-h)/2)
#root.geometry("600x400")
#root.configure(bg='#696969')
#update

img=Image.open('pics/back_ground.jpg')
print(img.size) 
img=img.resize((1200,650))   
test=ImageTk.PhotoImage(img)
home.geometry(f'{w}x{h}+{x}+{y}')
lb1=Label(home,ima=test)
lb1.place(x=0,y=0)


def go_to_issue_page():
    home.destroy()
    import issueBook
    
def go_to_booklist_page():
    home.destroy()
    import book_list 
    reload(book_list)

  
issue_btn=Button(home,text="issue Books",font=font,bg='darkslategrey',relief='ridge',borderwidth=4,command=go_to_issue_page)
issue_btn.place(relx=0.5, rely=0.37, relwidth=0.22, relheight=0.09)


return_btn=Button(home,text="Return Books",font=font,bg='darkslategrey',relief='ridge',borderwidth=4,command=go_to_issue_page)
return_btn.place(relx=0.2, rely=0.37, relwidth=0.22, relheight=0.09)

list_btn=Button(home,text="List of Books",font=font,bg='darkslategrey',relief='ridge',borderwidth=4,command=go_to_booklist_page)
list_btn.place(relx=0.2, rely=0.5, relwidth=0.22, relheight=0.09)

borrow_btn=Button(home,text="Borrowed Books",font=font,bg='darkslategrey',relief='ridge',borderwidth=4,command=go_to_issue_page)
borrow_btn.place(relx=0.5, rely=0.5, relwidth=0.22, relheight=0.09)
    


home.mainloop()    


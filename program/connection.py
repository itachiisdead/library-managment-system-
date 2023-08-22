import sqlite3

class ListBook:
    def __init__(self,database):
        self.con=sqlite3.connect(database)
        self.cur=self.con.cursor()
        sql= """
        CREATE TABLE IF NOT EXISTS list_of_books(
            book_id Integer Primary Key,
            book_title text,
            author text,
            genre text
            )
        """
        self.cur.execute(sql)
        self.con.commit()
        
        
    def addBook(self,book_id,book_title,author,genre):
        self.cur.execute("insert into list_of_books values (?,?,?,?)",(book_id,book_title,author,genre))
        self.con.commit()
        
        
    def fetch(self):
        self.cur.execute("SELECT * FROM list_of_books")
        rows=self.cur.fetchall()
        return rows
    
    def removeBook(self,book_id):
        self.cur.execute(f"delete from list_of_books where book_id={book_id}")
        self.con.commit()
        
    def update(self,book_id,book_title,author,genre):
        self.cur.execute("update list_of_books set book_title=?, author=?, genre=? where book_id=?",(book_title,author,genre,book_id))
        self.con.commit()
        
    def close_connection(self):
        self.con.close()   
        
class ListOfBorrowedBook:
    def __init__(self,database):
        self.con=sqlite3.connect(database)
        self.cur=self.con.cursor()
        sql= """
        CREATE TABLE IF NOT EXISTS list_of_borrowed_books(
            book_id Integer Primary Key,
            book_title text,
            author text,
            student_name text,
            date_borrowed text,
            date_due text,
            phone text

            )
        
        
        """
        self.cur.execute(sql)
        self.con.commit()
        
        
    def submit_borrowed(self,book_id,book_title,author,student_name,date_borrowed,date_due,phone):
        self.cur.execute("insert into list_of_borrowed_books values (?,?,?,?,?,?,?)",(book_id,book_title,author,student_name,date_borrowed,date_due,phone))
        self.con.commit()
        
        
    def fetch(self):
        self.cur.execute("SELECT * FROM list_of_borrowed_books")
        rows=self.cur.fetchall()
        return rows
    
    def returnBook(self,book_id):
        self.cur.execute(f"delete from list_of_borrowed_books where book_id={book_id}")
        self.con.commit()
        
    def update_borroweded(self,book_id,book_title,author,student_name,date_borrowed,date_due,phone):
        self.cur.execute("update  list_of_borrowed_books set book_title=?, author=?, student_name=?  ,date_borrowed=? ,date_due=? ,phone=? where book_id=?",(book_title,author,student_name,date_borrowed,date_due,phone,book_id))
        self.con.commit()
        

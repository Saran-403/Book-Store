#connect Sql Database
import mysql.connector
#Add book Information
def b_info():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        cursor.execute("create database if not exists abc_store")
        cursor.execute("use abc_store")
        cursor.execute("create table if not exists Books_info(book_no int(50) primary key,title varchar(100),subject_code varchar(50),author varchar(50),publisher varchar(50),price decimal(60,6),quantity int(50),location varchar(50),genre char(50),description varchar(100))")



        query=("insert into books_info values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        book_no=int(input("Enter Book Number:"))
        title =str(input("Enter The Book Title:"))
        sub_co=str(input("Enter The subject Code:"))
        author=str(input("Enter The Author Name:"))
        publi=str(input("Enter The Publisher Name:"))
        price=int(input("Enter Price:"))
        quantity=int(input("Enter Book quantity:"))
        location=str(input("Enter The Location:"))
        genre=str(input("Enter The Book Genre:"))
        descr=str(input("Enter The Book Description:"))
        data=(book_no,title,sub_co,author,publi,price,quantity,location,genre,descr)
        cursor.execute(query,data)
        db.commit()
        cursor.close()
        db.close
        print("added")
    except:
        db.close()
        
#Delete Books
def Del_book():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        bno=int(input("Enter Book No:"))
        dele=("delete from books_info where book_no=%s")
        val=(bno,)
        cursor.execute(dele,val)
        db.commit()
        print(cursor.rowcount,"record deleted")
    except:
        db.close()
#Edit Book Number
def Edit_b_no():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        bno=int(input("Enter Book NO:"))
        ch_no=int(input("Enter The New Book No to Update:"))
        c_query=("update books_info set book_no=%s where book_no=%s")
        data=(ch_no,bno)
        cursor.execute(c_query,data)
        db.commit()
        print(cursor.rowcount,"records affected")
        cursor.close()
        db.close
    except:
        db.close
#Edit Book Title        
def Edit_title():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        bno=int(input("Enter Book NO:"))
        ch_title=str(input("Enter The New Title Name to Update:"))
        c_query=("update books_info set title=%s where book_no=%s")
        data=(ch_title,bno)
        cursor.execute(c_query,data)
        db.commit()
        print(cursor.rowcount,"records affected")
        cursor.close()
        db.close
    except:
        db.close
#Edit Subject Code
def Edit_sj_code():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        bno=int(input("Enter Book NO:"))
        ch_sjc=int(input("Enter The New Subject Code to Update:"))
        c_query=("update books_info set subject_code=%s where book_no=%s")
        data=(ch_sjc,bno)
        cursor.execute(c_query,data)
        db.commit()
        print(cursor.rowcount,"records affected")
        cursor.close()
        db.close
    except:
        db.close
#Edit author
def Edit_author():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        bno=int(input("Enter Book NO:"))
        ch_author=str(input("Enter The New Author Name to Update:"))
        c_query=("update books_info set author=%s where book_no=%s")
        data=(ch_author,bno)
        cursor.execute(c_query,data)
        db.commit()
        print(cursor.rowcount,"records affected")
        cursor.close()
        db.close
    except:
        db.close
#Edit Publisher        
def Edit_publish():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        bno=int(input("Enter Book NO:"))
        ch_publish=str(input("Enter The New Publisher Name to Update:"))
        c_query=("update books_info set publisher=%s where book_no=%s")
        data=(ch_publish,bno)
        cursor.execute(c_query,data)
        db.commit()
        print(cursor.rowcount,"records affected")
        cursor.close()
        db.close
    except:
        db.close
#Edit Price
def Edit_price():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        bno=int(input("Enter Book NO:"))
        ch_price=int(input("Enter The New Price to Update:"))
        c_query=("update books_info set price=%s where book_no=%s")
        data=(ch_price,bno)
        cursor.execute(c_query,data)
        db.commit()
        print(cursor.rowcount,"records affected")
        cursor.close()
        db.close
    except:
        db.close
#Edit Quantity        
def Edit_qty():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        bno=int(input("Enter Book NO:"))
        ch_qty=int(input("Enter The New Quantity to Update:"))
        c_query=("update books_info set quantity=%s where book_no=%s")
        data=(ch_qty,bno)
        cursor.execute(c_query,data)
        db.commit()
        print(cursor.rowcount,"records affected")
        cursor.close()
        db.close
    except:
        db.close
#Edit LOcation        
def Edit_loc():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        bno=int(input("Enter Book NO:"))
        ch_loc=str(input("Enter The New Location to Update:"))
        c_query=("update books_info set location=%s where book_no=%s")
        data=(ch_loc,bno)
        cursor.execute(c_query,data)
        db.commit()
        print(cursor.rowcount,"records affected")
        cursor.close()
        db.close
    except:
        db.close
#Edit Genre        
def Edit_gen():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        bno=int(input("Enter Book NO:"))
        ch_gen=str(input("Enter The New Genre to Update:"))
        c_query=("update books_info set genre=%s where book_no=%s")
        data=(ch_gen,bno)
        cursor.execute(c_query,data)
        db.commit()
        print(cursor.rowcount,"records affected")
        cursor.close()
        db.close
    except:
        db.close
#Edit Description
def Edit_des():
    try:
         db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
         cursor=db.cursor(buffered=True)
         bno=int(input("Enter Book NO:"))
         ch_des=str(input("Enter The New Description to Update:"))
         c_query=("update books_info set description=%s where book_no=%s")
         data=(ch_des,bno)
         cursor.execute(c_query,data)
         db.commit()
         print(cursor.rowcount,"records affected")
         cursor.close()
         db.close
    except:
        db.close
        
        
    

        
    




        
    
        


        


        
        
        
    
    
        
        
        

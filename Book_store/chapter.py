#Connect Sql database
import mysql.connector
#view book chapters
def vw_chap():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)

        bno=int(input("Enter Book No:"))
        query=("select * from chapters where book_no=%s")
        val=(bno,)
        cursor.execute(query,val)
        sc=cursor.fetchone()
        if sc:
            print("BOOKNO\tCHAPTERNO\tTITLE\tSTARTING_PAGE_NO\tENDING_PAGE_NO")
            print(sc[0],"\t",sc[1],"\t\t",sc[2],"\t",sc[3],"\t\t\t",sc[4])
            db.commit()
            cursor.close()
            db.close
    except:
        db.close
        
#Adding Book chapter 
def add_chap():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        cursor.execute("create database if not exists abc_store")
        cursor.execute("use abc_store")
        cursor.execute("create table if not exists chapters(book_no int(50),chapter_no varchar(20),title varchar(50),starting_page_no int(30),ending_page_no int(30),FOREIGN KEY(book_no) REFERENCES books_info(book_no))")

        count=1
        cursor.execute("select book_no from books_info")
        sc=cursor.fetchall()
        if sc:
            print("BOOKNO")
            for sc1 in sc:
                print(sc1[0])
                count=count+1
        query=("insert into chapters values(%s,%s,%s,%s,%s)")
        bno=int(input("Enter Book Number:"))
        ch_no=int(input("Enter The Chapter Number:"))
        ch_tit=str(input("Enter The Chapter Title:"))
        st_pg=int(input("Enter the Starting Page NO:"))
        ed_pg=int(input("Enter the Ending Page NO:"))
        data=(bno,ch_no,ch_tit,st_pg,ed_pg,)
        cursor.execute(query,data)
        db.commit()
        print("Added To The Chapters")
        cursor.close()
        db.close
        
    except:
        db.close
#delete chapter
def del_chap():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        bno=int(input("Enter Book No:"))
        dele=("delete from chapters where book_no=%s")
        val=(bno,)
        cursor.execute(dele,val)
        db.commit()
        print(cursor.rowcount,"record deleted")
        cursor.close
        db.close
    except:
        db.close
#Edit Book chapter Number      
def edit_bnocha():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        bno=int(input("Enter Book NO:"))
        ch_no=int(input("Enter The New Book No to Update:"))
        c_query=("update chapters set book_no=%s where book_no=%s")
        data=(ch_no,bno)
        cursor.execute(c_query,data)
        db.commit()
        print(cursor.rowcount,"records affected")
        cursor.close()
        db.close
    except:
        db.close
#Edit Chapter Number
def edit_chano():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        chap_no=int(input("Enter Chapter NO:"))
        ch_no1=int(input("Enter The New Chapter to Update:"))
        c_query=("update chapters set chapter_no=%s where chapter_no=%s")
        data=(ch_no1,chap_no)
        cursor.execute(c_query,data)
        db.commit()
        print(cursor.rowcount,"records affected")
        cursor.close()
        db.close
    except:
        db.close
#Edit chapter Title
def edit_title():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        ch_ti=str(input("Enter chapter Title:"))
        ch_title=str(input("Enter The New Title Name to Update:"))
        c_query=("update chapters set title=%s where title=%s")
        data=(ch_title,ch_ti)
        cursor.execute(c_query,data)
        db.commit()
        print(cursor.rowcount,"records affected")
        cursor.close()
        db.close
    except:
        db.close
#Edit starting Page Number        
def edit_stpg():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        ch_st=int(input("Enter chapter Starting Page NO:"))
        ch_stp=int(input("Enter The New chapter Starting Page NO to Update:"))
        c_query=("update chapters set starting_page_no=%s where starting_page_no=%s")
        data=(ch_stp,ch_st)
        cursor.execute(c_query,data)
        db.commit()
        print(cursor.rowcount,"records affected")
        cursor.close()
        db.close
    except:
        db.close
#Edit Ending Page Number
def edit_edpg():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        ch_ed=int(input("Enter chapter Ending Page NO:"))
        ch_end=int(input("Enter The New chapter Ending Page NO to Update:"))
        c_query=("update chapters set ending_page_no=%s where ending_page_no=%s")
        data=(ch_end,ch_ed)
        cursor.execute(c_query,data)
        db.commit()
        print(cursor.rowcount,"records affected")
        cursor.close()
        db.close
    except:
        db.close


        
    



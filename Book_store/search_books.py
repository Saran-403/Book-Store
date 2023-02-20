#Connect sql database
import mysql.connector
def sc_bkno():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        book_no=int(input("Enter The Book No:"))
        query=("select * from books_info where book_no=%s")
        data=(book_no,)
        cursor.execute(query,data)
        bc=cursor.fetchone()
        if bc:
            print("BOOK_NO\tTITLE\tSUBJECT-CODE\tAUTHOR\tPUBLISHER\tPRICE\tQUANTITY\tLOCATION\tGENRE\tDESCRIPTION")
            print(bc[0],"\t",bc[1],"\t",bc[2],"\t\t",bc[3],"\t",bc[4],"\t\t",bc[5],"\t",bc[6],"\t\t",bc[7],"\t\t",bc[8],"\t",bc[9])
            cursor.close()
            db.close
    except:
        db.close
#Search by title        
def sc_bktit():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        book_title=str(input("Enter The Book Title:"))
        query=("select * from books_info where title=%s")
        data=(book_title,)
        cursor.execute(query,data)
        bc=cursor.fetchone()
        if bc:
            print("BOOK_NO\tTITLE\tSUBJECT-CODE\tAUTHOR\tPUBLISHER\tPRICE\tQUANTITY\tLOCATION\tGENRE\tDESCRIPTION")
            print(bc[0],"\t",bc[1],"\t",bc[2],"\t\t",bc[3],"\t",bc[4],"\t\t",bc[5],"\t",bc[6],"\t\t",bc[7],"\t\t",bc[8],"\t",bc[9])
            cursor.close()
            db.close
    except:
        db.close
#Search by author        
def sc_auth():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        count=0
        book_auth=str(input("Enter The Book Author:"))
        query=("select * from books_info where author=%s")
        data=(book_auth,)
        cursor.execute(query,data)
        bc=cursor.fetchall()
        if bc:
            print("BOOK_NO\tTITLE\tSUBJECT-CODE\tAUTHOR\tPUBLISHER\tPRICE\tQUANTITY\tLOCATION\tGENRE\tDESCRIPTION")
            for bc1 in bc:
                print(bc1[0],"\t",bc1[1],"\t",bc1[2],"\t\t",bc1[3],"\t",bc1[4],"\t\t",bc1[5],"\t",bc1[6],"\t\t",bc1[7],"\t\t",bc1[8],"\t",bc1[9])
                count=count+1
                cursor.close()
                db.close
    except:
        db.close
#Search by publisher
def sc_pub():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        count=0
        book_pub=str(input("Enter The Book Publisher:"))
        query=("select * from books_info where publisher=%s")
        data=(book_pub,)
        cursor.execute(query,data)
        bc=cursor.fetchall()
        if bc:
            print("BOOK_NO\tTITLE\tSUBJECT-CODE\tAUTHOR\tPUBLISHER\tPRICE\tQUANTITY\tLOCATION\tGENRE\tDESCRIPTION")
            for bc1 in bc:
                print(bc1[0],"\t",bc1[1],"\t",bc1[2],"\t\t",bc1[3],"\t",bc1[4],"\t\t",bc1[5],"\t",bc1[6],"\t\t",bc1[7],"\t\t",bc1[8],"\t",bc1[9])
                count=count+1
                cursor.close()
                db.close
    except:
        db.close
#Search by location        
def sc_loc():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)   
        count=0
        book_loc=str(input("Enter The Book Location:"))
        query=("select * from books_info where location=%s")
        data=(book_loc,)
        cursor.execute(query,data)
        bc=cursor.fetchall()
        if bc:
            print("BOOK_NO\tTITLE\tSUBJECT-CODE\tAUTHOR\tPUBLISHER\tPRICE\tQUANTITY\tLOCATION\tGENRE\tDESCRIPTION")
            for bc1 in bc:
                print(bc1[0],"\t",bc1[1],"\t",bc1[2],"\t\t",bc1[3],"\t",bc1[4],"\t\t",bc1[5],"\t",bc1[6],"\t\t",bc1[7],"\t\t",bc1[8],"\t",bc1[9])
                count=count+1
                cursor.close()
                db.close
    except:
        db.close

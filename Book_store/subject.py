#connect sql Database
import mysql.connector
#Add subject code
def add_sjcod():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        cursor.execute("create database if not exists abc_store")
        cursor.execute("use abc_store")
        cursor.execute("create table if not exists subject(subject_code varchar(50),name char(50),FOREIGN KEY(subject_code) REFERENCES books_info(subject_code))")
        db.commit()

        cursor.execute("select subject_code from books_info")
        res=cursor.fetchall()
        for subject_code in res:
            print(subject_code)
        query=("insert into subject values(%s,%s)")
        sub_co=int(input("Enter The Subject Code to Add:"))
        sub_name=str(input("Enter The Subject Name to Add :"))
        data=(sub_co,sub_name)
        cursor.execute(query,data)
        db.commit()
        cursor.close()
        db.close
        print("subject values added")
    except:
        db.close

#search By subject code
def sc_sjcod():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        count=1
        cursor.execute("select * from subject")
        sc=cursor.fetchall()
        if sc:
            print("SUBJECT-CODE\tNAME")
            for sc1 in sc:
                print(sc1[0],"\t\t",sc1[1])
                count=count+1
        sj_id=int(input("Enter The Subject Code:"))
        query=("select * from books_info where subject_code=%s")
        data=(sj_id,)
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
#delete subject code        
def sj_del():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        sj_no=str(input("Enter Subject code To delete:"))
        dele=("delete from subject where subject_code=%s")
        val=(sj_no,)
        cursor.execute(dele,val)
        db.commit()
        print(cursor.rowcount,"record deleted")
        cursor.close
        db.close
    except:
        db.close
#Edit subject code        
def sj_editcod():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        count=1
        cursor.execute("select * from subject")
        sc=cursor.fetchall()
        if sc:
            print("SUBJECT-CODE\tNAME")
            for sc1 in sc:
                print(sc1[0],"\t\t",sc1[1])
                count=count+1
        sj_id=int(input("Enter The Subject Code:"))
        ch_id1=int(input("Enter The New Subject code to Update:"))
        query=("update subject set subject_code=%s where subject_code=%s")
        data=(ch_id1,sj_id)
        cursor.execute(query,data)
        db.commit()
        cursor.close()
        db.close
        print("subject values affected")
    except:
        db.close
#Edit Subject Name        
def sj_editname():
    try:
        db=mysql.connector.connect(host="localhost",database="abc_store",user="root",password="")
        cursor=db.cursor(buffered=True)
        count=1
        cursor.execute("select * from subject")
        sc=cursor.fetchall()
        if sc:
            print("SUBJECT-CODE\tNAME")
            for sc1 in sc:
                print(sc1[0],"\t\t",sc1[1])
                count=count+1
        sj_id=int(input("Enter The Subject Code:"))
        ch_title=str(input("Enter The New Subject Name to Update:"))
        query=("update subject set name=%s where subject_code=%s")
        data=(ch_title,sj_id)
        cursor.execute(query,data)
        db.commit()
        cursor.close()
        db.close
        print("subject values affected")
    except:
        db.close


        







    

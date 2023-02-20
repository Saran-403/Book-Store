#Connect Mysql Database
import mysql.connector
db=mysql.connector.connect (host="localhost", user="root", password="")
#Heading Package
from art import tprint
tprint(" ABC STORE",font="blockhead")
tprint("WElCOME TO ABC STORE",font="random")
#Import time for login Details
import time
#Identify the user
while True:
    print("IDENTIFY YOURSELF\n1.CUSTOMER\n2.ADMINISTRATOR")
    opt=int(input("Please Enter Your Option - 1 or 2 :"))
    print()
    if opt==1:
        print("Directed you to the site as a customer")
        break
    elif opt==2:
        print("WELCOME TO THE SITE ADMIN")
        break
    else:
        print("***PLEASE SELECT THE CORRECT NUMBER***")
        
#CREATING DATABASE AND TABLE
cursor=db.cursor(buffered=True)
cursor.execute("create database if not exists abc_store")
cursor.execute("use abc_store")
cursor.execute("create table if not exists customer_login_details(user varchar(50),password varchar(50),login_date date,login_time time)")
cursor.execute("create table if not exists admin_login_details(admin varchar(50),password varchar(50),login_date date,login_time time)")


#Customer account details
while (True):
    if opt==1:
        print("1.Sign up for ABC STORE\n2.Login into ABC STORE")
        cus_opt=int(input("Please Enter Your Option- 1 or 2 :"))
        
        #Customer signup                  
        if cus_opt==1:
            user=input("ENTER YOUR USERNAME:")
            p_word=input("ENTER YOUR PASSWORD:")
            sg_date=time.strftime('%Y-%m-%d')
            sg_time=time.strftime('%H:%M:%S')
            cursor.execute("insert into customer_login_details values('"+user+"','"+p_word+"','"+sg_date+"','"+sg_time+"')")
            db.commit()
            print()
            print("YOU HAVE SUCCESSFULLY CREATED YOUR ACCOUNT")

            print()
            print("PLEASE LOGIN TO THE SITE")
            user=input("ENTER YOUR USERNAME:") 
            cursor.execute("select user from customer_login_details where user='"+user+"'")
            pot=cursor.fetchone()
            if pot is not None:
                print("VALID USERNAME!!!!!!")
                p_word=input("ENTER YOUR PASSWORD:")
                cursor.execute("select password from customer_login_details where password='"+p_word+"'")
                a=cursor.fetchone()
                if a is not None:
                    print("succesdfully loged in")
                    #signup customer Books record Menu
                    while(True):
                         print("1:View Chapter Information\n2:Direct Search\n3:Search By subject Code\n4:Exit")
                         cus_chs=int(input("Enter your choice:"))
                         if cus_chs==1:
                             import chapter
                             chapter.vw_chap()
                         elif cus_chs==2:
                             print("1:Search By Book No\n2:Search By Book Title\n3:Search By Author\n4:Search By Publisher\n5.Search By Location\n6:Exit")
                             cus_chs02=int(input("Enter your choice:"))
                             while(True):
                                 if cus_chs02==1:
                                     import search_books
                                     search_books.sc_bkno()
                                 elif cus_chs02==2:
                                     import search_books
                                     search_books.sc_bktit()
                                 elif cus_chs02==3:
                                     import search_books
                                     search_books.sc_auth()
                                 elif cus_chs02==4:
                                     import search_books
                                     search_books.sc_pub()
                                 elif cus_chs02==5:
                                     import search_books
                                     search_books.sc_loc()
                                 elif cus_chs02==6:
                                     print("welcome")
                                     break
                                 else:
                                     print("---Please Select Correct Option---")
                         elif cus_chs==3:
                             import subject
                             subject.sc_sjcod()
                         elif cus_chs==4:
                             print("welcome")
                             break
                         else:
                             print("---Please Select Correct Option---")
                    break
                else:
                      print("""++++++++++++++++++++++++INCORRECT PASSWORD++++++++++++++++++++++++""")
            else:
                print("""++++++++++++++++++++++INVALID USERNAME++++++++++++++++++++++""")
        
  
        #Customer Login 
        elif cus_opt==2:
              user=input("ENTER YOUR USERNAME:")
              sg_date=time.strftime('%Y-%m-%d')
              sg_time=time.strftime('%H:%M:%S') 
              cursor.execute("select user from customer_login_details where user='"+user+"'")   
              top=cursor.fetchone()
              if top is not None:
                  print("VALID USERNAME!!!!!!")
                  p_word=input("ENTER YOUR PASSWORD:")
                  cursor.execute("select password from customer_login_details where password='"+p_word+"'" )
                  q=cursor.fetchall()
                  cursor.execute("insert into customer_login_details values('"+user+"','"+p_word+"','"+sg_date+"','"+sg_time+"')")
                  db.commit()
                  if q is not None:
                      print("succesdfully loged in")
                      #login customer Books Record Menu
                      while(True):
                          print("1:View Chapter Information\n2:Direct Search\n3:Search By subject Code\n4:Exit")
                          cus_chs=int(input("Enter your choice:"))
                          if cus_chs==1:
                              import chapter
                              chapter.vw_chap()
                          elif cus_chs==2:
                              print("1:Search By Book No\n2:Search By Book Title\n3:Search By Author\n4:Search By Publisher\n5.Search By Location\n6:Exit")
                              cus_chs02=int(input("Enter your choice:"))
                              while(True):
                                  if cus_chs02==1:
                                      import search_books
                                      search_books.sc_bkno()
                                  elif cus_chs02==2:
                                      import search_books
                                      search_books.sc_bktit()
                                  elif cus_chs02==3:
                                      import search_books
                                      search_books.sc_auth()
                                  elif cus_chs02==4:
                                      import search_books
                                      search_books.sc_pub()
                                  elif cus_chs02==5:
                                      import search_books
                                      search_books.sc_loc()
                                  elif cus_chs02==6:
                                      print("welcome")
                                      break
                                  else:
                                      print("---Please Select Correct Option---")
                          elif cus_chs==3:
                              import subject
                              subject.sc_sjcod()
                          elif cus_chs==4:
                              print("welcome")
                              break
                          else:
                              print("---Please Select Correct Option---")
                              
                              
                              
                              
                          
                      break
                  else:
                      print("""++++++++++++++++++++++++INCORRECT PASSWORD++++++++++++++++++++++++""")
              else:
                  print("""++++++++++++++++++++++INVALID USERNAME++++++++++++++++++++++""")
      
     
       
    #Adinistrato Sign up
    elif opt==2:
          print("1.Sign up for ABC STORE\n2.Login into ABC STORE")
          adm_opt=int(input("Please Enter Your Option- 1 or 2 :"))
          
          if adm_opt==1:
              admin=input("ENTER YOUR USERNAME:")
              p_word=input("ENTER YOUR PASSWORD:")
              sg_date=time.strftime('%Y-%m-%d')
              sg_time=time.strftime('%H:%M:%S')
              cursor.execute("insert into admin_login_details values('"+admin+"','"+p_word+"','"+sg_date+"','"+sg_time+"')")
              db.commit()
              print()
              print("YOU HAVE SUCCESSFULLY CREATED YOUR ACCOUNT")

              print()
              print("PLEASE LOGIN TO THE SITE")
              admin=input("ENTER YOUR USERNAME:") 
              cursor.execute("select admin from admin_login_details where admin='"+admin+"'")
              pot=cursor.fetchone()
              if pot is not None:
                  print("VALID USERNAME!!!!!!")
                  p_word=input("ENTER YOUR PASSWORD:")
                  cursor.execute("select password from admin_login_details where password='"+p_word+"'")
                  a=cursor.fetchone()
                  if a is not None:
                      print("succesdfully loged in")
                      #sign up administrator Book Menu
                      while(True):
                          print("1:Add Books\n2:Delete Books\n3:Edit books\n4:Direct search\n5:Search By subject code\n6:View Book chapters\n7:Exit ")
                          chs=int(input("Enter your choice:"))
                          while(True):
                              if chs==1:
                                  import book
                                  book.b_info()
                              elif chs==2:
                                  import bk
                                  book.Del_book()
                              elif chs==3:
                                  print("1:Edit Book NO\n2:Edit Title\n3:Edit Subject Code\n4:Edit Author\n5:Edit Publisher\n6:Edit Price\n7:Edit Quantity\n8:Edit Location\n9:Edit Genre\n10:Edit description\n11.Exit")
                                  chs1=int(input("Enter your choice:"))
                                  while(True):
                                      if chs1==1:
                                          import book
                                          book.Edit_b_no()
                                      elif chs1==2:
                                          import book
                                          book.Edit_title()
                                      elif chs1==3:
                                          import book
                                          book.Edit_sj_code()
                                      elif chs1==4:
                                          import book
                                          book.Edit_author()
                                      elif chs1==5:
                                          import book
                                          book.Edit_publish()
                                      elif chs1==6:
                                          import book
                                          book.Edit_price()
                                      elif chs1==7:
                                          import book
                                          book.Edit_qty()
                                      elif chs1==8:
                                          import book
                                          book.Edit_loc()
                                      elif chs1==9:
                                          import book
                                          book.Edit_gen()
                                      elif chs1==10:
                                          import book
                                          book.Edit_des()
                                      elif chs1==11:
                                          print("welcome")
                                          break
                                      else:
                                          print("---Please Select Correct Option---")                                  
                              elif chs==4:
                                  print("1:Search By Book No\n2:Search By Book Title\n3:Search By Author\n4:Search By Publisher\n5.Search By Location\n6:Exit")
                                  chs2=int(input("Enter your choice:"))
                                  while(True):
                                      if chs2==1:
                                          import search_books
                                          search_books.sc_bkno()
                                      elif chs2==2:
                                          import search_books
                                          search_books.sc_bktit()
                                      elif chs2==3:
                                          import search_books
                                          search_books.sc_auth()
                                      elif chs2==4:
                                          import search_books
                                          search_books.sc_pub()
                                      elif chs2==5:
                                          import search_books
                                          search_books.sc_loc()
                                      elif chs2==6:
                                          print("welcome")
                                          break
                                      else:
                                          print("---Please Select Correct Option---")
                              elif chs==5:
                                  print("1:Search By Subject Code\n2:Add subject Code\n3:Delete Subject Code\n4:Edit Subject Code\n5:Exit")
                                  chs3=int(input("Enter your choice:"))
                                  while(True):
                                      if chs3==1:
                                          import subject
                                          subject.sc_sjcod()
                                      elif chs3==2:
                                          import subject
                                          subject.add_sjcod()                                  
                                      elif chs3==3:
                                          import subject
                                          subject.sj_del()
                                      elif chs3==4:
                                          print("1:Edit Subject Code No\n2:Edit Subject Code Name\n3:Exit")
                                          chs03=int(input("Enter your choice:"))
                                          while(True):
                                              if chs03==1:
                                                  import subject
                                                  subject.sj_editcod()
                                              elif chs03==2:
                                                  import subject
                                                  subject.sj_editname()                                  
                                              elif chs03==3:
                                                  print("welcome")
                                                  break
                                              else:
                                                  print("---Please Select Correct Option---")
                                      elif chs3==5:
                                          print("welcome")
                                          break
                                      else:
                                          print("---Please Select Correct Option---")                                                           
                              elif chs==6:
                                  print("1:View Chapter Information\n2:Add Chapter\3:Delete Chapter\4.Edit Chapter\n5:Exit")
                                  chs06=int(input("Enter your choice:"))
                                  while(True):
                                      if chs06==1:
                                          import chapter
                                          chapter.vw_chap()
                                      elif chs06==2:
                                          import chapter
                                          chapter.add_chap()
                                      elif chs06==3:
                                          import chapter
                                          chapter.del_chap()
                                      elif chs06==4:
                                          print("1:Edit Chapter Book NO\n2:Edit Chapter NO\n3:Edit Chapter Title\4:Edit Chapter Starting Page\5.Edit Chapter Ending Page\n6:Exit")
                                          chs006=int(input("Enter your choice:"))
                                          while(True):
                                              if chs006==1:
                                                  import chapter
                                                  chapter.edit_bnocha()
                                              elif chs006==2:
                                                  import chapter
                                                  chapter.edit_chano()
                                              elif chs006==3:
                                                  import chapter
                                                  chapter.edit_title()
                                              elif chs006==4:
                                                  import chapter
                                                  chapter.edit_stpg()
                                              elif chs006==5:
                                                  import chapter
                                                  chapter.edit_edpg()
                                              elif chs006==6:
                                                  print("welcome")
                                                  break
                                              else:
                                                  print("---Please Select Correct Option---")
                                      elif chs06==5:
                                          print("welcome")
                                          break
                                      else:
                                          print("---Please Select Correct Option---")
                              elif chs==7:
                                  print("welcome")
                                  break
                              else:
                                  print("---Please Select Correct Option---")                                       
                  else:
                      print("""++++++++++++++++++++++++INCORRECT PASSWORD++++++++++++++++++++++++""")
              else:
                  print("""++++++++++++++++++++++INVALID USERNAME++++++++++++++++++++++""")
        
  
          #login Administrator books record Menu         
          elif adm_opt==2:
                admin=input("ENTER YOUR USERNAME:")
                sg_date=time.strftime('%Y-%m-%d')
                sg_time=time.strftime('%H:%M:%S') 
                cursor.execute("select admin from admin_login_details where admin='"+admin+"'")   
                top=cursor.fetchone()
                if top is not None:
                    print("VALID USERNAME!!!!!!")
                    p_word=input("ENTER YOUR PASSWORD:")
                    cursor.execute("select password from admin_login_details where password='"+p_word+"'" )
                    q=cursor.fetchall()
                    cursor.execute("insert into admin_login_details values('"+admin+"','"+p_word+"','"+sg_date+"','"+sg_time+"')")
                    db.commit()
                    if q is not None:
                        print("succesdfully loged in")
                        while(True):
                          print("1:Add Books\n2:Delete Books\n3:Edit books\n4:Direct search\n5:Search By subject code\n6:View Book chapters\n7:Exit ")
                          chs=int(input("Enter your choice:"))
                          while(True):
                              if chs==1:
                                  import book
                                  book.b_info()
                              elif chs==2:
                                  import book
                                  book.Del_book()
                              elif chs==3:
                                  print("1:Edit Book NO\n2:Edit Title\n3:Edit Subject Code\n4:Edit Author\n5:Edit Publisher\n6:Edit Price\n7:Edit Quantity\n8:Edit Location\n9:Edit Genre\n10:Edit description\n11.Exit")
                                  chs1=int(input("Enter your choice:"))
                                  while(True):
                                      if chs1==1:
                                          import book
                                          book.Edit_b_no()
                                      elif chs1==2:
                                          import book
                                          book.Edit_title()
                                      elif chs1==3:
                                          import book
                                          book.Edit_sj_code()
                                      elif chs1==4:
                                          import book
                                          book.Edit_author()
                                      elif chs1==5:
                                          import book
                                          book.Edit_publish()
                                      elif chs1==6:
                                          import book
                                          book.Edit_price()
                                      elif chs1==7:
                                          import book
                                          book.Edit_qty()
                                      elif chs1==8:
                                          import book
                                          book.Edit_loc()
                                      elif chs1==9:
                                          import book
                                          book.Edit_gen()
                                      elif chs1==10:
                                          import book
                                          book.Edit_des()
                                      elif chs1==11:
                                          print("welcome")
                                          break
                                      else:
                                          print("---Please Select Correct Option---")                                  
                              elif chs==4:
                                  print("1:Search By Book No\n2:Search By Book Title\n3:Search By Author\n4:Search By Publisher\n5.Search By Location\n6:Exit")
                                  chs2=int(input("Enter your choice:"))
                                  while(True):
                                      if chs2==1:
                                          import search_books
                                          search_books.sc_bkno()
                                      elif chs2==2:
                                          import search_books
                                          search_books.sc_bktit()
                                      elif chs2==3:
                                          import search_books
                                          search_books.sc_auth()
                                      elif chs2==4:
                                          import search_books
                                          search_books.sc_pub()
                                      elif chs2==5:
                                          import search_books
                                          search_books.sc_loc()
                                      elif chs2==6:
                                          print("welcome")
                                          break
                                      else:
                                          print("---Please Select Correct Option---")
                              elif chs==5:
                                  print("1:Search By Subject Code\n2:Add subject Code\n3:Delete Subject Code\n4:Edit Subject Code\n5:Exit")
                                  chs3=int(input("Enter your choice:"))
                                  while(True):
                                      if chs3==1:
                                          import subject
                                          subject.sc_sjcod()
                                      elif chs3==2:
                                          import subject
                                          subject.add_sjcod()                                  
                                      elif chs3==3:
                                          import subject
                                          subject.sj_del()
                                      elif chs3==4:
                                          print("1:Edit Subject Code No\n2:Edit Subject Code Name\n3:Exit")
                                          chs03=int(input("Enter your choice:"))
                                          while(True):
                                              if chs03==1:
                                                  import subject
                                                  subject.sj_editcod()
                                              elif chs03==2:
                                                  import subject
                                                  subject.sj_editname()                                  
                                              elif chs03==3:
                                                  print("welcome")
                                                  break
                                              else:
                                                  print("---Please Select Correct Option---")
                                      elif chs3==5:
                                          print("welcome")
                                          break
                                      else:
                                          print("---Please Select Correct Option---")                                                           
                              elif chs==6:
                                  print("1:View Chapter Information\n2:Add Chapter\n3:Delete Chapter\n4.Edit Chapter\n5:Exit")
                                  chs06=int(input("Enter your choice:"))
                                  while(True):
                                      if chs06==1:
                                          import chapter
                                          chapter.vw_chap()
                                      elif chs06==2:
                                          import chapter
                                          chapter.add_chap()
                                      elif chs06==3:
                                          import chapter
                                          chapter.del_chap()
                                      elif chs06==4:
                                          print("1:Edit Chapter Book NO\n2:Edit Chapter NO\n3:Edit Chapter Title\4:Edit Chapter Starting Page\5.Edit Chapter Ending Page\n6:Exit")
                                          chs006=int(input("Enter your choice:"))
                                          while(True):
                                              if chs006==1:
                                                  import chapter
                                                  chapter.edit_bnocha()
                                              elif chs006==2:
                                                  import chapter
                                                  chapter.edit_chano()
                                              elif chs006==3:
                                                  import chapter
                                                  chapter.edit_title()
                                              elif chs006==4:
                                                  import chapter
                                                  chapter.edit_stpg()
                                              elif chs006==5:
                                                  import chapter
                                                  chapter.edit_edpg()
                                              elif chs006==6:
                                                  print("welcome")
                                                  break
                                              else:
                                                  print("---Please Select Correct Option---")
                                      elif chs06==5:
                                          print("welcome")
                                          break
                                      else:
                                          print("---Please Select Correct Option---")
                              elif chs==7:
                                  print("welcome")
                                  break
                              else:
                                  print("---Please Select Correct Option---")               
                        break
                    else:
                        print("""++++++++++++++++++++++++INCORRECT PASSWORD++++++++++++++++++++++++""")
                else:
                    print("""++++++++++++++++++++++INVALID USERNAME++++++++++++++++++++++""")
         
    else:
        break
     

        
  
                        

        


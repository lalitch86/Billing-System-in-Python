from tkinter import *
from tkinter import messagebox
import os,re,math,random
from datetime import date
import time
import mysql.connector
from fpdf import FPDF

root=Tk()

class Mainwindow():
  def __init__(self,root):
    self.root=root
    """==================================Login Window ==================="""
    global bg_color
    bg_color="#074463"

    self.root.title("USER LOGIN")
    self.root.geometry("1440x890+0+0")
    
    
    title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new romon",30,"bold"),pady=2)
    title.pack(fill=X)
    
    self.blabel=Label(self.root)
    self.blabel.pack()
   
    self.frame=Frame(self.root,)
    self.frame.place(x=390,y=170,width=400,height=450)
    
    self.label=Label(self.frame,text="USERID",font=("Andalus",15,'bold'),fg='gray',bg='#F0F8FF')
    self.label.place(x=80,y=50)

    self.Uentry=Entry(self.frame,font=('times new roman',15))
    self.Uentry.place(x=80,y=100,width=250)

    self.label = Label(self.frame, text="PASSWORD", font=("Andalus", 15,'bold'),bg='#F0F8FF',fg='gray')
    self.label.place(x=80, y=150)

    self.pentry = Entry(self.frame,show='*', font=('times new roman', 15))
    self.pentry.place(x=80, y=200,width=250)

    self.button=Button(self.frame,text="Login",bg='#F0F8FF',command=lambda:self.user_login(),activebackground='#00B0F0',activeforeground="white",fg='gray',font=('Arial Rounded MT Bold',15,'bold'))
    self.button.place(x=80,y=250,height=35,width=250)

  def user_login(self):
    if self.Uentry.get == '' and self.pentry.get() == '':
      messagebox.showwarning("Warning", 'Please Enter User ID and Passward')
    elif self.Uentry.get() == '':
      messagebox.showwarning("Warning", 'Please Enter User ID')
    elif self.pentry.get() == '':
      messagebox.showwarning("Warning", 'Please Enter Password')
    elif self.Uentry.get() !="1234":
      messagebox.showwarning("Warning","Plsese Enter Correct User Id")
    elif self.pentry.get() != "1234":
      messagebox.showwarning("Warning","Plsese Enter Correct Passward")
    else:
      self.Uentry.get == "1234" and self.pentry.get == "1234" 
      messagebox.showinfo("SUCCESS",'you logged in Successfully')

      bg_color="#074463"

      "============================ Customer Details ========================"
      cname=StringVar()
      cphone=StringVar()
      global cemail
      cemail=StringVar()

      
      F1=LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,font=("times new romon",15,"bold"),fg="gold",bg=bg_color)
      F1.place(x=0,y=80,relwidth=1)
    
      cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new romon",15,"bold"))
      cname_lbl.grid(row=0,column=0,padx=20,pady=5)      
      cname_txt=Entry(F1,textvariable=cname,width=19,font="arial 15",bd=7,relief=SUNKEN)
      cname_txt.grid(row=0,column=1,padx=2,pady=10)
      

      cphone_lbl=Label(F1,text="Phone NO",bg=bg_color,fg="white",font=("times new romon",15,"bold"))
      cphone_lbl.grid(row=0,column=2,padx=20,pady=5)      
      cphone_txt=Entry(F1,textvariable=cphone,width=19,font="arial 15",bd=7,relief=SUNKEN)
      cphone_txt.grid(row=0,column=3,padx=2,pady=10)
      

      cemail_lbl=Label(F1,text="Email Id",bg=bg_color,fg="white",font=("times new romon",15,"bold"))
      cemail_lbl.grid(row=0,column=4,padx=20,pady=5)
      cemail_txt=Entry(F1,textvariable=cemail,width=19,font="arial 15",bd=7,relief=SUNKEN)
      cemail_txt.grid(row=0,column=5,padx=2,pady=10)

      add_cd=Button(F1,text="Add",command=lambda:add_cd(),width=10,bd=7,font="arial 12 bold")
      add_cd.grid(row=0,column=6,padx=10,pady=5)

      clear_cd=Button(F1,text="Clear",command=lambda:clear_cd(),width=10,bd=7,font="arial 12 bold")
      clear_cd.grid(row=0,column=7,padx=10,pady=5)
      

      "=====================================  billing Frame  =====" 
      F2=Frame(root,bd=10,relief=GROOVE)
      F2.place(x=770,y=180,width=665,height=520)
      
      bill_title=Label(F2,text="Bill",font="arial 15 bold",bd=7,relief=GROOVE)
      bill_title.pack(fill=X)

           
      scrol_y=Scrollbar(F2,orient=VERTICAL)
      txtarea=Text(F2,yscrollcommand=scrol_y.set)
      scrol_y.pack(side=RIGHT,fill=Y)
      scrol_y.config(command=txtarea.yview)
      txtarea.pack(fill=BOTH,expand=1)

      """====================================  Total Bill Box ====================="""
      F5=LabelFrame(root,text="Bill Amount",bd=10,relief=GROOVE,font=("times new romon",15,"bold"),fg="gold",bg=bg_color)
      F5.place(x=770,y=705,width=665,height=120)

      
      B1_lbl=Label(F5,text="   Bill Amount    ",bg=bg_color,fg="white",font=("times new roman",25,"bold"))
      B1_lbl.grid(row=0,column=0,padx=20,pady=15)
      
      F6=Frame(root,bd=10,relief=GROOVE)
      F6.place(x=1020,y=735,width=350,height=70)
      
      T1=Text(F6,height=65,width=345,font=("times new romon",25,"bold"))
      T1.pack()

      

      "====================================== product Details ====="
      global Ecode
      global Equantity
      Ecode=IntVar()
      Equantity=IntVar()

      F3=LabelFrame(root,text="Product Details",bd=10,relief=GROOVE,font=("times new romon",15,"bold"),fg="gold",bg=bg_color)
      F3.place(x=5,y=180,width=755,height=360)

      code_lbl=Label(F3,text="Product Code:",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
      code_lbl.grid(row=0,column=0,padx=20,pady=10)
      code_txt=Entry(F3,width=20,textvariable=Ecode,font="arial 15",bd=7,relief=SUNKEN)
      code_txt.grid(row=0,column=1,pady=20,padx=10)

      quantity_lbl=Label(F3,text="Product Quantity",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
      quantity_lbl.grid(row=1,column=0,padx=20,pady=10)
      quantity_txt=Entry(F3,width=20,textvariable=Equantity,font="arial 15",bd=7,relief=SUNKEN)
      quantity_txt.grid(row=1,column=1,pady=20,padx=10)

      add_entry=Button(F3,text="Add to Cart",command=lambda:add_to_cart(),width=10,bd=7,font="arial 12 bold")
      add_entry.grid(row=0,column=2,padx=15,pady=5)

      remove_entry=Button(F3,text="remove Entry",command=lambda:remove_entry(),width=10,bd=7,font="arial 12 bold")
      remove_entry.grid(row=1,column=2,padx=15,pady=5)

      total_btn=Button(F3,text="Total",command=lambda:total_bill(),height=2,width=12,bd=7,font="arial 12 bold")
      total_btn.grid(row=2,column=0,padx=10,pady=10)
      
      generate_btn=Button(F3,text="Generate Bill",command=lambda:generate_bill(),bg="cadetblue",width=12,height=2,bd=8,font="arial 12 bold")
      generate_btn.grid(row=2,column=1,padx=10,pady=10)

      clear_entry=Button(F3,text="Clear",command=lambda:c_all(),width=12,height=2,bd=7,font="arial 12 bold")
      clear_entry.grid(row=2,column=2,padx=10,pady=10)
      
      "============================================product Details function code ======"

      
    lst=[]  
    def add_to_cart():
      a=int(Ecode.get())
      c=int(Equantity.get())
      con = mysql.connector.connect(user="root",password="mysql",host="localhost",database="test_sd")
      cursor=con.cursor()
      try:
        cursor.execute("select pname from stock where pid=%s"%a)
        name=cursor.fetchone()
        cursor.execute("select price from stock where pid=%s"%a)
        price=cursor.fetchall()
        for row in price:
          nprice=row[0]
        tprice=nprice*c
        totprice=nprice*c
        txtarea.insert(END,"\n ")
        txtarea.insert(END,"\n  ")
        txtarea.insert(END,a)
        txtarea.insert(END," \t\t ")
        txtarea.insert(END,name)
        txtarea.insert(END," \t \t \t ")
        txtarea.insert(END,c)
        txtarea.insert(END," \t \t")
        txtarea.insert(END,tprice)
        lst.append(totprice)
        x=0
        for i in lst:
          x=x+i
        T1.delete('1.0',END)        
        T1.insert(END,x)
        con.close()
      except:
        messagebox.showwarning("Warning","Check PID")
      
      
    def remove_entry():
      try:
        a=str(Ecode.get())
        c=int(Equantity.get())
        con = mysql.connector.connect(user="root",password="mysql",host="localhost",database="test_sd")
        cursor=con.cursor()

        cursor.execute("select pname from stock where pid=%s"%a)
        name=cursor.fetchone()
        cursor.execute("select price from stock where pid=%s"%a)
        price=cursor.fetchall()
        for row in price:
          nprice=row[0]
        tprice=nprice*c  
        con.close()

        lst.remove(tprice)
        if a:
          idx='1.0'
          while 1:
            idx=txtarea.search(a,idx,nocase=1,stopindex=END)
            if not idx:
              break
            lastidx = '% s+% dc' % (idx,len(a)+26)
            txtarea.delete(idx,lastidx)
      except:
        messagebox.showwarning("check","Entry Not Found")
          
      x=0
      for i in lst:
        x=x+i
      T1.delete('1.0',END)  
      T1.insert(END,x)
                    
    def total_bill():
      txtarea.insert(END,"\n=====================================================================")
      txtarea.insert(END,"\n     \t\t   TOTAL (*gst included)   \t\t\t      \t\t  ") 
      x=0
      for i in lst:
        x=x+i
      txtarea.insert(END,x)  
      txtarea.insert(END,"\t\t")
      txtarea.insert(END,"\n Thank You For Purchese...")
      txtarea.insert(END,"\n=====================================================================")
      txtarea.insert(END,"\n Contact No: 7894561230 \t Email:suprim@gmail.com")
      
    bn=random.randint(1000,10000)
    
    def add_cd():
      n=cname.get()
      p=cphone.get()
      m=cemail.get() 
      flag=False
      try :
        int(p)
      except ValueError:
        return flag==True
        
      def email_check(str):
        emailpattern='[a-zA-Z0-9(\.|\_]+@(\w+\.)+(com|org|net|edu|co.in)'

        if re.match(emailpattern,m):
          return True
        else:
          return False          
        
      if len(n) == 0 and len(p) != 10 and len(m) ==0:
        messagebox.showwarning("Warning","Plese Enter Customer Details ")
          
      elif len(n) == 0 :
        messagebox.showwarning("Warning","Plese Enter Name ")
          
      elif len(p) !=10 and flag == True :
        messagebox.showwarning("Warning","Plese Enter Valid 10 Digit Number")

      elif len(m)==0:
        messagebox.showwarning("Warning","Plses enter Email Id")
          
      elif email_check(m)== False :
        messagebox.showwarning("Warning","Plses Enter Valid Email Id")
          
      else:
        txtarea.delete('1.0',END)
        txtarea.insert(END,"=====================================================================")
        txtarea.insert(END,"\n\t\t\tShrinath  Super Market")  
        txtarea.insert(END,"\n=====================================================================")
        txtarea.insert(END,f"\nCustomer Name :"+n)      
        txtarea.insert(END,f"\t \t Phone Number : "+p)
        txtarea.insert(END,f"\nCustomer Email :"+m)
        
        txtarea.insert(END,"\t\t\t Bill Number :BN"+str(bn))
        txtarea.insert(END,"\nDate :"+str(date.today()))
        ttime=time.strftime("%H - %m - %S")
        txtarea.insert(END,"\t \t Time :"+str(ttime))
        txtarea.insert(END,"\n=====================================================================")
        txtarea.insert(END,"\n  PID \t\t PName \t\t\t Pquantity \t\t Price \t\t")
        txtarea.insert(END,"\n=====================================================================")
        messagebox.showinfo("Done","Customer Details Added SuccesFully")
        cname.set(" ")
        cphone.set(" ")
        cemail.set(" ")
          
    def clear_cd():
      cname.set(" ")
      cphone.set(" ")
      cemail.set(" ")
    def c_all():
      cname.set(" ")
      cphone.set(" ")
      cemail.set(" ")
      txtarea.delete('1.0',END)
      T1.delete('1.0',END)
      Ecode.set("")
      Equantity.set("")
      for i in lst:
        lst.remove(i)

    def generate_bill():
      op=messagebox.askyesno("Save Bill","Do You Want to Save the Bill")
      if op>0:
        file =txtarea.get("1.0",END)
        f1=open("bills/"+str(bn)+".txt","w+")
        f1.write(file)        
        f1.close()
        f1=open("bills/"+str(bn)+".txt","r")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 15)
        for x in f1:
          pdf.cell(200, 10, txt = x, ln = 1, align = 'L')
        pdf.output(str(bn)+".pdf") 
        f1.close()
      else:
        return
      messagebox.showinfo("Done","Bill Saved in Folder")
      
      
      """=================stock Details code======================"""
    def open_view_bills():
      top=Toplevel()
      top=top
      top.title("View Bills")
      top.geometry("600x400")

      global gbillno
      gbillno=IntVar()
      
      F1=Frame(top,bd=10,relief=GROOVE)
      F1.place(x=0,y=80,width=600)

      
      code_lbl=Label(F1,text="Enter Bill No:",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
      code_lbl.grid(row=0,column=0,padx=20,pady=5)
      code_txt=Entry(F1,width=20,textvariable=gbillno,font="arial 15",bd=7,relief=SUNKEN)
      code_txt.grid(row=0,column=1,pady=5,padx=10)

      gbill=Button(F1,text="View Bill",command=lambda:getbill(),bg="cadetblue",fg="white",pady=15,width=11,font="arial 10 bold")
      gbill.grid(row=1,column=2,padx=5,pady=5)  

    def getbill():
      txtarea.delete('1.0',END)
      ob=gbillno.get()
      f1=open("bills/"+str(ob)+".txt","r")
      for x in f1 :
        txtarea.insert(END,x)
      f1.close()
      

    def open_view_stock():
      top=Toplevel()
      top=top
      top.title("Stock")
      top.geometry("740x900")
      
      con = mysql.connector.connect(user="root",password="mysql",host="localhost",database="test_sd")
      cursor=con.cursor()
      
      F2=Frame(top,bd=10,relief=GROOVE)
      F2.place(x=0,y=0,width=725,height=600)
      bill_title=Label(F2,text="All Stocks ",font="arial 15 bold",bd=7,relief=GROOVE)
      bill_title.pack(fill=X)
           
      scrol_y=Scrollbar(F2,orient=VERTICAL)
      txtarea=Text(F2,yscrollcommand=scrol_y.set,font=("Andalus", 15,'bold'),bg='#F0F8FF',fg='gray')
      scrol_y.pack(side=RIGHT,fill=BOTH)
      scrol_y.config(command=txtarea.yview)
      txtarea.pack(fill=Y)
      

      cursor.execute("select * from stock")
      result=cursor.fetchall()
      txtarea.delete('1.0',END)      
      txtarea.insert(END,("\n{:5s}\t\t{:25s}\t\t\t{:5s}\n".format("  PID","pname","price")))
      txtarea.insert(END,"-"*97,)
      for row in result:
        pid=row[0]
        pname=row[1]
        price=row[2]
        txtarea.insert(END,("\n{:5d}\t\t{:25s}\t\t\t{:5d}\n".format(pid,pname,price)))
      txtarea.insert(END,"-"*97,)
      con.close()
      txtarea.configure(state='disabled')


    def open_new_stock():
        top=Toplevel()
        top=top
        top.title("New Stock Entry")
        top.geometry("600x340")

        global ncode
        global nname
        global nprice
        
        ncode=IntVar()
        nname=StringVar()
        nprice=IntVar()      

        

        F1=LabelFrame(top,text="New Stock Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=50,relwidth=1)
        
        code_lbl=Label(F1,text="Product Code:",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        code_lbl.grid(row=0,column=0,padx=20,pady=5)
        code_txt=Entry(F1,width=20,textvariable=ncode,font="arial 15",bd=7,relief=SUNKEN)
        code_txt.grid(row=0,column=1,pady=5,padx=10)

        name_lbl=Label(F1,text="Product Name:",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        name_lbl.grid(row=3,column=0,padx=20,pady=5)
        name_txt=Entry(F1,width=20,textvariable=nname,font="arial 15",bd=7,relief=SUNKEN)
        name_txt.grid(row=3,column=1,pady=5,padx=10)

        price_lbl=Label(F1,text="Product Price",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        price_lbl.grid(row=5,column=0,padx=20,pady=5)
        price_txt=Entry(F1,width=20,textvariable=nprice,font="arial 15",bd=7,relief=SUNKEN)
        price_txt.grid(row=5,column=1,pady=5,padx=10)

        insert=Button(F1,text="Insert",command=lambda:insert_stock(),bg="cadetblue",fg="white",pady=15,width=11,font="arial 10 bold")
        insert.grid(row=12,column=0,padx=5,pady=5)      

    def insert_stock():
        a = int(ncode.get())
        b = nname.get()
        c = int(nprice.get())
        
        con = mysql.connector.connect(user="root",password="mysql",host="localhost",database="test_sd")
        cursor=con.cursor()

        sqlf=("insert into stock(pid,pname,price) values(%s,%s,%s)")
        data = (a,b,c)
        try:
          cursor.execute(sqlf,data)
          con.commit()
          messagebox.showinfo("done","data added successfully")        
        except:
          con.rollback()
          messagebox.showwarning("waarning","Item ID Already Exits")
        con.close()
        
    def how_to_use():

          top=Toplevel()
          top=top
          top.title("Help")
          top.geometry("600x600")
          
          F2=Frame(top,bd=10,relief=GROOVE)
          F2.place(x=0,y=0,width=600,height=600)
          bill_title=Label(F2,text="All Stocks ",font="arial 15 bold",bd=7,relief=GROOVE)
          bill_title.pack(fill=X)
               
          scrol_y=Scrollbar(F2,orient=VERTICAL)
          txtarea=Text(F2,yscrollcommand=scrol_y.set,font=("Andalus", 15,'bold'),bg='#F0F8FF',fg='gray')
          scrol_y.pack(side=RIGHT,fill=BOTH)
          scrol_y.config(command=txtarea.yview)
          txtarea.pack(fill=BOTH)
          txtarea.insert(END,"How to Use This Billing Software :\n")
          txtarea.insert(END,"1.First Login To your Software\n")
          txtarea.insert(END,"( if You dont have login details than kindly go to developer)\n")
          txtarea.insert(END,"2.After succesfull login first Enter customer details first\n(make sure that are valid also)\n")
          txtarea.insert(END,"3.then add to code that is present on product and\n its quantity and click on add to cart button.\n")
          txtarea.insert(END,"4.if you want to remove any product then\n you can use remove from cart button.\n")
          txtarea.insert(END,"5.after adding all the products then click on total\n button and then generate bill button.\n(after taking payment)\n") 
          txtarea.insert(END,"6.then bill is generated go to respective folder\n and print the bill.\n")
          txtarea.insert(END,"7.Kindly Do Not Enter Same Product With Diffrent Nos of ")          
          txtarea.insert(END,"\n Quantity Beacause While Using Remove Entry Buttton")          
          txtarea.insert(END,"\n It Removes All The Entries Hence You Have To Use")
          txtarea.insert(END,"\n Remove Entry Button Number Of Time You Added Entry \n of Product.")

    def open_update_price():
        top=Toplevel()
        top.title("Update Price")
        top.geometry("600x300")
        global ncode2
        global nprice2
        

        ncode2=IntVar()
        nprice2=IntVar()
                    
        F1=LabelFrame(top,text="Update Price",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=50,relwidth=1)

        code_lbl=Label(F1,text="Product Code:",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        code_lbl.grid(row=0,column=0,padx=20,pady=5)
        code_txt=Entry(F1,width=20,textvariable=ncode2,font="arial 15",bd=7,relief=SUNKEN)
        code_txt.grid(row=0,column=1,pady=5,padx=10)

        price_lbl=Label(F1,text="Product Price:",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        price_lbl.grid(row=3,column=0,padx=20,pady=5)
        price_txt=Entry(F1,width=20,textvariable=nprice2,font="arial 15",bd=7,relief=SUNKEN)
        price_txt.grid(row=3,column=1,pady=5,padx=10)

        update=Button(F1,text="Update Price",command=lambda:update_price(),bg="cadetblue",fg="white",pady=15,width=11,font="arial 10 bold")
        update.grid(row=5,column=0,padx=5,pady=5)
        
    def update_price():
        a = int(ncode2.get())
        d = int(nprice2.get())
        
        con = mysql.connector.connect(user="root",password="mysql",host="localhost",database="test_sd")
        cursor=con.cursor()

        sqlf=("update stock SET price=%s where pid=%s")
        data=(d,a)
        try:
          cursor.execute(sqlf,data)
          con.commit()
          messagebox.showinfo("Done","Price Updated Successfully")
        except:
          return
        con.close()
        
    def open_delete_stock():
        top=Toplevel()
        top.title("Delete Stock")
        top.geometry("600x300")
        global ncode3

        ncode3=IntVar()
                    
        F1=LabelFrame(top,text="Delete Stock",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=50,relwidth=1)

        code_lbl=Label(F1,text="Product Code:",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        code_lbl.grid(row=0,column=0,padx=20,pady=5)
        code_txt=Entry(F1,width=20,textvariable=ncode3,font="arial 15",bd=7,relief=SUNKEN)
        code_txt.grid(row=0,column=1,pady=5,padx=10)

        update=Button(F1,text="Delete Stock",command=lambda:delete_stock(),bg="cadetblue",fg="white",pady=15,width=11,font="arial 10 bold")
        update.grid(row=5,column=0,padx=5,pady=5)
        
    def delete_stock():
        a = int(ncode3.get())
        
        con = mysql.connector.connect(user="root",password="mysql",host="localhost",database="test_sd")
        cursor=con.cursor()

        sqlf=("delete from stock where pid=%s"%a)

        try:
          cursor.execute(sqlf)
          con.commit()
          messagebox.showinfo("Done","Record Deleted Successfully")
        except:
          messagebox.showwarning("Warning","Item ID not Exits")                    
        con.close()



    """==========================================Details of product ====="""

    F4=LabelFrame(root,text="Details of Stocks ",bd=10,relief=GROOVE,font=("times new romon",15,"bold"),fg="gold",bg=bg_color)
    F4.place(x=5,y=545,width=755,height=280)

    view_bills=Button(F4,text="View Bills",command=lambda:open_view_bills(),bg="cadetblue",fg="white",pady=15,width=16,font="arial 10 bold")
    view_bills.grid(row=0,column=0,padx=25,pady=25)


    view_stock=Button(F4,text="View Stocks",command=lambda:open_view_stock(),bg="cadetblue",fg="white",pady=15,width=16,font="arial 10 bold")
    view_stock.grid(row=0,column=1,padx=25,pady=25)


    new_stock_entry=Button(F4,text="New Stock Entry",command=open_new_stock,bg="cadetblue",fg="white",pady=15,width=16,font="arial 10 bold")
    new_stock_entry.grid(row=0,column=2,padx=25,pady=25)
      
    update_sto=Button(F4,text="Help",command=lambda:how_to_use(),bd=7,bg="cadetblue",fg="white",pady=15,width=16,font="arial 10 bold")
    update_sto.grid(row=2,column=0,padx=25,pady=25)
        
    update_pri=Button(F4,text="Update Price",command=lambda:open_update_price(),bg="cadetblue",fg="white",pady=15,width=16,font="arial 10 bold")
    update_pri.grid(row=2,column=1,padx=25,pady=25)
        
    delete_sto=Button(F4,text="Delete Stock",command=lambda:open_delete_stock(),bg="cadetblue",fg="white",pady=15,width=16,font="arial 10 bold")
    delete_sto.grid(row=2,column=2,padx=25,pady=25)

    """===============end of stock details====="""       


s=Mainwindow(root)
root.mainloop()

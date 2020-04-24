from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from config import *
import smtplib
from login import *
from datetime import datetime

def yesterday(Uid,y_date,win):
	def addtodb():
		def check():
			def checkentryok():
				import pymysql as mysqli
				hostname="localhost"
				dbuser="root"
				dbpass=""
				dbname="expense"
				conn=mysqli.connect(hostname,dbuser,dbpass,dbname,port=3307)
				cursor=conn.cursor()
				query="insert into item_expense(CID,ITEM,COST,IMP,I_DATE) values ("+str(num)+",'"+str(newitem)+"',"+str(effcost)+","+str(important1)+",'"+str(y_date)+"')"
				res=cursor.execute(query)
				conn.commit()

				c = conn.cursor()
				q = "select * from item_expense"
				result = c.execute(q)
				c.close()
				row = c.fetchall()
				for x in row:
					if x[2] == str(newitem):
						Id = x[0]
				conn.commit()
		
				cur=conn.cursor()
				q1="insert into manage(UID,CID,ITEM_ID,I_DATE) values ("+str(Uid)+","+str(num)+","+str(Id)+",'"+str(y_date)+"')"
				r = cur.execute(q1)
				conn.commit()
		
				add.destroy()
				addd.destroy()
				
				from sendmail import notification
				notification()

			def checkentrycancel():
				addd.destroy()

			addd= Toplevel(topp)
			addd.config(bg="#ffffff")
			addd.geometry("%dx%d+%d+%d" % (300,100,300,150))
			l=Label(addd,text="Confirm?",font=(20),bg="#ffffff",fg="#0000ff" )
			l.place(x=100,y=20,width=100,height=30)

			l=Button(addd,text="OK",font=(10),bg="#449ff3",fg="#ffffff",command=checkentryok )
			l.place(x=33,y=60,width=100,height=30)

			l=Button(addd,text="CANCEL",font=(10),bg="#449ff3",fg="#ffffff",command=checkentrycancel )
			l.place(x=166,y=60,width=100,height=30)

		important1=important.get()
		newitem=item1.get()
		effcost=cost1.get()
		if important1==0:
			newlabel2.config(text="(select this field)")
		elif len(newitem)==0 :
			newlabel.config(text="(enter this field)")
		elif len(effcost)==0 :
			newlabel1.config(text="(enter this field)")
		else:
			check()

	def addexpense(value,value_no):
		global add,item1,cost1,important,num,newlabel,newlabel1,newlabel2
		num=value_no

		add= Toplevel(topp)
		add.config(bg="#449ff3")
		add.geometry("%dx%d+%d+%d" % (700,500,200,50))
		l=Label(add,text=value,font=("Georgia",30,"bold"),bg="#449ff3",fg="#ffffff" )

		l.place(x=200,y=0,width=300,height=100)
		l=Label(add,text="Enter the item :",font=(10),bg="#449ff3",fg="#ffffff" )
		l.place(x=100,y=150,width=200,height=50)

		item1=StringVar()
		item=Entry(add,font=(10),bg="#449ff3",fg="#ffffff",textvariable=item1)
		item.place(x=300,y=150,width=200,height=50)

		newlabel=Label(add,text="",bg="#449ff3",fg="#ff0000")
		newlabel.place(x=510,y=170)

		l=Label(add,text="Enter the cost :",font=(10),bg="#449ff3",fg="#ffffff" )
		l.place(x=100,y=250,width=200,height=50)

		cost1=StringVar()
		cost=Entry(add,font=(10),bg="#449ff3",fg="#ffffff",textvariable=cost1 )
		cost.place(x=300,y=250,width=200,height=50)

		newlabel1=Label(add,text="",bg="#449ff3",fg="#ff0000")
		newlabel1.place(x=510,y=270)

		important=IntVar()
		l=Label(add,text="Is the product important: ",font=(10),bg="#449ff3",fg="#ffffff")
		l.place(x=100,y=350,height=50)

		imp=Radiobutton(add,text="yes",variable=important,value=1,font=(10),bg="#449ff3",fg="#000000" ,activebackground="#449ff3",activeforeground= "#449ff3",selectcolor="#ffffff")
		imp.place(x=350,y=350,height=50)
		
		impp=Radiobutton(add,text="no",variable=important,value=2,font=(10),bg="#449ff3",fg="#000000" ,activebackground="#449ff3",activeforeground= "#449ff3",selectcolor="#ffffff")
		impp.place(x=420,y=350,height=50)

		newlabel2=Label(add,text="",bg="#449ff3",fg="#ff0000")
		newlabel2.place(x=500,y=370)
		
		btn=Button(add,text="ADD",font=(10),command=addtodb)
		btn.place(x=350,y=450)


	global topp, dt
	topp = Toplevel(win)
	topp.config(bg="#ffffff")
	topp.geometry("%dx%d+%d+%d" % (1500,750,0,0))
	l=Label(topp,text="Enter your today's expense",fg="black",font=("Georgia",30,"bold"))
	l.place(x=300,y=10,width=600,height=50)
	btn=Button(topp,text="DONE",font=(10),command=topp.destroy)
	btn.place(x=10,y=10)

	load = Image.open("images/edu.png")
	render = ImageTk.PhotoImage(load)
	img = Label(topp, image=render)
	img.image = render
	img.place(x=100, y=150,width=200,height=200)
	btn=Button(topp,text="Education",bg='#ffffff',font=(10),command=lambda:addexpense("EDUCATION",1))
	btn.place(x=100,y=360,width=200,height=50)

	load = Image.open("images/travell.png")
	render = ImageTk.PhotoImage(load)
	img = Label(topp, image=render)
	img.image = render
	img.place(x=350, y=150,width=200,height=200)
	btn=Button(topp,text="Travel",bg='#ffffff',font=(10),command=lambda:addexpense("TRAVEL",2))
	btn.place(x=350,y=360,width=200,height=50)

	load = Image.open("images/grocery.png")
	render = ImageTk.PhotoImage(load)
	img = Label(topp, image=render)
	img.image = render
	img.place(x=600, y=150,width=200,height=200)
	btn=Button(topp,text="Grocery",bg='#ffffff',font=(10),command=lambda:addexpense("GROCERY",3))
	btn.place(x=600,y=360,width=200,height=50)

	load = Image.open("images/bills.png")
	render = ImageTk.PhotoImage(load)
	img = Label(topp, image=render)
	img.image = render
	img.place(x=850, y=150,width=200,height=200)
	btn=Button(topp,text="Bills",bg='#ffffff',font=(10),command=lambda:addexpense("BILLS",4))
	btn.place(x=850,y=360,width=200,height=50)

	load = Image.open("images/electro.png")
	render = ImageTk.PhotoImage(load)
	img = Label(topp, image=render)
	img.image = render
	img.place(x=1100, y=150,width=200,height=200)
	btn=Button(topp,text="Electronics",bg='#ffffff',font=(10),command=lambda:addexpense("ELECTRONICS",5))
	btn.place(x=1100,y=360,width=200,height=50)

	load = Image.open("images/enter.png")
	render = ImageTk.PhotoImage(load)
	img = Label(topp, image=render)
	img.image = render
	img.place(x=100, y=450,width=200,height=200)
	btn=Button(topp,text="Entertainment",bg='#ffffff',font=(10),command=lambda:addexpense("ENTERTAINMENT",6))
	btn.place(x=100,y=660,width=200,height=50)

	load = Image.open("images/clothes.png")
	render = ImageTk.PhotoImage(load)
	img = Label(topp, image=render)
	img.image = render
	img.place(x=350, y=450,width=200,height=200)
	btn=Button(topp,text="Clothes",bg='#ffffff',font=(10),command=lambda:addexpense("CLOTHES",7))
	btn.place(x=350,y=660,width=200,height=50)

	load = Image.open("images/health.png")
	render = ImageTk.PhotoImage(load)
	img = Label(topp, image=render)
	img.image = render
	img.place(x=600, y=450,width=200,height=200)
	btn=Button(topp,text="Health",bg='#ffffff',font=(10),command=lambda:addexpense("HEALTH",8))
	btn.place(x=600,y=660,width=200,height=50)

	load = Image.open("images/saving.png")
	render = ImageTk.PhotoImage(load)
	img = Label(topp, image=render)
	img.image = render
	img.place(x=850, y=450,width=200,height=200)
	btn=Button(topp,text="Savings",bg='#ffffff',font=(10),command=lambda:addexpense("SAVINGS",9))
	btn.place(x=850,y=660,width=200,height=50)

	load = Image.open("images/other.png")
	render = ImageTk.PhotoImage(load)
	img = Label(topp, image=render)
	img.image = render
	img.place(x=1100, y=450,width=200,height=200)
	btn=Button(topp,text="Other",bg='#ffffff',font=(10),command=lambda:addexpense("OTHER",10))
	btn.place(x=1100,y=660,width=200,height=50)

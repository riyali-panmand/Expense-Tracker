from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image 
from login import *
from datetime import datetime

def sitems(Uid,win):
	global master
	master = Toplevel(win)	
	master.config(bg="#ffffff")
	master.state('zoomed')

	f = ("Georgia",20,"bold")
	f1 = ("Iceland" , 12)
	

	def value():
		def importdate():
			import pymysql as mysqli
			hostname="localhost"
			dbuser="root"
			dbpass=""
			dbname="expense"
			conn=mysqli.connect(hostname,dbuser,dbpass,dbname,port=3307)
			cursor=conn.cursor()
			query="select START_DATE, END_DATE from dateinfo where UID="+str(Uid)
			cursor.execute(query)
			row=cursor.fetchall()
			for y in row:
				cursor=conn.cursor()
				query="select UID,CATEGORY_NAME, ITEM, COST, IMP, i.I_DATE from category c, item_expense i, manage m where c.C_ID=i.CID and i.ITEM_ID=m.ITEM_ID"
				cursor.execute(query)
				row=cursor.fetchall()
				flag=1
				name="\n"
				height=350
				for x in row:
					
					if x[0]==Uid and x[5]==start_date:
						if x[4]==1:
							text="yes"
						else:
							text="no"
						lbl8=Label(master,text=str(x[1]),font=f1,bg="#A1ECF6")
						lbl8.place(x=350,y=int(height),width=200,height=30)
						lbl9=Label(master,text=str(x[2]),font=f1,bg="#A1ECF6")
						lbl9.place(x=550,y=int(height),width=200,height=30)
						lbl10=Label(master,text=str(x[3]),font=f1,bg="#A1ECF6")
						lbl10.place(x=750,y=int(height),width=200,height=30)
						lbl11=Label(master,text=text,font=f1,bg="#A1ECF6")
						lbl11.place(x=950,y=int(height),width=200,height=30)
						height=int(height)+40
						flag=0
						
				if flag==1:
					messagebox.showinfo("Error","No Item ")
					master.destroy()
					
			conn.close()
		flag=0
		feb=0 
		m = mon.get()
		for i in range(len(months)):
			if m == months[i]:
				pos = i
		for i in range(len(months)):
			for j in range(len(monx)):
				if pos==j:
					if monx[j]==0 and int(dt.get())==31:
						flag = 1
					elif monx[j]== -1:
						if int(y.get())%4==0 and int(dt.get())>29:
							feb=1
						elif int(dt.get())>28:
							feb=2
		if flag==1:
			messagebox.showinfo("Error", m + " has only 30 days!")
		elif feb==1:
			messagebox.showinfo("Error", m + " has only 29 days!")
		elif feb==2:
			messagebox.showinfo("Error", m + " has only 28 days!")
			
		start_date = y.get()+"-"+mon.get()+"-"+dt.get()
		start_date=datetime.strptime(start_date, '%Y-%B-%d')
		start_date=datetime.date(start_date)
		importdate()
		
		
	date=[]
	for i in range(1,32):
		date.append(i)
	months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
	monx = [1,-1,1,0,1,0,1,1,0,1,0,1]
	year = [2019,2020,2021,2022]
	d1=["15 days","1 Month","2 Month"]
	now = datetime.now()
	master.config(bg='#ffffff')	

	lb1 = Label(master, text="Select Date", font=f, fg='#449ff3',bg='#ffffff')
	lb1.place(x=100,y=0)

	mon = StringVar(master)
	mon.set(now.strftime("%B")) # default value
	m = OptionMenu(master, mon, *months)
	m.config(compound='right')
	m.place(x=100,y=100)

	dt = StringVar(master)
	dt.set(now.strftime("%d"))
	d = OptionMenu(master, dt, *date)
	d.place(x=180,y=100)

	y = StringVar(master)
	y.set(now.strftime("%Y"))
	y1 = OptionMenu(master, y, *year)
	y1.place(x=250,y=100)

	load = Image.open("images/todays.jpg")
	render = ImageTk.PhotoImage(load)
	img = Label(master, image=render)
	img.place(x=350, y=10,width=800,height=300)

	lbl66=Label(master,text="CATEGORY",font=f, bg="#ffffff",fg='#449ff3')
	lbl66.place(x=350,y=320,width=200,height=30)
	lbl66=Label(master,text="ITEM",font=f, bg="#ffffff",fg='#449ff3')
	lbl66.place(x=550,y=320,width=200,height=30)
	lbl66=Label(master,text="COST",font=f, bg="#ffffff",fg='#449ff3')
	lbl66.place(x=750,y=320,width=200,height=30)
	lbl66=Label(master,text="IMPORTANT",font=f, bg="#ffffff",fg='#449ff3')
	lbl66.place(x=950,y=320,width=200,height=30)

	btn = Button(master, text="DONE" , font=f1 , fg="#ffffff", border=3,bg="#449ff3", command=value)
	btn.place(x=100,y=150)
	
	
			

	mainloop()
from tkinter import *
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
	lbl8=Label(master,text="SORTED LIST OF RECENT MONTH",font=f,fg='#ffffff',bg='#30C2D1')
	lbl8.place(x=400,y=0,width=600,height=40)

	load = Image.open("images/background.jpg")
	render = ImageTk.PhotoImage(load)
	img = Label(master, image=render)
	img.image = render
	img.place(x=20, y=50,height=645)


	load = Image.open("images/background.jpg")
	render = ImageTk.PhotoImage(load)
	imgg = Label(master, image=render)
	imgg.image = render
	imgg.place(x=720, y=50,height=655)


	f = ("Georgia",20,"bold")
	f1 = ("Iceland" , 12)
	lbl8=Label(img,text="CATEGORY",font=f,fg='#ffffff',bg='#30C2D1')
	lbl8.place(x=200,y=10,width=200,height=30)

	lbl8=Label(img,text="CATEGORY",font=f, bg="#ffffff",fg='#449ff3')
	lbl8.place(x=100,y=50,width=200,height=30)

	lbl8=Label(img,text="COST",font=f, bg="#ffffff",fg='#449ff3')
	lbl8.place(x=300,y=50,width=200,height=30)


	lbl8=Label(imgg,text="ITEM",font=f, bg="#30C2D1",fg='#ffffff')
	lbl8.place(x=200,y=10,width=200,height=30)

	lbl8=Label(imgg,text="ITEM",font=f, bg="#ffffff",fg='#449ff3')
	lbl8.place(x=100,y=50,width=200,height=30)

	lbl8=Label(imgg,text="COST",font=f, bg="#ffffff",fg='#449ff3')
	lbl8.place(x=300,y=50,width=200,height=30)


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
	for x in row:
		height=100
		ht=100
		cursor=conn.cursor()
		query="select UID,CATEGORY_NAME, SUM(COST), IMP, i.I_DATE from category c, item_expense i, manage m where c.C_ID=i.CID and i.ITEM_ID=m.ITEM_ID AND UID="+str(Uid)+" AND I.I_DATE>='"+str(x[0])+"' AND I.I_DATE<='"+str(x[1])+"' group by CATEGORY_NAME ORDER BY SUM(COST) DESC"
		cursor.execute(query)
		row=cursor.fetchall()
		for y in row:
			lbl8=Label(img,text=str(y[1]),font=f1,bg="#A1ECF6")
			lbl8.place(x=100,y=int(height),width=200,height=30)
			lbl9=Label(img,text=str(y[2]),font=f1,bg="#A1ECF6")
			lbl9.place(x=300,y=int(height),width=200,height=30)
			height=height+40

		cursor=conn.cursor()
		query="select UID,CATEGORY_NAME,ITEM, SUM(COST), IMP, i.I_DATE from category c, item_expense i, manage m where c.C_ID=i.CID and i.ITEM_ID=m.ITEM_ID AND UID="+str(Uid)+" AND I.I_DATE>='"+str(x[0])+"' AND I.I_DATE<='"+str(x[1])+"' group by ITEM ORDER BY SUM(COST) DESC"
		cursor.execute(query)
		row=cursor.fetchall()
		for y in row:
			lbl8=Label(imgg,text=str(y[2]),font=f1,bg="#A1ECF6")
			lbl8.place(x=100,y=int(ht),width=200,height=30)
			lbl9=Label(imgg,text=str(y[3]),font=f1,bg="#A1ECF6")
			lbl9.place(x=300,y=int(ht),width=200,height=30)
			ht=ht+40
	

	mainloop()
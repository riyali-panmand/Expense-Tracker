from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import re


def Get():
	def Twofun():
		window.destroy()
		from project import Mainpage
		Mainpage()
	def Account():
		text1=name1.get()
		text2=user1.get()
		text3=email1.get()
		if re.search("[a-z | 0-9 | .]+[@]{1}[a-z | . ]+[a-z]+$", text3):
			flag=1
		else:
			flag=0
		text4=phone1.get()
		text5=pwrd1.get()
		text6=conpwrd1.get()
		if text5!=text6:
			messagebox.showinfo("error","Password not same")
		elif len(text1)==0 or len(text2)==0 or len(text3)==0 or len(text4)==0 or len(text5)==0 or len(text6)==0:
			messagebox.showinfo("error","empty string")
		elif len(text5)<8:
			messagebox.showinfo("error","Password should be more than 8 characters")
		elif flag==0:
			messagebox.showinfo("error","Incorrect email")
		elif len(text4)>10 or len(text4)<10:
			messagebox.showinfo("error","Phone number should be of 10 digit")
		elif text5==text6:
			import pymysql as mysqli
			hostname="localhost"
			dbuser="root"
			dbpass=""
			dbname="expense"
			conn=mysqli.connect(hostname,dbuser,dbpass,dbname,port=3307)
			cur=conn.cursor()
			q="select * from userinfo"
			cur.execute(q)
			cur.close()
			r=cur.fetchall()
			f=0
			print(text2)
			for x in r:
				print(x[2])
				if str(x[2])==str(text2):
					f=1
			if f==1:
				messagebox.showinfo("error","Username already exists")
			else:			
				cursor=conn.cursor()
				query="insert into userinfo(NAME,USERNAME,EMAIL,PHONE,PASSWORD) values ('"+text1+"','"+text2+"','"+text3+"','"+text4+"','"+text5+"')"
				res=cursor.execute(query)
				conn.commit()
				if res==1:
					n.set("")
					us.set("")
					e.set("")
					ph.set("")
					pa.set("")
					c.set("")
					messagebox.showinfo("Successful","Account Created")
					window.destroy()
				else:
					messagebox.showinfo("Error","Can't create account")	

				conn.close()
	window=Tk()
	window.config(bg="#ffffff")
	load = Image.open("images/signup.png")
	render = ImageTk.PhotoImage(load)
	img = Label(window, image=render)
	img.Image = render
	img.place(x=250,y=0)

	n=StringVar()
	us=StringVar()
	e=StringVar()
	ph=StringVar()
	pa=StringVar()
	c=StringVar()

	lbl6=Label(img,text="Create Your Account",font=("Georgia",30,"bold"),bg="#ffffff" )
	lbl6.place(x=200, y=10)

	name=Label(img,text="Name :",font=(10),bg="#ffffff",anchor=W)
	name.place(x=200,y=100,width=110,height=50)
	name1=Entry(img,font=(10), border=3,textvariable=n)
	name1.place(x=350,y=100,width=300,height=40)
    
	user=Label(img,text="Username :",font=(10),bg="#ffffff",anchor=W)
	user.place(x=200,y=150,width=110,height=50)
	user1=Entry(img,font=(10),border=2,textvariable=us)
	user1.place(x=350,y=150,width=300,height=40)

	email=Label(img,text="Email :",font=(10),bg="#ffffff",anchor=W)
	email.place(x=200,y=200,width=110,height=50)
	email1=Entry(img,font=(10),border=2,textvariable=e)
	email1.place(x=350,y=200,width=300,height=40)

	phone=Label(img,text="Phone :",font=(10),bg="#ffffff",anchor=W)
	phone.place(x=200,y=250,width=110,height=50)
	phone1=Entry(img,font=(10),border=2,textvariable=ph)
	phone1.place(x=350,y=250,width=300,height=40)

	pwrd=Label(img,text="Password :",font=(10),bg="#ffffff",anchor=W)
	pwrd.place(x=200,y=300,width=110,height=50)
	pwrd1=Entry(img,font=(10),border=2,textvariable=pa)
	pwrd1.place(x=350,y=300,width=300,height=40)
	lb5=Label(img,text="(Use 8 or more characters)",bg="#ffffff",fg="red")
	lb5.place(x=670,y=320)

	conpwrd=Label(img,text="Confirm password :",font=(10),bg="#ffffff",anchor=W)
	conpwrd.place(x=200,y=350,width=180,height=50)
	conpwrd1=Entry(img,font=(10),border=2,textvariable=c)
	conpwrd1.place(x=350,y=350,width=300,height=40)

	btn=Button(img,text="CREATE ACCOUNT",command=Account, bg='#449ff3')
	btn.place(x=310,y=410,width=210,height=50)

	back = Image.open("images/back.jpg")
	back = ImageTk.PhotoImage(back)
	btn=Button(window,text="BACK",image=back,border=0,command=Twofun)
	btn.place(x=0,y=0)
	window.state('zoomed')
	window.mainloop() 

Get()	
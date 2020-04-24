from tkinter import *
from login import *
from PIL import Image,ImageTk
def UserInfo(Uid,win):	
	global t
	t=Toplevel(win)
	t.config(bg="#ffffff")
	t.state('zoomed')
	def TwoFun():
		t.destroy()

	def editName():
		def newName():
			n_name=e.get()
			import pymysql as mysqli
			hostname="localhost"
			dbuser="root"
			dbpass=""
			dbname="expense"
			conn=mysqli.connect(hostname,dbuser,dbpass,dbname,port=3307)
			cursor=conn.cursor()
			query="select * from userinfo"
			cursor.execute(query)
			cursor.close()
			row=cursor.fetchall()
			for x in row:
				if x[0]==Uid:
					cur=conn.cursor()
					q="update userinfo set NAME='"+n_name+"'where USER_ID='"+str(Uid)+"'"
					cur.execute(q)
					conn.commit()
					cur.close()
					conn.close()
			lbl8.config(text=n_name)		
			top.destroy()

		top = Toplevel(topl)
		top.config(bg="#ffffff")
		top.geometry("%dx%d+%d+%d" % (500, 200,380 ,100))
		lb = Label(top,text="Enter new name", bg='#ffffff',font=f1)
		lb.place(x=100,y=50)
		em = Label(top,text="Name" , bg="white", font=f1)
		em.place(x=100,y=100)
		e = Entry(top, font=(10), border=3)
		e.place(x=200,y=100, height=30)
		btn = Button(top, text="Done", bg="#449ff3", fg="white",command=newName)
		btn.place(x=250,y=150,height=35,width=100)
		top.mainloop()

	def editUsername():
		def newUsername():
			n_username=e.get()
			import pymysql as mysqli
			hostname="localhost"
			dbuser="root"
			dbpass=""
			dbname="expense"
			conn=mysqli.connect(hostname,dbuser,dbpass,dbname,port=3307)
			cursor=conn.cursor()
			query="select * from userinfo"
			cursor.execute(query)
			cursor.close()
			row=cursor.fetchall()
			flag=0
			for x in row:
				if x[2]==n_username:
					flag=1
			if flag==0:
				for x in row:
					if x[0]==Uid:
						cur=conn.cursor()
						q="update userinfo set USERNAME='"+n_username+"'where USER_ID='"+str(Uid)+"'"
						cur.execute(q)
						conn.commit()
						cur.close()
						conn.close()
				lbl9.config(text=n_username)		
				top.destroy()
			else:
				messagebox.showinfo("Error","Username already exists")
					

		top = Toplevel(topl)
		top.config(bg="#ffffff")
		top.geometry("%dx%d+%d+%d" % (500, 200,380 ,100))
		lb = Label(top,text="Enter new username", bg='#ffffff',font=f1)
		lb.place(x=100,y=50)
		em = Label(top,text="User Name" , bg="white", font=f1)
		em.place(x=100,y=100)
		e = Entry(top, font=(10), border=3)
		e.place(x=200,y=100, height=30)
		btn = Button(top, text="Done", bg="#449ff3", fg="white",command=newUsername)
		btn.place(x=250,y=150,height=35,width=100)
		top.mainloop()
	def editEmail():
		def newEmail():
			n_email=e.get()
			if re.search("[a-z | 0-9 | .]+[@]{1}[a-z | . ]+[a-z]+$", n_email):
				flag=1
			else:
				flag=0
			if flag==1:	
				import pymysql as mysqli
				hostname="localhost"
				dbuser="root"
				dbpass=""
				dbname="expense"
				conn=mysqli.connect(hostname,dbuser,dbpass,dbname,port=3307)
				cursor=conn.cursor()
				query="select * from userinfo"
				cursor.execute(query)
				cursor.close()
				row=cursor.fetchall()
				for x in row:
					if x[0]==Uid:
						cur=conn.cursor()
						q="update userinfo set EMAIL='"+n_email+"'where USER_ID='"+str(Uid)+"'"
						cur.execute(q)
						conn.commit()
						cur.close()
						conn.close()
				lbl10.config(text=n_email)		
				top.destroy()
			elif flag==0:
				messagebox.showinfo("Error","Incorrect Email")
					

		top = Toplevel(topl)
		top.config(bg="#ffffff")
		top.geometry("%dx%d+%d+%d" % (500, 200,380 ,100))
		lb = Label(top,text="Enter new Email", bg='#ffffff',font=f1)
		lb.place(x=100,y=50)
		em = Label(top,text="Email" , bg="white", font=f1)
		em.place(x=100,y=100)
		e = Entry(top, font=(10), border=3)
		e.place(x=200,y=100, height=30)
		btn = Button(top, text="Done", bg="#449ff3", fg="white",command=newEmail)
		btn.place(x=250,y=150,height=35,width=100)
		top.mainloop()
	def editPhn():
		def newPhn():
			n_phn=e.get()
			if len(n_phn)==10:
				flag=1
			else:
				flag=0
			if flag==1:	
				import pymysql as mysqli
				hostname="localhost"
				dbuser="root"
				dbpass=""
				dbname="expense"
				conn=mysqli.connect(hostname,dbuser,dbpass,dbname,port=3307)
				cursor=conn.cursor()
				query="select * from userinfo"
				cursor.execute(query)
				cursor.close()
				row=cursor.fetchall()
				for x in row:
					if x[0]==Uid:
						cur=conn.cursor()
						q="update userinfo set PHONE='"+n_phn+"'where USER_ID='"+str(Uid)+"'"
						cur.execute(q)
						conn.commit()
						cur.close()
						conn.close()
				lbl11.config(text=n_phn)		
				top.destroy()
			elif flag==0:
				messagebox.showinfo("Error","Mobile number should have 10 digits")
					

		top = Toplevel(topl)
		top.config(bg="#ffffff")
		top.geometry("%dx%d+%d+%d" % (500, 200,380 ,100))
		lb = Label(top,text="Enter new Phone number", bg='#ffffff',font=f1)
		lb.place(x=100,y=50)
		em = Label(top,text="Phone Number" , bg="white", font=f1)
		em.place(x=100,y=100)
		e = Entry(top, font=(10), border=3)
		e.place(x=200,y=100, height=30)
		btn = Button(top, text="Done", bg="#449ff3", fg="white",command=newPhn)
		btn.place(x=250,y=150,height=35,width=100)
		top.mainloop()	
	def editPsw():
		def newPsw():
			n_psw=e.get()
			if len(n_psw)==8:
				flag=1
			else:
				flag=0
			if flag==1:	
				import pymysql as mysqli
				hostname="localhost"
				dbuser="root"
				dbpass=""
				dbname="expense"
				conn=mysqli.connect(hostname,dbuser,dbpass,dbname,port=3307)
				cursor=conn.cursor()
				query="select * from userinfo"
				cursor.execute(query)
				cursor.close()
				row=cursor.fetchall()
				for x in row:
					if x[0]==Uid:
						cur=conn.cursor()
						q="update userinfo set PASSWORD='"+n_psw+"'where USER_ID='"+str(Uid)+"'"
						cur.execute(q)
						conn.commit()
						cur.close()
						conn.close()
				lbl12.config(text=n_psw)		
				top.destroy()
			elif flag==0:
				messagebox.showinfo("Error","Password should be of 8 characters")
					

		top = Toplevel(topl)
		top.config(bg="#ffffff")
		top.geometry("%dx%d+%d+%d" % (500, 200,380 ,100))
		lb = Label(top,text="Enter new password", bg='#ffffff',font=f1)
		lb.place(x=100,y=50)
		em = Label(top,text="Password" , bg="white", font=f1)
		em.place(x=100,y=100)
		e = Entry(top, font=(10), border=3)
		e.place(x=200,y=100, height=30)
		btn = Button(top, text="Done", bg="#449ff3", fg="white",command=newPsw)
		btn.place(x=250,y=150,height=35,width=100)
		top.mainloop()	
	def call():
		import pymysql as mysqli
		hostname="localhost"
		dbuser="root"
		dbpass=""
		dbname="expense"
		conn=mysqli.connect(hostname,dbuser,dbpass,dbname,port=3307)
		cursor=conn.cursor()
		query="select * from userinfo"
		cursor.execute(query)
		row=cursor.fetchall()
		for x in row:
			if x[0]==Uid:
				name=x[1]
				usern=x[2]
				email=x[3]
				phone=x[4]
				passw=x[5]
				lbl8.config(text=name)
				lbl9.config(text=usern)
				lbl10.config(text=email)
				lbl11.config(text=phone)
				lbl12.config(text=passw)
		conn.close()			

	load = Image.open("images/userbg.jpg")
	img = ImageTk.PhotoImage(load)
	topl = Label(t, image=img)
	topl.image = img 
	topl.place(x=115,y=0)

	btn=Button(topl,text="back",font=(10),command=TwoFun)
	btn.place(x=0,y=0)

	f = ("Iceland",13,"bold")
	f1 = ("Iceland" , 12)	
	lbl=Label(topl,text="MY ACCOUNT",font=("Georgia",30,"bold"),bg="#ffffff")
	lbl.place(x=250,y=10,width=500,height=50)

	lbl=Label(topl,text="NAME ",font=f,anchor=W,fg="#ffffff",bg='#449ff3')
	lbl.place(x=0,y=200,width=200,height=50)
	lbl8=Label(topl,font=f1,anchor=W, fg="#ffffff",bg='#30C2D1')
	lbl8.place(x=200,y=200,width=300,height=50)
	lbl=Button(topl,text="EDIT",font=f,anchor=W,fg="#ffffff",bg='#449ff3',command=editName)
	lbl.place(x=510,y=200,height=50)
	
	lbl=Label(topl,text="USERNAME ",font=f,anchor=W, fg="#ffffff",bg='#449ff3')
	lbl.place(x=0,y=300,width=200,height=50)
	lbl9=Label(topl,font=f1,anchor=W, fg="#ffffff",bg='#30C2D1')
	lbl9.place(x=200,y=300,width=300,height=50)
	lbl=Button(topl,text="EDIT",font=f,anchor=W,fg="#ffffff",bg='#449ff3',command=editUsername)
	lbl.place(x=510,y=300,height=50)
	
	lbl=Label(topl,text="EMAIL ",font=f,anchor=W, fg="#ffffff",bg='#449ff3')
	lbl.place(x=0,y=400,width=200,height=50)
	lbl10=Label(topl,font=f1,anchor=W, fg="#ffffff",bg='#30C2D1')
	lbl10.place(x=200,y=400,width=300,height=50)
	lbl=Button(topl,text="EDIT",font=f,anchor=W,fg="#ffffff",bg='#449ff3',command=editEmail)
	lbl.place(x=510,y=400,height=50)
	
	lbl=Label(topl,text="PHONE NUMBER ",font=f,anchor=W, fg="#ffffff",bg='#449ff3')
	lbl.place(x=0,y=500,width=200,height=50)	
	lbl11=Label(topl,font=f1,anchor=W, fg="#ffffff",bg='#30C2D1')
	lbl11.place(x=200,y=500,width=300,height=50)
	lbl=Button(topl,text="EDIT",font=f,anchor=W,fg="#ffffff",bg='#449ff3',command=editPhn)
	lbl.place(x=510,y=500,height=50)
	
	lbl=Label(topl,text="YOUR PASSWORD ",font=f,anchor=W, fg="#ffffff",bg='#449ff3')
	lbl.place(x=0,y=600,width=200,height=50)	
	lbl12=Label(topl,font=f1,anchor=W, fg="#ffffff",bg='#30C2D1')
	lbl12.place(x=200,y=600,width=300,height=50)
	lbl=Button(topl,text="EDIT",font=f,anchor=W,fg="#ffffff",bg='#449ff3',command=editPsw)
	lbl.place(x=510,y=600,height=50)

	call()
	

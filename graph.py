from tkinter import *
import calendar
from PIL import Image,ImageTk
from tkinter import messagebox
from login import *
from datetime import datetime
from matplotlib import pyplot

def graph(Uid,win):
	def exp_graph():
		flag1=0
		feb1=0
		flag2=0
		feb2=0 
		m1 = mon1.get()
		m2 = mon2.get()
		for i in range(len(months)):
			if m1 == months[i]:
				pos1 = i
			if m2 == months[i]:
				pos2 = i	
		for i in range(len(months)):
			for j in range(len(monx)):
				if pos1==j:
					if monx[j]==0 and int(dt1.get())==31:
						flag1 = 1
					elif monx[j]== -1:
						if int(y1.get())%4==0 and int(dt1.get())>29:
							feb1=1
						elif int(dt1.get())>28:
							feb1=2
		if flag1==1:
			messagebox.showinfo("Error", m1 + " has only 30 days!")
		elif feb1==1:
			messagebox.showinfo("Error", m1 + " has only 29 days!")
		elif feb1==2:
			messagebox.showinfo("Error", m1 + " has only 28 days!")

		for i in range(len(months)):
			for j in range(len(monx)):
				if pos2==j:
					if monx[j]==0 and int(dt2.get())==31:
						flag2 = 1
					elif monx[j]== -1:
						if int(y2.get())%4==0 and int(dt2.get())>29:
							feb2=1
						elif int(dt1.get())>28:
							feb2=2
		if flag2==1:
			messagebox.showinfo("Error", m2 + " has only 30 days!")
		elif feb2==1:
			messagebox.showinfo("Error", m2 + " has only 29 days!")
		elif feb2==2:
			messagebox.showinfo("Error", m2 + " has only 28 days!")
		import pymysql as mysqli
		hostname="localhost"
		dbuser="root"
		dbpass=""
		dbname="expense"
		conn=mysqli.connect(hostname,dbuser,dbpass,dbname,port=3307)
		cur = conn.cursor()
		query = "select * from category"
		res = cur.execute(query)
		row = cur.fetchall()
		cur.close()
		sd = y1.get()+"-"+mon1.get()+"-"+str(dt1.get())
		sd = datetime.strptime(sd, '%Y-%B-%d')
		sd = datetime.date(sd)
		ed = y2.get()+"-"+mon2.get()+"-"+str(dt2.get())
		ed = datetime.strptime(ed, '%Y-%B-%d')
		ed = datetime.date(ed)
		if sd>ed:
			messagebox.showinfo("Error","Invalid Dates !!!")
		x = []
		y = []
		for i in row:
			s = str(i[1])
			x.append(s)	
		cur = conn.cursor()
		query = "select UID,m.CID,SUM(COST) from manage as m,item_expense as i where UID = '"+str(Uid)+"'and m.ITEM_ID=i.ITEM_ID and i.I_DATE>='"+str(sd)+"' and i.I_DATE<='"+str(ed)+"' group by m.CID"
		res = cur.execute(query)
		row = cur.fetchall()
		k=0	
		for i in row:
			for j in range(k,10):
				if j+1==int(i[1]):
					y.insert(j,int(i[2]))
					k=k+1
					break
				else:
					y.insert(j,0)
					k=k+1	
		if len(y)!=10:
			for i in range(len(y),10):
				y.insert(i,0)									
		cur.close()
		pyplot.bar(x ,y , color=(0.2, 0.4, 1, 1))
		pyplot.show()


	global master,now
	master = Toplevel(win)	
	master.geometry("%dx%d+%d+%d" % (500,500,500,100))
	
	date=[]
	for i in range(1,32):
		date.append(i)
	months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
	monx = [1,-1,1,0,1,0,1,1,0,1,0,1]
	year = [2019,2020,2021,2022]
	d1=["1 Month"]
	now = datetime.now()
	master.config(bg='#ffffff')
	f1 = ('Georgia' , 20 , 'bold')	

	lb1 = Label(master, text="Start Date", font=f1, fg='#449ff3',bg='#ffffff')
	lb1.place(x=120,y=100)

	mon1 = StringVar(master)
	mon1.set(now.strftime("%B")) # default value
	m1 = OptionMenu(master, mon1, *months)
	m1.config(compound='right')
	m1.place(x=100,y=150)

	dt1 = StringVar(master)
	dt1.set(now.strftime("%d"))
	d1 = OptionMenu(master, dt1, *date)
	d1.place(x=250,y=150)

	y1 = StringVar(master)
	y1.set(now.strftime("%Y"))
	y11 = OptionMenu(master, y1, *year)
	y11.place(x=320,y=150)

	lb2 = Label(master, text="End Date", font=f1, fg='#449ff3',bg='#ffffff')
	lb2.place(x=120,y=200)

	mon2 = StringVar(master)
	mon2.set(now.strftime("%B")) # default value
	m2 = OptionMenu(master, mon2, *months)
	m2.config(compound='right')
	m2.place(x=100,y=250)

	dt2 = StringVar(master)
	dt2.set(now.strftime("%d"))
	d2 = OptionMenu(master, dt2, *date)
	d2.place(x=250,y=250)

	y2 = StringVar(master)
	y2.set(now.strftime("%Y"))
	y12 = OptionMenu(master, y2, *year)
	y12.place(x=320,y=250)

	btn = Button(master, text="View Graph" , font=f1 , fg="#ffffff", border=3,bg="#449ff3", command=exp_graph)
	btn.place(x=190,y=300)

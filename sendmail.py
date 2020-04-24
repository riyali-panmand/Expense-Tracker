from tkinter import *
from config import *
import smtplib
from login import *
from datetime import datetime
from today import *

def notification():
	import pymysql as mysqli
	hostname="localhost"
	dbuser="root"
	dbpass=""
	dbname="expense"
	conn=mysqli.connect(hostname,dbuser,dbpass,dbname,port=3307)
	cursor = conn.cursor()
	q = "select * from dateinfo"
	res = cursor.execute(q)
	cursor.close()

	cur = conn.cursor()
	query = "select * from item_expense"
	r = cur.execute(query)
	cur.close()

	c = conn.cursor()
	q1 = "select * from manage"
	r1 = c.execute(q1)
	c.close()

	c1 = conn.cursor()
	q2 = "select * from userinfo"
	r2 = c1.execute(q2)
	c1.close()

	date = cursor.fetchall()
	item = cur.fetchall()
	manage = c.fetchall()
	user = c1.fetchall()
	for x in date:
		if x[4] == int(Uid):
			exp = x[3]
			sd = x[1]
			ed = x[2]
	cost = 0		
	for y in manage:
		if y[1]==int(Uid):
			id = y[3]
			d = y[4]		
			for z in item:
				if id==z[0]:
					if z[5]>=sd and z[5]<=ed:
						cost += z[3]

	exp50 = exp*0.5
	exp75 = exp*0.75	
	exp90 = exp*0.9
	exp100 = exp
	flag=0
	print(cost)
	if int(cost)>=exp50 and int(cost)<exp75:
		b = "Your expense for the current month has reached 50%"
		flag = 1
	elif cost>=exp75 and cost<exp90:
		b = "Your expense for the current month has reached 75%"
		flag = 1
	elif cost>=exp90 and cost<exp100:
		b = "Your expense for the current month has reached 90%"
		flag = 1
	else:
		b = "You have reached your maximum expense limit!!!"
		flag = 1

	for i in user:
		if i[0]==int(Uid):
			if flag==1:		
				smtp=smtplib.SMTP("smtp.gmail.com",587)
				smtp.ehlo()
				smtp.starttls()
				smtp.ehlo()
				smtp.login(username,password)
				subject="Notification"
				body=b
				msg='subject:'+subject+'\n\n'+body
				smtp.sendmail(username,i[3],msg)





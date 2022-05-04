import mysql.connector
from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import*
from datetime import datetime
import re

now = datetime.now() 
dt_string = now.strftime("%d/%m/%Y  %H:%M:%S")

db=mysql.connector.connect(
host="localhost",
user="root",
passwd="abc456",
database="project"
)

def fun1():
	bmi_window.deiconify()   
	main_window.withdraw()
def fun2():
	cal_window.deiconify()
	bmi_window.withdraw()
def fun3():
	view_window.deiconify()
	bmi_window.withdraw()
	view_data.delete(1.0,END)
	info=""
	try:
		cursor=db.cursor()
		sql="select * from bmi"
		cursor.execute(sql)
		data=cursor.fetchall()
		db.commit()
		for d in data:
			info=info+" id:"+str(d[0])+"\n Name:"+str(d[1])+"                  Age:"+str(d[2])+"\n Phone:"+str(d[3])+"    Gender:"+str(d[4])+"\n Height:"+str(d[5])+"                 Weight:"+str(d[6])+"\n *************************""\n"
		view_data.insert(INSERT,info)
	except Exception as e:
		db.rollback()

def fun4():
	try:
		cursor=db.cursor()
		cursor.callproc('p2')
		db.commit()
		showinfo("Data","Data has exported successfully....")
	except Exception as e:
		db.rollback()
def fun5():
	profdes_window.deiconify()
	bmi_window.withdraw()
def fun6():
	main_window.deiconify()
	bmi_window.withdraw()
def fun7():
	try:
		cursor=db.cursor()
		sql1 = "INSERT INTO bmi VALUES ('%d','%s','%d','%d','%s','%f','%f')"
		try:		
			id = int(cal_ent_id.get())
			id !=0
		except ValueError:
			showerror("ID Issue","Not accepted") 
			showerror("ID Issue","ID is empty")
			cal_ent_id.delete(0, END)
			cal_ent_id.focus()
			return	
		else:
			if (int(id) == 0) or (int(id) < 0):
				showerror("ID Issue","ID should be positive")
				cal_ent_id.delete(0, END)
				cal_ent_id.focus()
				return
		name = cal_ent_name.get()
		len(name) != 0
		if len(name) == 0:
			showerror("Name Issue", "Name is empty")
			cal_ent_name.delete(0, END)
			cal_ent_name.focus()
			return
		
	#Min Name Limit:

		if len(name) < 2:
			showerror("Name Issue","should enter more characters ")
			cal_ent_name.delete(0, END)
			cal_ent_name.focus()
			return	
			
		if not name.isalpha() :
			showerror("Issue", "should enter a name in alphabate only")
			cal_ent_name.delete(0, END)
			cal_ent_name.focus()
			return
		
	# Max Name Limit:
	
		len(name) == 15
		if len(name) > 15:
			showerror("Warning","Name limit exceeding ")
			cal_ent_name.delete(0, END)
			cal_ent_name.focus()
			return

		try:		
			age = int(cal_ent_age.get())
			age !=0
		except ValueError:
			showerror("Age Issue","Not accepted") 
			showerror("AGE Issue","age is empty")
			cal_ent_age.delete(0, END)
			cal_ent_age.focus()
			return	
		else:
			if (int(age) == 0) or (int(age) < 0):
				showerror("age Issue","age should be positive number")
				cal_ent_age.delete(0, END)
				cal_ent_age.focus()
				return	

		try:		
			phone = int(cal_ent_phone.get())
			phone !=0
		except ValueError:
			showerror("phone Issue","Not accepted") 
			showerror("phone Issue","age is empty")
			cal_ent_phone.delete(0, END)
			cal_ent_phone.focus()
			return	
		else:
			r=re.fullmatch('[6-9][0-9]{9}',str(phone))
			if r==None:
				showerror("phone issue","Invalid Phone number")
				cal_ent_phone.delete(0, END)
				cal_ent_phone.focus()
				return	
		
			if (int(phone) == 0) or (int(phone) < 0):
				showerror("age Issue","age should be positive number")
				cal_ent_phone.delete(0, END)
				cal_ent_phone.focus()
				return	


		if fb.get()==1:
			gender="Male"
		else:
			gender="Female"

		try:		
			height1=cal_ent_height.get()
			height=float(height1)
			height !=0
		except ValueError:
			showerror("height Issue","Not accepted") 
			showerror("height Issue","HEIGHT is empty")
			cal_ent_height.delete(0, END)
			cal_ent_height.focus()
			return	
		else:
			if (int(height) == 0) or (int(height) < 0):
				showerror("height Issue","height should be positive")
				cal_ent_height.delete(0, END)
				cal_ent_height.focus()
				return
		try:		
			weight1=cal_ent_wt.get()
			weight=float(weight1)	
			weight !=0
		except ValueError:
			showerror("weight Issue","Not accepted") 
			showerror("weight Issue","weight is empty")
			cal_ent_wt.delete(0, END)
			cal_ent_wt.focus()
			return	
		else:
			if (int(weight) == 0) or (int(weight) < 0):
				showerror("weight Issue","weight should be positive")
				cal_ent_wt.delete(0, END)
				cal_ent_wt.focus()
				return
		#val = (id,name,age,phone,gender,height,weight)
		cursor.execute(sql1%(id,name,age,phone,gender,height,weight))
		db.commit()
		showinfo("information", "Record inserted successfully...")
		id = int(cal_ent_id.get())
		height1=float(cal_ent_height.get())
		weight1=int(cal_ent_wt.get())
		bmi=(weight1/(height1*height1))
		height=str(height1)
		weight=str(weight1)
		#query="select height,weight,(weight/power(height,2)) as bmi from bmi where id=%s" %(id,)
		#cursor.execute(query)
		#data=cursor.fetchall()
		db.commit()
		#for row in data:
		#mass="BMI IS: "bmi,"\n Height is:"height,"\n Weight is:"weight
		showinfo("BMI:","BMI is: "+str(bmi))
		if bmi<18.5:
			showinfo("BMI range","You are in underweight range")
		elif 18.5<bmi<24.9:
			showinfo("BMI range","You are in Healthy weight range")
		elif 25<bmi<29.9:
			showinfo("BMI range","You are in overweight range")
		else:
			showinfo("BMI range","You are in obese range")
		cal_ent_id.delete(0,END)
		cal_ent_name.delete(0,END)
		cal_ent_age.delete(0,END)
		cal_ent_phone.delete(0,END)
		cal_ent_height.delete(0,END)
		cal_ent_wt.delete(0,END)
		cal_ent_id.focus()
		cursor.close()
	except Exception as e:
		db.rollback()
		showerror("issue","ID already exists")
		cal_ent_id.delete(0,END)
		cal_ent_id.focus()

def fun8():
	bmi_window.deiconify()
	cal_window.withdraw()
def fun9():
	htcon_window.deiconify()
	cal_window.withdraw()
def fun10():
	try:
		cursor=db.cursor()
		sql = "INSERT INTO con VALUES ('%d','%d','%d')"
		try:
			cid = int(htcon_ent_cid.get())
			cid != 0
		except ValueError:
			showerror("CID Issue","Not accepted") 
			showerror("CID Issue","CID is empty")
			htcon_ent_cid.delete(0, END)
			htcon_ent_cid.focus()
			return	
		else:
			if (int(cid) == 0) or (int(cid) < 0):
				showerror("CID Issue","CID should be positive")
				htcon_ent_cid.delete(0, END)
				htcon_ent_cid.focus()
				return

		try:
			feet = int(htcon_ent_feet.get())
			#fe=len(str(feet))
			feet != 0
		except ValueError:
			showerror("feet Issue","Not accepted") 
			showerror("feet Issue","feet is empty")
			htcon_ent_feet.delete(0, END)
			htcon_ent_feet.focus()
			return	
		else:
			if ((int(feet) == 0) or (int(feet) < 2) or (int(feet)>7)):
				showerror("feet Issue","feet should be in between 2 to 7")
				htcon_ent_feet.delete(0, END)
				htcon_ent_feet.focus()
				return
		try:
			inches = int(htcon_ent_inches.get())
			inches != 0
		except ValueError:
			showerror("inches Issue","Not accepted") 
			showerror("inches Issue","inches is empty")
			htcon_ent_inches.delete(0, END)
			htcon_ent_inches.focus()
			return	
		else:
			if ((int(inches) == 0) or (int(inches) < 0) or (int(inches)>11)):
				showerror("inches Issue","inches should be in between 0 to 11")
				htcon_ent_inches.delete(0, END)
				htcon_ent_inches.focus()
				return
		cursor.execute(sql%(cid,feet,inches))
		db.commit()
		showinfo("information", "Record inserted successfully...")
		feet=int(htcon_ent_feet.get())
		cid=int(htcon_ent_cid.get())
		inches=int(htcon_ent_inches.get())
		height=(feet*12+inches)/39.37
		#query="select feet,inch,((feet*12+inch)/39.37) as HT from con where cid=%s" %(cid,)
		#cursor.execute(query)
		#data=cursor.fetchall()
		db.commit()
		#for row in data:
		#mass="height: "+(str(row[2]))
			
		showinfo("Height:","Height is: "+str(height))
		htcon_ent_cid.delete(0,END)
		htcon_ent_feet.delete(0,END)
		htcon_ent_inches.delete(0,END)
		htcon_ent_cid.focus()
	except Exception as e:
		db.rollback()
		showerror("issue",e)
		htcon_ent_cid.delete(0,END)
		htcon_ent_cid.focus()

	 

def fun11():
	cal_window.deiconify()
	htcon_window.withdraw()
def fun12():
	prof_window.deiconify()
	cal_window.withdraw()

def fun13():
	try:
		cursor=db.cursor()
		sql2="INSERT INTO prof values('%d','%s')"
		try:		
			pid = int(prof_ent_id.get())
			pid != 0
		except ValueError:
			showerror("PID Issue","Not accepted") 
			showerror("PID Issue","PID is empty")
			prof_ent_id.delete(0, END)
			prof_ent_id.focus()
			return	
		else:
			if (int(pid) == 0) or (int(pid) < 0):
				showerror("PID Issue","PID should be positive")
				prof_ent_id.delete(0, END)
				prof_ent_id.focus()
				return
		profession= prof_ent_prof.get()
		len(profession) != 0
		if len(profession) == 0:
			showerror("Profession Issue", "Profession is empty")
			prof_ent_prof.delete(0, END)
			prof_ent_prof.focus()
			return

		if len(profession) < 2:
			showerror("Profession Issue","should enter more characters ")
			prof_ent_prof.delete(0, END)
			prof_ent_prof.focus()
			return	
			
		if not profession.isalpha() :
			showerror("Issue", "should enter a profession in alphabate only")
			prof_ent_prof.delete(0, END)
			prof_ent_prof.focus()
			return
	
		len(profession) == 15
		if len(profession) > 15:
			showerror("Warning","Profession limit exceeding ")
			prof_ent_prof.delete(0, END)
			prof_ent_prof.focus()
			return

		cursor.execute(sql2%(pid,profession))
		db.commit()
		showinfo("information", "Record inserted successfully...")
		prof_ent_id.delete(0,END)
		prof_ent_prof.delete(0,END)
		prof_ent_id.focus()
	except Exception as e:
		db.rollback()
		showerror("issue","please enter a data for valid ID only")
		prof_ent_id.delete(0,END)
		prof_ent_id.focus()
	
def fun14():
	cal_window.deiconify()
	prof_window.withdraw()
def fun15():
	bmi_window.deiconify()
	view_window.withdraw()
def fun16():
	try:
		cursor=db.cursor()
		cursor.callproc('p4')
		for records in cursor.stored_results():
			result=records.fetchall()
		db.commit()
		for row in result:
			mass="Name: "+(str(row[3]))+"  ,  Age: "+(str(row[4]))+"\nPhone: "+(str(row[5]))+"  ,  Gender: "+(str(row[6]))+"\nHeight: "+(str(row[7]))+"  ,  Weight: "+(str(row[8]))
						
			showinfo("Information:",mass)
	except Exception as e:
		print(e)
		db.rollback()
	

def fun17():

	try:
		cursor=db.cursor()
		cursor.callproc('p5')
		for records in cursor.stored_results():
			result=records.fetchall()
		db.commit()
		for row in result:
			mass="Name: "+(str(row[3]))+"  ,  Age: "+(str(row[4]))+"\nPhone: "+(str(row[5]))+"  ,  Gender: "+(str(row[6]))+"\nHeight: "+(str(row[7]))+"  ,  Weight: "+(str(row[8]))
						
			showinfo("Information:",mass)
	except Exception as e:
		db.rollback()

def fun18():
	try:
		cursor=db.cursor()
		cursor.callproc('p10')
		for records in cursor.stored_results():
			result=records.fetchall()
		db.commit()
		for row in result:
			mass="Name: "+(str(row[3]))+"  ,  Age: "+(str(row[4]))+"\nPhone: "+(str(row[5]))+"  ,  Gender: "+(str(row[6]))+"\nHeight: "+(str(row[7]))+"  ,  Weight: "+(str(row[8]))
						
			showinfo("Information:",mass)
	except Exception as e:
		showerror(e)
		db.rollback()
	

def fun19():
	try:
		cursor=db.cursor()
		cursor.callproc('p7')
		for records in cursor.stored_results():
			result=records.fetchall()
		db.commit()
		for row in result:
			mass="Name: "+(str(row[3]))+"  ,  Age: "+(str(row[4]))+"\nPhone: "+(str(row[5]))+"  ,  Gender: "+(str(row[6]))+"\nHeight: "+(str(row[7]))+"  ,  Weight: "+(str(row[8]))
						
			showinfo("Information:",mass)
	except Exception as e:
		showerror(e)
		db.rollback()	
def fun20():
	bmi_window.deiconify()
	profdes_window.withdraw()
def before_insert(self):
	cursor=db.cursor()
	sql="""create trigger t1 before insert on bmi for each row begin if (new.id is null)or(new.id<1) then signal SQLSTATE '12345' set message_text="PID should be greater than 1 digit" end if;
	        if (new.name is null)or(length(new.name)<2)or 
		(length(new.name)>15) or 
		(not(new.name regexp "^[A-Za-z ]*$")) then
		signal SQLSTATE '23456'
		set message_text="invalide name";
		end if;

		if (new.age is null)or(new.age<1) then
		signal SQLSTATE '34567'
		set message_text="invalide age";
		end if;

	
		if (new.phone is null)or(new.phone<10000000000) then
		signal SQLSTATE '45678'
		set message_text="invalide phone";
		end if;

		if (new.height is null)or(new.height<0) then
		signal SQLSTATE '56789'
		set message_text="invalide height";
		end if;
	
		if (new.weight is null)or(new.weight<0) then
		signal SQLSTATE '67890'
		set message_text="invalide weight";
		end if;
	        end"""
	self.db.execute(sql)
	self.connect.commit()
main_window=Tk()
main_window.title("WELCOME")
main_window.geometry("650x430+400+100")
main_window.configure(bg="PaleGreen3")
f1=("Times New Roman",60,"bold")
mw_lbl=Label(main_window,text="BMI Calsi \n by Prasad Bhange",font=f1,fg="red")
mw_lbl.place(x=2,y=60)
f2=("Times New Roman",20,"bold")
mw_btn=Button(main_window,text="Start",font=f2,width=6,command=fun1)
mw_btn.place(x=270,y=310)



bmi_window=Toplevel(main_window) 
bmi_window.title("BMI Calculator")
bmi_window.geometry("500x500+400+100")
bmi_window.configure(bg="SlateGray3")
bmi_btn_cal=Button(bmi_window,text="Calculate BMI",font=f2,width=11,command=fun2)
bmi_btn_his=Button(bmi_window,text="View History",font=f2,width=11,command=fun3)
bmi_btn_exp=Button(bmi_window,text="Export Data",font=f2,width=11,command=fun4)
bmi_btn_profession=Button(bmi_window,text="Profession \n wise data",font=f2,width=11,command=fun5)
bmi_btn_cal.pack(pady=10)
bmi_btn_his.pack(pady=10)
bmi_btn_exp.pack(pady=10)
bmi_btn_profession.pack(pady=10)
bmi_lbl_date=Label(bmi_window,text="Now:"+str(now),font=f2)
bmi_lbl_date.place(x=5,y=400)
bmi_lbl_time=Label(bmi_window,text="Date & Time:"+str(dt_string),font=f2)
bmi_lbl_time.place(x=5,y=450)
bmi_btn_back=Button(bmi_window,text="Back",font=f2,width=6,command=fun6)
bmi_btn_back.pack(pady=10)
bmi_window.withdraw()

view_window=Toplevel(bmi_window)
view_window.title("View")
view_window.geometry("500x450+400+100")
view_window.configure(bg="khaki3")
view_data=ScrolledText(view_window,width=30,height=10,font=f2)
view_btn_back=Button(view_window,text="Back",font=f2,command=fun15)
view_data.pack(pady=10)
view_btn_back.pack(pady=10)
view_window.withdraw()

profdes_window=Toplevel(bmi_window)
profdes_window.title("Profession list")
profdes_window.geometry("500x450+400+100")
profdes_window.configure(bg="khaki3")
profdes_btn_doc=Button(profdes_window,text="Doctor",font=f2,width=10,command=fun16)
profdes_btn_doc.pack(pady=10)
profdes_btn_eng=Button(profdes_window,text="Engineer",font=f2,width=10,command=fun17)
profdes_btn_eng.pack(pady=10)
profdes_btn_army=Button(profdes_window,text="Indian Army",font=f2,width=10,command=fun18)
profdes_btn_army.pack(pady=10)
profdes_btn_tea=Button(profdes_window,text="Teacher",font=f2,width=10,command=fun19)
profdes_btn_tea.pack(pady=10)
profdes_btn_back=Button(profdes_window,text="Back",font=f2,width=6,command=fun20)
profdes_btn_back.pack(pady=10)
profdes_window.withdraw()

cal_window=Toplevel(bmi_window) 
cal_window.title("Calculate")
cal_window.geometry("700x570+400+100")
cal_window.configure(bg="SlateGray3")
cal_lbl_id=Label(cal_window,text="Identity no:",font=f2)
cal_ent_id=Entry(cal_window,bd=5,font=f2)
cal_lbl_name=Label(cal_window,text="enter name:",font=f2)
cal_ent_name=Entry(cal_window,bd=5,font=f2)
cal_lbl_age=Label(cal_window,text="enter age:",font=f2)
cal_ent_age=Entry(cal_window,bd=5,font=f2)
cal_lbl_phone=Label(cal_window,text="enter phone:",font=f2)
cal_ent_phone=Entry(cal_window,bd=5,font=f2)
cal_lbl_gender=Label(cal_window,text="Gender:",font=f2)
fb=IntVar()
fb.set(1)
cal_radio_gender1=Radiobutton(cal_window, text="Male",font=f2,variable=fb,value=1)
cal_radio_gender2=Radiobutton(cal_window, text="Female",font=f2,variable=fb,value=2)
cal_lbl_height=Label(cal_window,text="enter height in mtr:",font=f2)
cal_ent_height=Entry(cal_window,bd=5,font=f2)
cal_btn_convert=Button(cal_window,text="Convert",font=f2,width=7,command=fun9)
cal_lbl_wt=Label(cal_window,text="enter weight in kg:",font=f2)
cal_ent_wt=Entry(cal_window,bd=5,font=f2)
cal_btn_prof=Button(cal_window,text="Enter Profession",font=f2,command=fun12)
cal_btn_cal=Button(cal_window,text="Calculate",font=f2,command=fun7)
cal_btn_back=Button(cal_window,text="Back",font=f2,command=fun8)

cal_lbl_id.place(x=4,y=15)
cal_ent_id.place(x=250,y=15)
cal_lbl_name.place(x=4,y=71)
cal_ent_name.place(x=250,y=71)
cal_lbl_age.place(x=4,y=127)
cal_ent_age.place(x=250,y=127)
cal_lbl_phone.place(x=4,y=187)
cal_ent_phone.place(x=250,y=187)
cal_lbl_gender.place(x=4,y=247)
cal_radio_gender1.place(x=250,y=247)
cal_radio_gender2.place(x=370,y=247)
cal_lbl_height.place(x=4,y=307)
cal_ent_height.place(x=250,y=307)
cal_btn_convert.place(x=570,y=307)
cal_lbl_wt.place(x=4,y=367)
cal_ent_wt.place(x=250,y=367)
cal_btn_prof.place(x=4,y=427)
cal_btn_cal.place(x=250,y=500)
cal_btn_back.place(x=430,y=500)

cal_window.withdraw()

htcon_window=Toplevel(cal_window) 
htcon_window.title("Height Converter")
htcon_window.geometry("520x630+400+100")
htcon_window.configure(bg="SlateGray3")
htcon_lbl=Label(htcon_window,text="Enter your height",font=f2)
htcon_lbl.pack(pady=10)
htcon_lbl_cid=Label(htcon_window,text="ID",font=f2)
htcon_ent_cid=Entry(htcon_window,bd=5,font=f2)
htcon_lbl_feet=Label(htcon_window,text="Feet",font=f2)
htcon_ent_feet=Entry(htcon_window,bd=5,font=f2)
htcon_lbl_inches=Label(htcon_window,text="Inches",font=f2)
htcon_ent_inches=Entry(htcon_window,bd=5,font=f2)
htcon_lbl_cid.pack(pady=10)
htcon_ent_cid.pack(pady=10)
htcon_lbl_feet.pack(pady=10)
htcon_ent_feet.pack(pady=10)
htcon_lbl_inches.pack(pady=10)
htcon_ent_inches.pack(pady=10)
htcon_btn_convert=Button(htcon_window,text="Convert",font=f2,command=fun10)
htcon_btn_back=Button(htcon_window,text="Back",font=f2,command=fun11)
htcon_btn_convert.pack(pady=10)
htcon_btn_back.pack(pady=10)
htcon_window.withdraw()

prof_window=Toplevel(cal_window) 
prof_window.title("Profession")
prof_window.geometry("500x450+400+100")
prof_window.configure(bg="SlateGray3")
prof_lbl=Label(prof_window,text="Enter your Profession",font=f2)
prof_lbl.pack(pady=10)
prof_lbl_id=Label(prof_window,text="Identity No.",font=f2)
prof_ent_id=Entry(prof_window,bd=5,font=f2)
prof_lbl_prof=Label(prof_window,text="Profession",font=f2)
prof_ent_prof=Entry(prof_window,bd=5,font=f2)
prof_lbl_id.pack(pady=10)
prof_ent_id.pack(pady=10)
prof_lbl_prof.pack(pady=10)
prof_ent_prof.pack(pady=10)
prof_btn_save=Button(prof_window,text="Save",font=f2,command=fun13)
prof_btn_save.pack(pady=10)
prof_btn_back=Button(prof_window,text="Back",font=f2,command=fun14)
prof_btn_back.pack(pady=10)
prof_window.withdraw()



main_window.mainloop()
from tkinter import * 
base = Tk()
base.geometry("550x550")
base.title('Registration form')
lbl_0 = Label(base, text="Registration form", width=20,font=("bold",20))  
lbl_0.place(x=90,y=60) 
lbl_1 =Label(base, text= "FullName", width=20,font=("bold",10))  
lbl_1.place(x=80,y=130)
enter_1 = Entry(base)  
enter_1.place(x=240,y=130)
lbl_3 = Label(base, text="Email", width=20,font=("bold",10))  
lbl_3.place(x=68,y=180)
enter_3 = Entry(base)  
enter_3.place(x=240,y=180)
lbl_4 = Label(base, text="Gender", width=20,font=("bold",10))  
lbl_4.place(x=70,y=230)
vars = IntVar()
Radiobutton(base, text="Male", padx= 5, variable= vars, value=1).place(x=235, y=230)  
Radiobutton(base, text="Female", padx= 20, variable= vars, value=2).place(x=290,y=230)
lbl_5=Label(base, text ="Country", width=20,font=("bold",11))  
lbl_5.place(x=70,y=280)
list_of_cntry=[ 'India' ,'Canada' , 'US' ,'Germany' ,'UK']
default is (empty) ""  
cv = StringVar()  
drplist = OptionMenu(base, cv, *list_of_cntry)  
drplist.config(width=15)  
cv.set('Select your Country')  
drplist.place(x=240, y=280)
lbl_6=Label(base, text="Language", width=20,font=('bold',10))  
lbl_6.place(x=75,y=330)
vars1=IntVar()
Checkbutton(base,text="English", variable = vars1).place(x=230,y=330)
vars2=IntVar()
Checkbutton(base,text="German", variable=vars2).place(x=290, y=330)
Button(base, text='Submit' , width=20, bg="black",fg='white').place(x=180,y=380)
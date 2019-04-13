'''
iris
'''
import final as f
import numpy
from tkinter import *
import tkinter.messagebox as m

w=Tk()
w.title("IRIS_Flower")
w.geometry("700x300")

def compute():
        # check if user hasn't choosen a method or hasn't filled up any of the flower details!!!
        #if so, return after showing a warning messagebox
        if v.get()==-1:
                m.showwarning(title="Warning",message="Please choose a method!!!")
                return
        if len(E1.get())==0 or len(E2.get())==0 or len(E3.get())==0 or len(E4.get())==0:
                m.showwarning(title="Warning",message="Please enter all flower details!!!")
                return

        
        #compute the name of the flower
        flower_details=numpy.array([float(E1.get()),float(E2.get()),float(E3.get()),float(E4.get())])
        result=f.compute(v.get(),flower_details)
        flower_name="Your flower name is "
        if result[0]==0:
                flower_name=flower_name+"Iris Setosa"
        elif result[0]==1:
                flower_name=flower_name+"Iris Virginica"
        else:
                flower_name=flower_name+"Iris Versicolor"
        m.showinfo(title="your result",message=flower_name)

def reset():
        E1.delete(0, END)
        E2.delete(0, END)
        E3.delete(0, END)
        E4.delete(0, END)

v=IntVar()
v.set(-1)
flower_details=[]

R1=Radiobutton(w,text="   Logistic  ",indicatoron = 0,width = 10,padx = 20,\
               value=1,variable=v,font=("arial",20))
R2=Radiobutton(w,text="  K-nearest  ",indicatoron = 0,width = 10,padx = 20,\
               value=2,variable=v,font=("arial",20))
R3=Radiobutton(w,text=" Naive Bayes ",indicatoron = 0,width = 10,padx = 20,\
               value=3,variable=v,font=("arial",20))
R4=Radiobutton(w,text="Decision Tree",indicatoron = 0,width = 10,padx = 20,\
               value=4,variable=v,font=("arial",20))

head=Label(w,text="Enter flower details",font=("arial",30,"bold"))

L1=Label(w,text="Sepal Length",font=("arial",20))
L2=Label(w,text="Sepal Width",font=("arial",20))
L3=Label(w,text="Petal Length",font=("arial",20))
L4=Label(w,text="Petal Width",font=("arial",20))

E1=Entry(w,font=("arial",20))
E2=Entry(w,font=("arial",20))
E3=Entry(w,font=("arial",20))
E4=Entry(w,font=("arial",20))

B1=Button(w,text=" Submit ",font=("arial",20),command=compute)
B2=Button(w,text=" Cancel ",font=("arial",20),command=reset)

head.grid(row=1,column=3,columnspan=2)
R1.grid(row=1,column=1,rowspan=2)
R2.grid(row=3,column=1,rowspan=2)
R3.grid(row=5,column=1,rowspan=2)
R4.grid(row=7,column=1,rowspan=2)
L1.grid(row=3,column=3)
L2.grid(row=4,column=3)
L3.grid(row=5,column=3)
L4.grid(row=6,column=3)
E1.grid(row=3,column=4)
E2.grid(row=4,column=4)
E3.grid(row=5,column=4)
E4.grid(row=6,column=4)
B1.grid(row=8,column=3)
B2.grid(row=8,column=4)

w.mainloop()

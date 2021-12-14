#importing required modules tkinter and fractions
from tkinter import *
from fractions import Fraction
import tkinter.font as font
import os
import sys
from tkinter import filedialog
import subprocess
#naming the tkinter window
root=Tk()
#giving title to window
root.title("Determinant")
#configuring size and background colour
root.geometry("350x500")
root.configure(bg="grey6")
myc=Canvas(root,bg="grey6", width=350, height=500)
myc.pack(fill="both")
root.configure(bg="black")
myc.create_rectangle(10,10,155,140,fill="grey")
#settinfg predefined fonts to use later
f=font.Font(family='Century Gothic',size="15",weight="bold")
f2=font.Font(family='Cambria',size="12",weight="bold")
f3=font.Font(size="10",weight="bold")
f4=font.Font(size="12", weight="bold")
f5=font.Font(size="11")
#Creating few menu buttons (Quit and New)
mymenu=Menu(root)
mymenu.add_command(label="Quit!", command=root.destroy)
def opennew():
    os.startfile('Inverse and Determinant of 3x3 matrix.py')
mymenu.add_command(label="New",command=opennew)
root.config(menu=mymenu)

#creating entry boxes
e1=Entry(root,width=5)
e1.place(x=15,y=15)
e2=Entry(root,width=5)
e2.place(x=65,y=15)
e3=Entry(root,width=5)
e3.place(x=115,y=15)
e4=Entry(root,width=5)
e4.place(x=15,y=65)
e5=Entry(root,width=5)
e5.place(x=65,y=65)
e6=Entry(root,width=5)
e6.place(x=115,y=65)
e7=Entry(root,width=5)
e7.place(x=15,y=115)
e8=Entry(root,width=5)
e8.place(x=65,y=115)
e9=Entry(root,width=5)
e9.place(x=115,y=115)
#defining the determinant function (It also calculated the inverse)
def determinant():
    #getting the values from entry boxes
    k1=e1.get()
    k2=e2.get()
    k3=e3.get()
    k4=e4.get()
    k5=e5.get()
    k6=e6.get()
    k7=e7.get()
    k8=e8.get()
    k9=e9.get()
    try:
        #converting the values into integers since entries are accepted as strings
        i1=int(k1)
        i2=int(k2)
        i3=int(k3)
        i4=int(k4)
        i5=int(k5)
        i6=int(k6)
        i7=int(k7)
        i8=int(k8)
        i9=int(k9)
        #calculating determinant
        a=i1*(i5*i9-i6*i8)
        b=i2*(i4*i9-i6*i7)
        c=i3*(i4*i8-i7*i5)
        #finding determinant using cofactors formula
        d=a-b+c
        l=Label(root,text="The determinant is:", fg="blue",font=f3)
        l.place(x=5,y=210)
        mylabel=Label(root,text=d,fg="red",font=f4)
        mylabel.place(x=140,y=210)
        #calculating inverse
        #first we check whether the determinant is non-zero or not
        #inverse is not defined for non zero matrices
        if d!=0:
            #caculating co-factors
            l1=(i5*i9-i8*i6)
            l2=-(i4*i9-i7*i6)
            l3=(i4*i8-i7*i5)
            l4=-(i2*i9-i3*i8)
            l5=(i1*i9-i3*i7)
            l6=-(i1*i8-i7*i2)
            l7=(i2*i6-i3*i5)
            l8=-(i1*i6-i3*i4)
            l9=(i1*i5-i2*i4)
            #The inverse is calculated
            #Here we have used fraction module to represent the elements as fractions instead of float values.
            L1=Label(root,text=Fraction(l1,d),font=f5).place(x=105,y=250)
            L2=Label(root,text=Fraction(l2,d),font=f5).place(x=105,y=290)
            L3=Label(root,text=Fraction(l3,d),font=f5).place(x=105,y=330)
            L4=Label(root,text=Fraction(l4,d),font=f5).place(x=165,y=250)
            L5=Label(root,text=Fraction(l5,d),font=f5).place(x=165,y=290)
            L6=Label(root,text=Fraction(l6,d),font=f5).place(x=165,y=330)
            L7=Label(root,text=Fraction(l7,d),font=f5).place(x=225,y=250)
            L8=Label(root,text=Fraction(l8,d),font=f5).place(x=225,y=290)
            L9=Label(root,text=Fraction(l9,d),font=f5).place(x=225,y=330)
        m=Label(root,text="The inverse is:",fg="blue",font=f3).place(x=5,y=290)
        if d==0:
            L10=Label(root,text="Inverse of the matrix is not defined",fg="red",font=f3).place(x=105,y=290)
    except:
        #Handling the exception and informing user about possible errors
        err=Label(root,text="Sorry there was an error",fg='red',font=f4).place(x=5,y=380)
        err1=Label(root,text="The possible errors could be:",fg="blue",font=f4).place(x=5,y=405)
        err2=Label(root,text="1. Missed entering the elements",font=f4).place(x=5,y=435)
        err3=Label(root,text="2. Elements entered are not integers",font=f4).place(x=5,y=460)
mine1=Label(root,text="Enter",fg='green',font=f2).place(x=200,y=20)
mine2=Label(root,text="the",fg='green',font=f2).place(x=205,y=50)
mine3=Label(root,text="elements",fg='green',font=f2).place(x=188,y=80)
mybutton=Button(root, text="CALCULATE",fg="red",bg="white",command=determinant)
mybutton['font']=f
mybutton.place(x=10,y=160)
root.mainloop()

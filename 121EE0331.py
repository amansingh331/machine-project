from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import math


# Design and code written by Aman Kumar(121EE0331)



def opencircuit():
    val1=float(V.get())
    val2=float(I.get())
    val3=float(WA.get())

    Iw=(val3)/(val1)
    Im=math.sqrt((val2*val2)-(Iw*Iw))
    Pw=(val3)/(val2*val1)
    Ro=val1/Iw
    Xo=val1/Im

    Label(text="OPEN CIRCUIT", font=40).place(x=720, y=30)
    Label(text=f"Iw = {round(Iw,3)}", font=30).place(x=720, y=80)
    Label(text=f"Im = {round(Im,3)}", font=30).place(x=720, y=100)
    Label(text=f"cosθ = {round(Pw,3)}", font=30).place(x=720, y=120)
    Label(text=f"Ro = {round(Ro,3)}", font=30).place(x=720, y=140)
    Label(text=f"Xo = {round(Xo,3)}", font=30).place(x=720, y=160)

def shortcircuit():
    val1=float(Vs.get())
    val2=float(Is.get())
    val3=float(Ws.get())

    Ro1=val3/(val2*val2)
    Zo1=val1/val2
    Xo1=math.sqrt((Zo1*Zo1)-(Ro1*Ro1))

    Label(text="SHORT CIRCUIT", font=40).place(x=960, y=30)
    Label(text=f"Zo = {round(Zo1,3)}", font=30).place(x=960, y=80)
    Label(text=f"Ro = {round(Ro1,3)}", font=30).place(x=960, y=100)
    Label(text=f"Xo = {round(Xo1,3)}", font=30).place(x=960, y=120)



def loadpercentage():
    val1=float(Ze1r.get())
    val2=float(Ze1i.get())
    val3=float(Ze2r.get())
    val4=float(Ze2i.get())
    val5=float(Kvalue.get())

    Z1=complex(val1,val2)
    Z2=complex(val3,val4)
    ls1=Z2/(Z1+Z2)
    ls1final=(math.sqrt(((ls1.real)*(ls1.real))+((ls1.imag)*(ls1.imag))))*100
    Label(text=f"percentage load sharing of transformer 1 is = {round(ls1final,3)}%", font=30).place(x=850, y=390)
    Label(text=f"percentage load sharing of transformer 2 is = {round(100-ls1final,3)}%", font=30).place(x=850, y=410)



def calculating():
    val1=float(Br.get())
    val2=float(L.get())
    val3=float(Wi.get())
    val4=float(Th.get())

    test=math.sqrt(val2*val3)
    fin=0.576*(val1*val1)*(val4)*test
    Label(text=f"Pull Force = {round(fin,3)}", font=30).place(x=940, y=620)






root = Tk()
root.title('Calculator')
root.geometry("1600x1000")




global V
global I
global WA
global Vs
global Is
global Ws

Label(text="OPEN CIRCUIT", font=40).place(x=150, y=30)
Label(text="V", font=23).place(x=100,y=80) 
Label(text="I", font=23).place(x=100,y=130) 
Label(text="W", font=23).place(x=100,y=180) 


V=Entry(root, width=15,bd=3, font=20)
V.place(x=150,y=80)

I=Entry(root, width=15,bd=3, font=20)
I.place(x=150,y=130)

WA=Entry(root, width=15,bd=3, font=20)
WA.place(x=150,y=180)

Button(text="calculate", font=20, bg="white", fg="black", width=11, height=2, command=opencircuit).place(x=150,y=240)


# short circuit test

Label(text="SHORT CIRCUIT", font=40).place(x=550, y=30)
Label(text="V", font=23).place(x=500,y=80) 
Label(text="I", font=23).place(x=500,y=130) 
Label(text="W", font=23).place(x=500,y=180) 



Vs=Entry(root, width=15,bd=3, font=20)
Vs.place(x=550,y=80)

Is=Entry(root, width=15,bd=3, font=20)
Is.place(x=550,y=130)

Ws=Entry(root, width=15,bd=3, font=20)
Ws.place(x=550,y=180)


Button(text="calculate", font=20, bg="white", fg="black", width=11, height=2, command=shortcircuit).place(x=550,y=240)







global Ze1r
global Ze1i
global Ze2r
global Ze2i
global K

Label(text="LOAD SHARING PERCENTAGE OF TRANSFORMER", font=40).place(x=350, y=320)
Label(text="Ze1 (Real part)", font=23).place(x=100,y=370) 
Label(text="Ze2 (Real part)", font=23).place(x=100,y=420) 
Label(text="Ze1 (Imiginary part)", font=23).place(x=500,y=370) 
Label(text="Ze2 (Imiginary part)", font=23).place(x=500,y=420)
Label(text="KVA", font=23).place(x=100,y=470) 


Ze1r=Entry(root, width=15,bd=3, font=20)
Ze1r.place(x=200,y=370)

Ze1i=Entry(root, width=15,bd=3, font=20)
Ze1i.place(x=630,y=370)

Ze2r=Entry(root, width=15,bd=3, font=20)
Ze2r.place(x=200,y=420)

Ze2i=Entry(root, width=15,bd=3, font=20)
Ze2i.place(x=630,y=420)

Kvalue=Entry(root, width=15,bd=3, font=20)
Kvalue.place(x=200,y=470)


Button(text="Calculate", font=20, bg="white", fg="black", width=11, height=2, command=loadpercentage).place(x=500,y=470)






global Br
global L
global Wi
global Th

Label(text="MAGNETIC PULL FORCE", font=40).place(x=350, y=560)
Label(text="Br(magnetic flux density)", font=23).place(x=100,y=600) 
Label(text="L(Length of magnet)", font=23).place(x=100,y=650) 
Label(text="W(width of magnet)", font=23).place(x=450,y=600) 
Label(text="Th(thickness of magnet)", font=23).place(x=450,y=650) 


Br=Entry(root, width=15,bd=3, font=20)
Br.place(x=255,y=600)

L=Entry(root, width=15,bd=3, font=20)
L.place(x=255,y=650)

Wi=Entry(root, width=15,bd=3, font=20)
Wi.place(x=600,y=600)

Th=Entry(root, width=15,bd=3, font=20)
Th.place(x=600,y=650)

Button(text="calculate", font=20, bg="white", fg="black", width=11, height=2, command=calculating).place(x=770,y=625)


root.mainloop()
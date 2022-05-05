from tkinter import *
import tkinter.messagebox as m


w = Tk()
w.title(string='Simple Calc')
w.geometry('300x400')


def aler():
    m.showerror("Error","You Ca`t Division for Zero")


def validateentrys():
    W   

def subtraction_userdata():
    try:
        if e3.get()!="":
            e3.configure(state=NORMAL)
            e3.insert(0 ,f"                              ")
        if e1.get() == '' or e2.get() =='':
             m.showwarning("Error","write something no white space")
        else:
            num1spilt = e1.get().replace(' ','')
            num2spilt = e2.get().replace(' ','')
            num1 =float(num1spilt)
            num2 =float(num2spilt)
            result =   num1 - num2
            e3.configure(state=NORMAL)
            e3.insert(0 ,f"result is {result}")
            e3.configure(state="readonly")
            e2.delete(0,"end")
            e1.delete(0,"end")
            e2.insert(0 ,num2spilt)
            e1.insert(0 ,num1spilt)
    except ValueError:
         m.showwarning("Error","Write Only Numbers ")

    

def Division_userdata():
    try:
      if e3.get()!="":
          e3.configure(state=NORMAL)
          e3.insert(0 ,f"                              ")
      if e1.get() == '' or e2.get() =='':
           m.showwarning("Error","write something no white space")
      else:
          num1spilt = e1.get().replace(' ','')
          num2spilt = e2.get().replace(' ','')
          num1 =float(num1spilt)
          num2 =float(num2spilt)
          if num2 == 0:
              e3.insert(0 ,f"                              ")
              e3.configure(state="readonly")
              aler()
          else:   
              result =   num1 / num2
              e3.configure(state=NORMAL)
              e3.insert(0 ,f"result is {result}")
              e3.configure(state="readonly")
              e2.delete(0,"end")
              e1.delete(0,"end")
              e2.insert(0 ,num2spilt)
              e1.insert(0 ,num1spilt)
    except ValueError:
         m.showwarning("Error","Write Only Numbers ")

def multiplication_userdata():
    try:
       if e3.get()!="":
           e3.configure(state=NORMAL)
           e3.insert(0 ,f"                              ")
       if e1.get() == '' or e2.get() =='':
            m.showwarning("Error","write something no white space")
       else:
           num1spilt = e1.get().replace(' ','')
           num2spilt = e2.get().replace(' ','')
           num1 =float(num1spilt)
           num2 =float(num2spilt)
           result =   num1 * num2
           e3.configure(state=NORMAL)
           e3.insert(0 ,f"result is {result}")
           e3.configure(state="readonly")
           e2.delete(0,"end")
           e1.delete(0,"end")
           e2.insert(0 ,num2spilt)
           e1.insert(0 ,num1spilt)
    except ValueError:
         m.showwarning("Error","Write Only Numbers ")

def addition_userdata():
    try:
        if e3.get()!="":
            e3.configure(state=NORMAL)
            e3.insert(0 ,f"                              ")
        if e1.get() == '' or e2.get() =='':
             m.showwarning("Error","write something no white space")
        else:
            num1spilt = e1.get().replace(' ','')
            num2spilt = e2.get().replace(' ','')
            num1 =float(num1spilt)
            num2 =float(num2spilt)
            result =   num1 + num2
            e3.configure(state=NORMAL)
            e3.insert(0 ,f"result is {result}")
            e3.configure(state="readonly")
            e2.delete(0,"end")
            e1.delete(0,"end")
            e2.insert(0 ,num2spilt)
            e1.insert(0 ,num1spilt)
    except ValueError:
         m.showwarning("Error","Write Only Numbers ")


def cls():
    if e1.get() == "" and e3.get() == "" and e2.get() == "":
     m.showwarning("Error","There is no data to delete")
    else:
     e3.configure(state="normal")
     e3.delete(0,"end") 
     e2.delete(0,"end")
     e1.delete(0,"end")
     e3.configure(state="readonly")

def close():
  answer = m.askyesno("close","Are You Sure You Will lose All Data")
  if answer == TRUE:
        w.destroy()
  


fleft = Frame(w)
fleft.pack(side=LEFT)
fright = Frame(w)
fright.pack(side=RIGHT)
fbottom = Frame(w)
fbottom.pack(side=BOTTOM ,pady=50 )

label1 = Label(fleft , text= 'Frist Number').pack(pady=20)
label2 = Label(fleft , text= 'Second Number').pack(pady=20)
label3 = Label(fleft , text= 'Result').pack(pady=20)

e1 = Entry(fright)
e1.pack(pady=20)
e2 = Entry(fright)
e2.pack(pady=20)
e3 = Entry(fright ,state="disabled")
e3.pack(pady=20)


b1 = Button( fbottom, text='+' ,width=5 , command=addition_userdata).grid(row=1, column=1)
b1 = Button( fbottom, text='-' ,width=5 , command=subtraction_userdata).grid(row=1, column=5)
b1 = Button( fbottom, text='*' ,width=5 , command=multiplication_userdata).grid(row=2, column=1)
b1 = Button( fbottom, text='/' ,width=5 , command=Division_userdata).grid(row=2, column=5)

clear = Button( text='clear',width=10 ,command=cls).pack(pady=10) #side=tk.LEFT
exit = Button(text='exit', width=10 , command=close ).pack(pady=10) #side=tk.LEFT


def exit():
    "dummy function"
    pass
w.protocol("WM_DELETE_WINDOW", exit)
btn_quit = Button( text="Quit", command=w.destroy )



w.mainloop()

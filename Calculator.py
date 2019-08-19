from tkinter import *
import math

class calc:

 def answer(self):
    self.expression = self.e.get() #fetches data into expression variable
    try:
     self.value= eval(self.expression) #evaluate the expression using the eval function
    except SyntaxError or NameErrror:
     self.e.delete(0,END)
     self.e.insert(0,'Invalid Input!')
    else:
     self.e.delete(0,END)
     self.e.insert(0,self.value)

 def clear(self): 
  """when clear button is pressed,clears the text input area"""
  self.e.delete(0,END)

 def action(self,argu): 
  """pressed button's value is inserted into the end of the text area"""
  self.e.insert(END,argu)

 def __init__(self,master):
  """Constructor method"""
  master.title('Calulator') 
  master.geometry('150x160')
  master.resizable(0,0) #this removed maximize window button
  self.e = Entry(master,width=22)
  self.e.place(x=5,y=10)
  self.e.focus_set() #Sets focus on the input text area
  
  Button(master,text=" 1 ",width=3,command=lambda:self.action(1)).place(x=10,y=35)
  Button(master,text=" 2 ",width=3,command=lambda:self.action(2)).place(x=40,y=35)
  Button(master,text=" 3 ",width=3,command=lambda:self.action(3)).place(x=70,y=35)
  Button(master,text=" 4 ",width=3,command=lambda:self.action(4)).place(x=10,y=65)
  Button(master,text=" 5 ",width=3,command=lambda:self.action(5)).place(x=40,y=65)
  Button(master,text=" 6 ",width=3,command=lambda:self.action(6)).place(x=70,y=65)
  Button(master,text=" 7 ",width=3,command=lambda:self.action(7)).place(x=10,y=95)
  Button(master,text=" 8 ",width=3,command=lambda:self.action(8)).place(x=40,y=95)
  Button(master,text=" 9 ",width=3,command=lambda:self.action(9)).place(x=70,y=95)
  Button(master,text=" 0 ",width=3,command=lambda:self.action(0)).place(x=40,y=125)
  Button(master,text="clr",width=3,command=lambda:self.clear()).place(x=10,y=125)
  Button(master,text="Ans",width=3,command=lambda:self.answer()).place(x=70,y=125)
  Button(master,text=" + ",width=3,command=lambda:self.action('+')).place(x=110,y=35)
  Button(master,text=" x ",width=3,command=lambda:self.action('*')).place(x=110,y=65)
  Button(master,text=" / ",width=3,command=lambda:self.action('/')).place(x=110,y=95)
  Button(master,text=" - ",width=3,command=lambda:self.action('-')).place(x=110,y=125)  

#Main
root = Tk()
obj=calc(root) #object instantiated
root.mainloop()
